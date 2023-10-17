FROM node:18-alpine3.17

ENV FLASK_APP=app
ENV FLASK_DEBUG=False
ENV REACT_BACKEND_URL="https://my_app.onrender.com"

WORKDIR /app

COPY package.json .
RUN npm install

EXPOSE 3000 

COPY . . 

RUN pip install 

CMD ["npm", "start"]
# CMD ["param1", "param2"]
# CMD npm start
