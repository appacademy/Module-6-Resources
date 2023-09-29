# Simple websocket set up (React frontend, Flask backend)

Websockets are a protocol for creating a persistant connection between a client and a server, allowing data to be sent in either direction outside of the typical request/response cycle. This makes them very useful for features that rely on live updates, like chatting, gameplay, and notifications.

The goal of this guide is the successful implementation of websockets in a React app with a Flask backend, including deployment on Heroku. For the purposes of this demo, we will be creating a very simple application, that allows live chatting with all active users. This guide is not intended to cover all of the functionality that websockets can provide—it's just a starting point.

Features like message persistance, chatrooms, direct messaging, and notifications won't be covered in this guide. However, hopefully the steps here will get you pointed in the right direction, and give you an implementation you can start building on.

As you go through these steps, you will probably find it useful to look at the [documentation for the `socket.io` JavaScript library](https://socket.io/docs/v3/) that will be used to set up your websockets in your React app, as well as the [documentation for the `Flask-SocketIO` library](https://flask-socketio.readthedocs.io/) that will be used with your Flask server.

## Installation and setup

### For development

Install `flask-socketio` in your backend.
```bash
pipenv install flask-socketio
```
Install socket.io-client in your frontend.
```bash
npm install socket.io-client
```

### For production
Install `eventlet` in your backend. (Specifying the version is necessary here since the latest version will not be compatible with your application).
```bash
pipenv install eventlet==0.30.2
```
Update the contents of your __requirements.txt__ file to match your __Pipfile.lock__ (run the following command in your terminal to do this automatically).
```bash
pipenv lock -r > requirements.txt
```
Replace the final line of your Dockerfile (the `CMD`) with this line:
```dockerfile=
CMD gunicorn --worker-class eventlet -w 1 app:app
```

## Initialize websockets in your Flask app

First create a file to hold your SocketIO object, inside your __app__ folder.

### Inside this file
Import `SocketIO` from `flask_socketio` and initialize an instance of a socketio object.
```python=
from flask_socketio import SocketIO

# create your SocketIO instance
socketio = SocketIO()
```

#### CORS setup
When you instantiate your app, you must set the appropriate `cors_allowed_origins` value for the app to work in production. You could use `cors_allowed_origins="*"` to allow all origins, which would work both locally and in production, although it would be less secure. It would be better practice to set this value to be the actual url of your heroku app. 

```python=
socketio = SocketIO(cors_allowed_origins=[
        "http://actual-app-url.herokuapp.com",
        "https://actual-app-url.herokuapp.com"
    ])
```

However, if we only include our Heroku app on the list of allowed origins, then our websockets won't work when we run the app locally. One solution is to set the allowed origins based on whether the app is running in production or not:
```python=
if os.environ.get("FLASK_ENV") == "production":
    origins = [
        "http://actual-app-url.herokuapp.com",
        "https://actual-app-url.herokuapp.com"
    ]
else:
    origins = "*"

# create your SocketIO instance
socketio = SocketIO(cors_allowed_origins=origins)
```

(There are other approaches you could take here, as well, like setting a value for your allowed origins in your `.env` file and a separate value in your Heroku config vars, which might be more flexible.)


#### Handle a chat message
Let's make a very simple event handler. We can use the `@socketio.on()` decorator to handle specific named events. The decorator will wrap around a function that will manage events of that type.

```python=
@socketio.on("event-type")
def function_to_handle_event(data_included_with_event):
    # code to follow
```

There are some built-in events like `"connection"` which we could write handlers for. We can also define custom events. In this case, we want to handle chat events, so we will use the label `"chat"`. (On the front-end, we will need to make sure that we use the same value when we emit our events so that they get handled by this function).

```python=
@socketio.on("chat")
def handle_chat(data):
    # code to follow
```


When we recieve a chat message, we are going to broadcast that same message back to everyone who is currently connected. (In most applications, you won't need to broadcast to all connected users—instead you may want to set up chatrooms and send messages to the users who are connected to a specific room—see the [documentation](https://flask-socketio.readthedocs.io/en/latest/#rooms) here).

We can use the `broadcast=True` keyword argument  when we use the `emit` function achieve the desired functionality—that will emit the message to all connected users.


```python=
# handle chat messages
@socketio.on("chat")
def handle_chat(data):
    emit("chat", data, broadcast=True)
```

Unlike with a Flask route handler, we will not need to have an actual `return` statement—we send messages explicitly using `emit` or `send` functions.

#### Put it all together...

At this point, your file should look something like this:

```python=
from flask_socketio import SocketIO, emit
import os


# configure cors_allowed_origins
if os.environ.get('FLASK_ENV') == 'production':
    origins = [
        'http://actual-app-url.herokuapp.com',
        'https://actual-app-url.herokuapp.com'
    ]
else:
    origins = "*"

# initialize your socket instance
socketio = SocketIO(cors_allowed_origins=origins)


# handle chat messages
@socketio.on("chat")
def handle_chat(data):
    emit("chat", data, broadcast=True)

```

### Connect the websocket to your application

In the `__init__.py` file in your __app__ folder, you will need to connect your socket instance to your application.

```python=
# import your socketio object (with the other imports at the
# top of the file)
# in this example, the file from the previous step is named socket.py
from .socket import socketio

# initialize the app with the socket instance
# you could include this line right after Migrate(app, db)
socketio.init_app(app)

# at the bottom of the file, use this to run the app
if __name__ == '__main__':
    socketio.run(app)
```



## Front-end React app
In this simple example, the socket will only be relevent on the `Chat` component, so all of our websocket logic will live on a single component. We can create our socket when the component mounts, and then disconnect when the component unmounts. (If you want to use the same socket connection in components throughout your application, you may want to create a context that makes the socket widely available, or even handle it with redux.)

### Initialize your socket
```javascript=
// import the socket
import { io } from 'socket.io-client';

// outside of your component, initialize the socket variable
let socket;
```

### Open the socket connection in a `useEffect`

The socket will, by default, connect immediately upon creation.
```javascript=
const Chat = () => {

    useEffect(() => {

        // create websocket/connect
        socket = io();

        // when component unmounts, disconnect
        return (() => {
            socket.disconnect()
        })
    }, [])
    
    // additional code to be added
};
```

### Create a listener for chat events
We can create a listener for `"chat"` events on our websocket on the same `useEffect` where we created our socket. This listener will be active once the component mounts, and it will remain active until it unmounts, which is the behavior we want.

Let's also use state to store all the messages that we recieve so we can display them.

```javascript=
const Chat = () => {
    const [messages, setMessages] = useState([])

    useEffect(() => {

        // create websocket
        socket = io();
        
        // listen for chat events
        socket.on("chat", (chat) => {
            // when we recieve a chat, add it into our messages array in state
            setMessages(messages => [...messages, chat])
        })
        
        // when component unmounts, disconnect
        return (() => {
            socket.disconnect()
        })
    }, [])
};
```

### Create our input form

```jsx=
// use state for controlled form input
const [chatInput, setChatInput] = useState("");
```


In our return statement, we'll need to include a form that we can submit to send our messages.
```jsx=
// include the form in the return statement for the component
<form onSubmit={sendChat}>
    <input
        value={chatInput}
        onChange={updateChatInput}
    />
    <button type="submit">Send</button>
</form>
```

Next let's write the `sendChat` function that will emit our message through the websocket when the form is submitted.

### Use `socket.emit()` to send chat messages through the websocket
When we send our messages, we want to include a username in addition to the message itself. (In this example, we're including the username with the request so our backend doesn't have to interact with the database to get user information—the backend can just directly broadcast this message to all connected users and it will contain all the information we want to include.)


If we are using our redux store to access the information associated with our current user, we'll use `useSelector`. Depending on the structure of the redux store, the statement we use to get our user information might look something like this:
```jsx=
const user = useSelector(state => state.session.user)
```

Once we have our user information, we're ready to handle sending chats. We get the message contents from `chatInput` (the controlled value of our form input), and we get the username from the value of `user` from our redux store. The `socket.emit()` method takes a first parameter which is the event name—in this case, "chat". (It needs to match the value in our backend event handler—`@socketio.on("chat")`—so that it will get handled by the correct function). The next parameter to the `emit` function will be the data we want to send.

```jsx=
const sendChat = (e) => {
    e.preventDefault()
    // emit a message
    socket.emit("chat", { user: user.username, msg: chatInput });
    // clear the input field after the message is sent
    setChatInput("")
}
```


### Display recieved messages
In our return statement, we'll map over the messages array and print our the username and message for each chat.

```jsx=
// include this in the return statement 
<div>
    {messages.map((message, ind) => (
        <div key={ind}>{`${message.user}: ${message.msg}`}</div>
    ))}
</div>
```

### Put it all together....
At this point, your `Chat` component might look something like this. Make sure to incorporate this component into your application—e.g., if you're using `ReactRouter` you'll probably want to add a `Route` for rendering this component to your __App.js__ file.

```jsx=
import React, { useState, useEffect } from "react";
import { useSelector } from "react-redux";
import { io } from 'socket.io-client';
let socket;

const Chat = () => {
    const [chatInput, setChatInput] = useState("");
    const [messages, setMessages] = useState([]);
    const user = useSelector(state => state.session.user)

    useEffect(() => {
        // open socket connection
        // create websocket
        socket = io();

        socket.on("chat", (chat) => {
            setMessages(messages => [...messages, chat])
        })
        // when component unmounts, disconnect
        return (() => {
            socket.disconnect()
        })
    }, [])

    const updateChatInput = (e) => {
        setChatInput(e.target.value)
    };

    const sendChat = (e) => {
        e.preventDefault()
        socket.emit("chat", { user: user.username, msg: chatInput });
        setChatInput("")
    }

    return (user && (
        <div>
            <div>
                {messages.map((message, ind) => (
                    <div key={ind}>{`${message.user}: ${message.msg}`}</div>
                ))}
            </div>
            <form onSubmit={sendChat}>
                <input
                    value={chatInput}
                    onChange={updateChatInput}
                />
                <button type="submit">Send</button>
            </form>
        </div>
    )
    )
};


export default Chat;
```


## Summary

On our Flask back-end, we create a `SocketIO` instance from the `flask-socketio` package, and used a custom event handler to broadcast all chat messages that are recieved to all connected users. 

In our React front-end, we used `socket.io-client` to create a websocket instance. We added a listener to our socket to handle events where we recieve new chats. We displayed all the chats we recieved, and used a form to submit new chats.


# Websockets & AWS

If you are implementing BOTH websockets and AWS, you will want to do things slightly differently.  AWS will try to use the same worker you have assigned to handle your sockets, so we need to do a few things differently, as listed below...

First:
```
pipenv install gevent
```

Next, 
```
pipenv requirements > requirements.txt
```

In your init.py for app, add the following code before all imports

```python
from gevent import monkey

monkey.patch_all()
```

Replace socketio.init_app(app) with

```python
socketio.init_app(app, async_mode='gevent') 
```

Replace start command on render or in your Dockerfile with

```
gunicorn -k gevent -w 1 app:app
```