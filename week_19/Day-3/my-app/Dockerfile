FROM node:18-alpine3.15
# Linux and Node

# some sort of port
EXPOSE 3000

# React App - dependancies (npm install)
# install those dependancies
WORKDIR /app

COPY package.json ./

RUN npm install

# source code
COPY . . 

# start up react app 
CMD ["npm", "start"]