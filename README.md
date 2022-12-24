# Yahoo stock quote loader service
Service for download stock quotes from [yahoo finance](https://finance.yahoo.com/)

## API
[Swagger file](./Swagger.yaml)

## Commands
- build image
```sh
docker image build -t nn-trade/datasource/yahoo-stock-quote-loader-srv .
```
- run image
localhost:5000 -> yahoo-stock-quote-loader-srv:80
```sh
docker run -p 5000:80 -d nn-trade/datasource/yahoo-stock-quote-loader-srv
```