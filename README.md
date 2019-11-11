# server_with_flask

rest сервер с использованием deris и flask

для работы нужно сначала собрать образ: ``` docker build . -t echo ```

потом запустить: ``` docker-compose up --no-deps --build ```

примеры запросов:

1) ```curl -X PUT -d '{"message": "2"}' -H "Content-Type: application/json" 127.0.0.1:5000/23/```
2) ```curl -X GET 127.0.0.1:5000/23/```
