FROM node:18-alpine3.16

ENV FLASK_APP=my-app
ENV FLASK_DEBUG=True
ENV REACT_APP_BACKEND_URL="https://my-app.onrender.com"
EXPOSE 3000

WORKDIR /my-app

COPY package.json .

RUN npm install


COPY Pipfile .
RUN pip install

COPY . .
RUN flask run

CMD ["npm", "start"]
CMD ["param1", "param2"]
CMD npm start