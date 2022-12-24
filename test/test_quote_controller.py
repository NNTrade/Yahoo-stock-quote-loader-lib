## coding: utf-8
#
#from __future__ import absolute_import
#
#from flask import json
#from six import BytesIO
#
##from src.models.quote_candle import QuoteCandle  # noqa: E501
#from test import BaseTestCase
#
#
#class TestQuoteController(BaseTestCase):
#    """QuoteController integration test stubs"""
#
#    def test_get_quote(self):
#        """Test case for get_quote
#
#        Download quote
#        """
#        query_string = [('quote', 'quote_example'),
#                        ('timeframe', 'day'),
#                        ('date_from', 'date_from_example'),
#                        ('date_till', 'date_till_example')]
#        response = self.client.open(
#            '/api/quote',
#            method='GET',
#            query_string=query_string)
#        self.assert200(response,
#                       'Response body is : ' + response.data.decode('utf-8'))
#
#
#if __name__ == '__main__':
#    import unittest
#    unittest.main()
#