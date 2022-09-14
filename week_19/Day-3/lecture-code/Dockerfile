# SAMPLE DOCKERFILE DO NOT ACTUALLY BUILD
FROM node:18-alpine3.15

EXPOSE 3000 

ENV FLASK_APP=my-app
ENV FLASK_DEBUF=false
ENV REACT_BACKEND_URL="https://heroku-my-app.com"

WORKDIR /app 

# COPY AND INSTALL NODE MODULES
COPY package.json .
COPY package-lock.json .
# can use the wildCARD * if needed
# COPY package*.json .
RUN npm install 


# TO COPY AND INSTALL PYTHON DEPENDANCIES
COPY Pipfile .
RUN pip install 

COPY . .
CMD ['npm', 'start']
