# Example Dockerfile Commands (should not try to build this!)

FROM node:18-alpine3.15
EXPOSE 3000

ENV FLASK_APP=my-app
ENV FLASK_DEBUG=false
ENV REACT_BACKEND_URL='https://heroku-app.myapp.com'

WORKDIR /app

COPY package.json .
COPY package-lock.json .

RUN npm install

RUN pip install

COPY . . 

CMD ['npm', 'start' ]
CMD ['param1', 'param2']
CMD npm start

