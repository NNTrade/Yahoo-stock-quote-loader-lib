# Yahoo stock quote loader service
Service for download stock quotes from [yahoo finance](https://finance.yahoo.com/)

## API
[Swagger file](./Swagger.yaml)

## Commands
- build image
```sh
docker build -t ghcr.io/nntrade/datasource/yahoo-stock-quote-loader-srv:1.0 .
```

- push image
```sh
docker push ghcr.io/nntrade/datasource/yahoo-stock-quote-loader-srv:1.0
```

- run image
localhost:5000 -> yahoo-stock-quote-loader-srv:80
```sh
docker run -p 5000:80 -d nn-trade/datasource/yahoo-stock-quote-loader-srv:1.0
```