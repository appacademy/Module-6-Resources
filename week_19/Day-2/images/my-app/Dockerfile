FROM node:15-alpine3.13

EXPOSE 3000

WORKDIR /app

COPY package.json ./

RUN npm install

COPY . .

CMD ["npm", "start"]