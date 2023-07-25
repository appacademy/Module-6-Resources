FROM node:18-alpine3.15

EXPOSE 3000

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . . 
# this is a comment
CMD ["npm", "start"]
