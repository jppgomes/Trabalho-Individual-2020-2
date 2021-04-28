# develop stage
FROM node:12.4.0-alpine as develop-stage
WORKDIR /client
COPY package*.json ./client
RUN npm install -g @vue/cli && npm install -g @quasar/cli
COPY . .
# build stage
FROM develop-stage as build-stage
