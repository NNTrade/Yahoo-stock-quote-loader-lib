import unittest
import logging
from NNTrade.datasource.stock_quote_loader_lib.loader.yahoo import YahooStockQuoteLoader
from NNTrade.datasource.stock_quote_loader_lib.config import QuoteRequest, ChartConfig
from NNTrade.common.time_frame import TimeFrame
from NNTrade.datasource.stock_quote_loader_lib.cache import FileCache
from datetime import date
from src.dto.candleDto import CandleDto

class CandleDtoTestCase(unittest.TestCase):

  logger = logging.getLogger(__name__)
  logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
  cache = FileCache("./cached_files")

  def test_WHEN_parse_df_THEN_get_correct_data(self):
    # Array
    expected_request = QuoteRequest(ChartConfig("EURUSD=X",TimeFrame.D), date(2020,2,4), date(2020,2,7))
    expected_df = YahooStockQuoteLoader(self.cache).download( expected_request, use_cache=False).round(12)
    expected_list = [CandleDto(date(2020,2,4),1.106292605400, 1.106561899185 ,1.103387355804, 1.106292605400, 0 ), 
                   CandleDto(date(2020,2,5),  1.104472041130, 1.104850292205 ,1.099831700325, 1.104728221893, 0 ),
                   CandleDto(date(2020,2,6),  1.100049495697, 1.101285219192 ,1.096551299095, 1.100231051445, 0 )]

    self.logger.info("Loaded DF")
    self.logger.info(expected_df)
    
    # Act
    self.logger.info("to_dict()")
    self.logger.info(expected_df.to_dict(orient='records'))
    asserted_list = CandleDto.from_df(expected_df)

    # Assert
    self.logger.info("Asserted List")
    self.logger.info(asserted_list)

    self.assertEqual(len(asserted_list), len(expected_list))
    for i in range(0,3):
      asserted_candle = asserted_list[i]
      expected_candle = expected_list[i]
      self.assertEqual(asserted_candle.date_open, expected_candle.date_open)
      self.assertAlmostEqual(asserted_candle.open, expected_candle.open,10)
      self.assertAlmostEqual(asserted_candle.high, expected_candle.high,10)
      self.assertAlmostEqual(asserted_candle.low, expected_candle.low,10)
      self.assertAlmostEqual(asserted_candle.close, expected_candle.close,10)
      self.assertAlmostEqual(asserted_candle.volume, expected_candle.volume,10)
 