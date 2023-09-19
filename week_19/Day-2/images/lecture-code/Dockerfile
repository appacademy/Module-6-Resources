FROM node:18-alpine3.18

EXPOSE 3000

ENV FLASK_APP=app
ENV FLASK_DEBUG=True
ENV REACT_BACKEND_URL="https://app_name.onrender.com"

WORKDIR /app

COPY package.json . 
RUN npm install

COPY . .

CMD ["npm", "start"]
# CMD ["arg1", "arg2"]
# CMD npm start 