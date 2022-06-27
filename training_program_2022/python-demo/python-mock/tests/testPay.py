from os import stat
import unittest
from unittest import mock

from Pay import PayApi


class TestPayApi(unittest.TestCase):

    def test_success(self):
        pay = PayApi()
        pay.auth = mock.Mock(return_value=200)
        status = pay.pay(card='123456789', amount=100)
        self.assertEqual(status, 'success')

    def test_failed(self):
        pay = PayApi()
        pay.auth = mock.Mock(return_value=500)
        status = pay.pay(card='123456789', amount=100)
        self.assertEqual(status, 'failed')

    def test_error(self):
        pay = PayApi()
        pay.auth = mock.Mock(return_value=404)
        status = pay.pay(card='123456789', amount=100)
        self.assertEqual(status, 'error')

    def test_exception(self):
        pay = PayApi()
        pay.auth = mock.Mock(return_value=2000)
        status = pay.pay(card='123456789', amount=100)
        self.assertEqual(status, 'error')


if __name__ == '__main__':
    unittest.main()
