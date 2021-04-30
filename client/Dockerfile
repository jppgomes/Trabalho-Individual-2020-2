# develop stage
FROM node:12.4.0-alpine as develop-stage
WORKDIR /client
COPY . .
RUN npm install -g @vue/cli && npm install -g @quasar/cli
# build stage
FROM develop-stage as build-stage
