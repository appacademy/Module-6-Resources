FROM python:3.11-alpine:3.16

ENV FLASK_APP=my-app
ENV FLASK_ENV=production
ENV REACT_BACKEND_URL="https://heroku-my-app.com"

WORKDIR /app
# /app:   run commands in that terminal level
COPY pipfile .
RUN pip install

COPY package.json .
RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
# CMD ["param1", "param2"]
# CMD npm start