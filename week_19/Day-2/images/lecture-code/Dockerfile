FROM node:18-alpine3.18

WORKDIR /app

ENV FLASK_APP=app

ENV FLASK_ENV=production

ENV REACT_BACKEND_URL= "https://my_app.onrender.com"

EXPOSE 3000

COPY package.json .

RUN npm install

RUN pip install 

RUN flask db upgrade

RUN flask seed all

COPY . . 

CMD ["npm", "start"]
CMD ["para1", "param2"]
CMD npm start

