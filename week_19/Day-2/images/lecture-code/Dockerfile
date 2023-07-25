FROM node:18-alpine3.15

EXPOSE 3000

WORKDIR /app

ENV FLASK_APP=app
ENV FLASK_DEBUG=false
ENV REACT_BACKEN_URL="https://my_site.onrender.com"

COPY package.json . 

RUN npm install

RUN pip install

COPY . . 

CMD ["npm", "start"]
CMD ["args", "args1"]
CMD npm start 