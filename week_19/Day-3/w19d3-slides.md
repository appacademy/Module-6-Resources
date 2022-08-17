<style>
    .present {
        text-align: left;
    }
</style>

---

###### tags: `Week 19` `W19D3`

---

# Docker Images and Dockerfiles
## Week 19 Day 3

---

## Lecture Videos 1 (20 minutes)
Watch:
- Docker Images and Layers (5:00)
- Docker Building and Pushing (12:00)


---


### Docker images
A Docker image is a read-only, executable file that is the template for creating and running a container.

Images are built from Dockerfiles, which contain a set of instructions for building an image. 

When an image is built from a Dockerfile, each instruction creates a layer in the resulting image. Each layer is an intermediate image built on top of the previous layer.

All images are built from Dockerfiles. We can use preexisiting Dockerfiles & images or build or own image using a custom Dockerfile!


---

### Docker image commands
| Command                               | Description                                        |
| ---------------------------------     | -----------------------------------                |
| `docker image ls`                     | list all images currently on machine               |
| `docker image history <IMAGE NAME>`   | show the layers in an image                        |
| `docker image inspect <IMAGE NAME>`   | show all of the metadata associated with an image  |
| `docker image rm <IMAGE NAME>`        | remove a cached image from your system             |
| `docker image push <IMAGE NAME>`      | push an image (that is already built) to dockerhub |
| `docker image build [OPTIONS] <PATH>` | build an image from a Dockerfile based on the path |


---

### Composing Dockerfiles
Each line of execution in a Dockerfile will have its own image layer.

Each line contains an instruction, which must begin with a keyword.

---

### Dockerfile Keywords: `FROM` ([Official documentation](https://docs.docker.com/engine/reference/builder/#from))

All Dockerfiles begin with a `FROM` statement.

In this statement you specify the parent image to start from.

For example, if I wanted to run a Flask server, I might start with a parent image that is the official Python image.

Usage:
```dockerfile=
FROM <IMAGE NAME>
```

---

### Dockerfile Keywords: `WORKDIR` ([Official documentation](https://docs.docker.com/engine/reference/builder/#workdir))

`WORKDIR` changes the working directory in the image, sort of like using `cd` at the command line. That means any subsequent commands will take place in that directory.

Additionally, `WORKDIR` will create a directory if it does not exist yet.

Usage:
```dockerfile=
WORKDIR <DIRECTORY PATH>
```

---

### Dockerfile Keywords: `COPY` ([Official documentation](https://docs.docker.com/engine/reference/builder/#copy))

`COPY` moves a file, files, or directory from your host machine to a location on the image.


Usage:
```dockerfile=
COPY <LOCAL DIR PATH> <IMAGE DIR PATH>
```

---

### Dockerfile Keywords: `ENV` ([Official documentation](https://docs.docker.com/engine/reference/builder/#env))

`ENV` lets you set environment variables in the image.


Usage:
```dockerfile=
ENV <ENV VARIABLE>=<VALUE>
```

---

### Dockerfile Keywords: `EXPOSE` ([Official documentation](https://docs.docker.com/engine/reference/builder/#expose))

`EXPOSE` indicates the port that should be exposed. 

Note that this does not actually publish the port—when you run a container based on the image you would still have to use the `-p external_port:internal_port` flag. The command just sets the intended port in the image's metadata. 

Usage:
```dockerfile=
EXPOSE <PORT NUMBER>
```

---

### A note about EXPOSE vs. publish

`EXPOSE` tells Docker that the image will listen on the specified port within a container at runtime.

This allows the container to easily communicate with others on the same network via this exposed port.


Publishing a port (with the `-p` flag) maps the container's `EXPOSE`'d port to a port on the Docker host (your local machine) via *port forwarding*.

---

### Dockerfile Keywords: `RUN` ([Official documentation](https://docs.docker.com/engine/reference/builder/#run))

`RUN` executes a command on the image.

Usage:
```dockerfile=
RUN <COMMAND>
```

---

### Dockerfile Keywords: `CMD` ([Official documentation](https://docs.docker.com/engine/reference/builder/#cmd))


`CMD` specifies the default process that a container based on the image should execute. An image can only have one `CMD`—if more than one is specified, only the latter will be used.

If you include a command after the image name when running a container with `docker container run ...`, that will replace the CMD in the Dockerfile.

Usage:
```dockerfile=
# exec form (preferred)
CMD ["individual", "strings", "for", "command"]

# params for ENTRYPOINT (if specified)
CMD ["param1", "param2"]

# shell form (will execute in shell)
CMD command param1 param2
```

---


### Layers are Cached on Builds!
When a dockerfile is built the first time it must run each layer of commands.  If there is an error or you made changes, and docker is "rebuilding" an image, it will cache the layers that were successful and unchanged! This does mean we want to consider this process when writing our Dockerfiles



---


### Dockerfile demo
Let's use a Dockerfile to create an image for a simple react app, and then push it to Docker hub.

First we'll need a Dockerfile, so create a file named "Dockerfile" inside our demo directory


---


### Dockerfile demo

Let's start with a base image, and let's include a specific version tag. We want to run an express server, so let's use an official Node image. 


---

### Dockerfile demo

Let's add an `EXPOSE` to indicate the port where we will be serving content.

```dockerfile=
FROM node:15-alpine3.10
# add an EXPOSE
```

---

### Dockerfile demo

Next, let's create a folder called "app" and set it as our working directory so we can build our server.

```dockerfile=
FROM node:15-alpine3.10
EXPOSE 3000
# add a WORKDIR
```


---

### Dockerfile demo


Now we can copy our package.json and package-lock.json to /app—just the files we need to do install dependencies
```dockerfile=
FROM node:15-alpine3.10
EXPOSE 3000
WORKDIR /app
# copy overpackage installation files
```


---


### Dockerfile demo

And now we can install those dependencies.

```dockerfile=
FROM node:15-alpine3.10
EXPOSE 3000
WORKDIR /app
COPY package*.json ./
# install dependencies
```


---

### Dockerfile demo

Then we can copy over the rest of the application files.

```dockerfile=
FROM node:15-alpine3.10
EXPOSE 3000
WORKDIR /app
COPY package*.json ./
RUN npm install
# copy files
```

---

### Dockerfile demo

And provide a command to start the application


```dockerfile=
FROM node:15-alpine3.10
EXPOSE 3000
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
# run app
```

---

### Dockerfile demo
```dockerfile=
FROM node:15-alpine3.10
EXPOSE 3000
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
CMD ["npm", "start"]
```

---

### .dockerignore
Next, we'll need to create a .dockerignore file.
- Why do we ignore node_modules when we're going to npm install anyway?
    - We want the build process to take care of all setup for us, so it should create a new node_modules folder
```dockerfile=
node_modules
```

---

## Building and pushing the image
```bash=
# log in to dockerhub
docker login
# build from the dockerfile located in our current directory
# and tag with your dockerhub username
docker build -t your-dockerhub-username/test_app .
# push the image to dockerhub
docker image push your-dockerhub-username/test_app
# you can remove the local version of the image
docker image rm your-dockerhub-username/test_app
# make a container based on the image—because it does not exist locally, 
# it will pull down the image from your dockerhub
docker container run -p 3000:3000 --name demo your-dockerhub-username/test_app
```

---

## Today's projects

- First Dockerfile
- Dockerfiles Deep Dive
- *Optional - Making Efficient Dockerfiles*

As always, please coordinate within your groups for more project planning after the Docker projects.
