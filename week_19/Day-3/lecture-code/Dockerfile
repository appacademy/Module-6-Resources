FROM node:18-alpine3.16

EXPOSE 3000

ENV FLASK_APP=app
ENV FLASK_DEBUG=True
ENV REACT_BACKEND_URL="https://my_app.onrender.com"

WORKDIR /app

COPY package.json .
RUN npm install

RUN pip install 

COPY . . 

CMD ["npm", "start"]
# CMD ["flask", "run", "-p", "5001"]
# CMD ["param1", "param2"]
# CMD npm start
