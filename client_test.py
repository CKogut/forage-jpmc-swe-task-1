import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))


  """ ------------ Add more unit tests ------------ """
  def test_getRatio_nonzero(self):
    prices = [
      {'ABC': 126.32, 'DEF': 124.905},
      {'ABC': 128.215, 'DEF': 126.58500000000001}
    ]
    for price in prices:
      self.assertEqual(getRatio(price["ABC"], price["DEF"]), price["ABC"] / price["DEF"])

  def test_getRatio_zero_div(self):
    prices = [
      {'ABC': 0, 'DEF': 124.905},
      {'ABC': 0, 'DEF': 126.58500000000001}
    ]
    for price in prices:
      self.assertEqual(getRatio(price["ABC"], price["DEF"]), 0)

  def test_getRatio_zero_operand(self):
    prices = [
      {'ABC': 126.32, 'DEF': 0},
      {'ABC': 128.215, 'DEF': 0}
    ]
    for price in prices:
      self.assertEqual(getRatio(price["ABC"], price["DEF"]), None)

if __name__ == '__main__':
    unittest.main()
