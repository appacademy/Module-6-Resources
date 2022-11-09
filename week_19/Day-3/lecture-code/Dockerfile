# Example dockerfile
FROM node:18-alpine3.15

ENV FLASK_APP=my_app
ENV FLASK_DEBUG=false
ENV REACT_BACKEND_URL="https://my_app.onrender.com"

EXPOSE 3000

WORKDIR /app

COPY package.json .
RUN npm install 

COPY pipfile .
# COPY package-lock.json .
# COPY package*.json . 
RUN pip install

COPY . .

CMD ["npm", "start"]
CMD ["param1", "param2"]
CMD npm start
