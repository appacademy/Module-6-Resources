FROM node:18-alpine3.15

EXPOSE 3000

ENV FLASK_APP=my-app
ENV FLASK_DEBUG=True
ENV REACT_BACKEND_URL="https://my-app.onrender.com"


WORKDIR /my-app

COPY package.json .

RUN npm install

COPY pipfile . 

RUN pip install 


COPY . . 

CMD  ["npm", "start"]
CMD  ["parameter1", "parameter2"]
CMD npm start  