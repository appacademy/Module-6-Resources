FROM node:18-alpine3.18

EXPOSE 3000

WORKDIR /my_app

COPY package.json ./

RUN npm install

COPY . .

CMD ["npm", "start"]