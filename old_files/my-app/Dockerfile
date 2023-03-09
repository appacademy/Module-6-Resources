FROM node:15-alpine3.10

EXPOSE 3000

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

CMD ["npm", "start"]