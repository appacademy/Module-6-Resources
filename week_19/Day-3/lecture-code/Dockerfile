FROM node:18-alpine3.15

EXPOSE 3000

WORKDIR /app

COPY package.json .
RUN npm install

ENV FLASK_APP=my-app 
ENV FLASK_DEBUG=False 
ENV RAECT_BACKEND_URL="https//my-app.onrender.com"


RUN pip install
COPY . .

CMD ["npm", "start"]

CMD npm start
docker container run [options] image [commands]

CMD psql -p 5432 -h localhost -U postgres
CMD ["psql", "-p", "5432", "-h", "localhost"]