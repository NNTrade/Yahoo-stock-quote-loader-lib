from enum import Enum
from flask import Flask
from flask_restful import Resource, Api
from flask_apispec import marshal_with, doc, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from NNTrade.datasource.stock_quote_loader_lib.loader.yahoo import YahooStockQuoteLoader
from NNTrade.datasource.stock_quote_loader_lib.config import QuoteRequest, ChartConfig
from NNTrade.common.time_frame import TimeFrame
from .dto import CandleDto, date

app = Flask(__name__)  # Flask app instance initiated
api = Api(app=app)
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Yahoo quote loader service',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/api/swagger/json/',  # URI to access API Doc JSON
    'APISPEC_SWAGGER_UI_URL': '/api/swagger/ui/'  # URI to access UI of API Doc
})
docs = FlaskApiSpec(app)

class CandleSchema(Schema):
    date_open = fields.Date(required=True, description="Date open candle")
    open = fields.Float(description="Open price")
    high = fields.Float(description="High price")
    low = fields.Float(description="Low price")
    close = fields.Float(description="Close price")
    volume = fields.Float(description="Volume")


class QuoteResponseSchema(Schema):
    CandleSchema = fields.List(fields.Nested(CandleSchema))


class QuoteRequestSchema(Schema):
    stock = fields.String(
        required=True, description="Yahoo stock code", default="AAPL")
    timeframe = fields.Enum(TimeFrame, required=True, description="Timeframe")
    date_from = fields.Date(required=True, description="Download from date")
    date_till = fields.Date(required=True, description="Download till datea")

class QuoteController(MethodResource, Resource):
    @doc(description='Get stock quotes', tags=['Quotes'])
    @use_kwargs(QuoteRequestSchema, location=('query'))
    @marshal_with(CandleSchema(many=True))  # marshalling
    def get(self, **kwargs):
        #stock = request.args.get("stock", default="", type=str)
        
        '''
        Get method represents a GET API method
        '''
        quoteRequest = QuoteRequest(ChartConfig(kwargs["stock"], kwargs["timeframe"]), kwargs["date_from"], kwargs["date_till"])
        loaded_df = YahooStockQuoteLoader().download(quoteRequest,use_cache= False)
        _ret_list = CandleDto.from_df(loaded_df)
        return _ret_list


api.add_resource(QuoteController, '/api/quote')
docs.register(QuoteController)

if __name__ == '__main__':
    app.run(debug=True)
