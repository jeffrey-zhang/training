import unittest


def sort(arr):
    l = len(arr)
    for i in range(0, l):
        for j in range(i + 1, l):
            if arr[i] >= arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp


class TestSort(unittest.TestCase):
    def test_sort(self):
        arr = [3, 2, 1]
        sort(arr)
        self.assertEqual(arr, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
