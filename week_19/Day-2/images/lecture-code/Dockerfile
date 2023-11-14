FROM node:18-alpine3.18  

ENV FLASK_APP=app
ENV FLASK_DEBUG=True
ENV REACT_BACKEND_URL="https://my_app.onrender.com"


WORKDIR /app 

COPY package.json .

RUN npm install 

RUN pip install 

COPY . .

EXPOSE 3000

CMD ["npm", "start"]

# CMD ["param1", "param2"]
# CMD npm start