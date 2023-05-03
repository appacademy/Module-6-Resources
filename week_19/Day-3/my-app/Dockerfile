FROM node:18-alpine3.15

EXPOSE 3000

WORKDIR /my-app

COPY package.json ./

RUN npm install
# comments are allowed 
COPY . .

CMD ["npm", "start"]