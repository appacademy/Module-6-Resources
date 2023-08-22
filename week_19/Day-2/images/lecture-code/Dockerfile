FROM node:18-alpine3.18

ENV FLASK_APP=app
ENV REACT_BACKEND_URL="http://my_app.onrender.com"

EXPOSE 3000 

WORKDIR /app  

COPY package.json .

RUN npm install 

RUN pip install 

COPY . . 

# this is like running "npm start"
CMD ["npm", "start"]