FROM node:18-alpine3.16

WORKDIR /app

ENV FLASK_APP=app
ENV FLASK_DEBUG=False   
ENV REACT_BACKEND_URL="https://my-app.onrender.com"

EXPOSE 3000 

COPY package.json .

RUN npm install

RUN pip install

COPY . . 

CMD ["npm", "start"]
CMD ["param1", "param2"]
CMD npm start