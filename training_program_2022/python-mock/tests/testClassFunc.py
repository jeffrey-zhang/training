import unittest
from unittest import mock

from ClassFunc import SubClass


class TestSub(unittest.TestCase):

    def test_add(self):
        sub = SubClass()
        sub.add = mock.Mock(return_value=10, side_effect=sub.add)
        result = sub.add(5, 5)
        self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main()