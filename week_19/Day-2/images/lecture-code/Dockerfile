FROM node:18-alpine3.18

EXPOSE 3000

ENV FLASK_APP=app
ENV FLASK_DEBUG=True

WORKDIR /app

COPY package.json .

RUN npm install

RUN pip install

COPY . .

CMD ["npm", "start"]
