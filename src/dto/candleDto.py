from __future__ import annotations
from datetime import date, datetime
import pandas as pd
from typing import List
from NNTrade.common.candle_col_name import OPEN, CLOSE, HIGH, LOW, VOLUME

class CandleDto:
    def __init__(self, 
                date_open: date, 
                open: float, 
                high: float,
                low:float,
                close: float, 
                volume):
      self.date_open = date_open
      self.open = open
      self.high = high
      self.low = low
      self.close = close
      self.volume = volume

    @staticmethod
    def from_df(df:pd.DataFrame)-> List[CandleDto]:
        tmp_df = df.copy()
        tmp_df.index.name = "date_open"
        tmp_df = tmp_df.reset_index()
        return [CandleDto(date_open = kwargs['date_open'].date(), 
                          open = kwargs[OPEN],
                          close= kwargs[CLOSE],
                          high = kwargs[HIGH],
                          low = kwargs[LOW],
                          volume= kwargs[VOLUME]
                          ) for kwargs in tmp_df.to_dict(orient='records')]

    def __eq__(self, other) -> bool:
      if not isinstance(other, CandleDto):
        return False
      return self.date_open == other.date_open and \
             self.open == other.open and \
             self.high == other.high and \
             self.low == other.low and \
             self.close == other.close and \
             self.volume == other.volume


