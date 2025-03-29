FROM node:alpine

ARG APP_NAME="my_app"

RUN npm install -g @angular/cli

WORKDIR /app

RUN ng new $APP_NAME --defaults

WORKDIR /app/$APP_NAME

CMD ["ng", "serve", "--host", "0.0.0.0", "--port", "3000"]