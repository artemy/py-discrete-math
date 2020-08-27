import unittest

from main import set_as_matrix, create_tau, create_rho, compose, inverse, transitive, create_set, sort, unique


class TestMatrix(unittest.TestCase):
    def test_set_as_matrix(self):
        test_set = [[2, 1], [2, 2], [2, 3], [2, 5], [4, 3]]

        expected = '00000\n11101\n00000\n00100\n00000\n'
        self.assertEqual(expected, set_as_matrix(test_set))

    def test_create_matrix(self):
        expected = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3]]
        self.assertEqual(expected, create_set(range(1, 3), range(1, 4), lambda x, y: True))

    def test_create_rho(self):
        expected = [[1, 3], [2, 2], [2, 3], [2, 4], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [4, 2], [4, 3], [4, 4],
                    [5, 3]]
        self.assertEqual(expected, create_rho())

    def test_create_tau(self):
        expected = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [3, 1]]
        self.assertEqual(expected, create_tau())

    def test_compose(self):
        test_set1 = [[1, 3], [2, 2], [2, 3], [2, 4], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [4, 2], [4, 3], [4, 4],
                     [5, 3]]
        test_set2 = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [3, 1]]
        expected = [[1, 1], [2, 1], [2, 2], [3, 1], [3, 2], [3, 3], [4, 1], [4, 2], [5, 1]]
        self.assertEqual(expected, compose(test_set1, test_set2))

    def test_inverse(self):
        test_set = [[1, 3], [2, 2], [2, 3], [2, 4], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [4, 2], [4, 3], [4, 4],
                    [5, 3]]
        expected = [[1, 3], [2, 2], [2, 3], [2, 4], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [4, 2], [4, 3], [4, 4],
                    [5, 3]]
        self.assertEqual(expected, inverse(test_set))

    def test_transitive(self):
        test_set = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [3, 1]]
        expected = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]
        self.assertEqual(expected, transitive(test_set))

    def test_sort(self):
        test_set = [[3, 4], [1, 5], [2, 1], [2, 1]]
        expected = [[1, 5], [2, 1], [2, 1], [3, 4]]
        self.assertEqual(expected, sort(test_set))

    def test_unique(self):
        set = [[3, 4], [1, 5], [2, 1], [2, 1], [1, 5]]
        expected = [[3, 4], [1, 5], [2, 1]]
        self.assertListEqual(expected, unique(set))


if __name__ == '__main__':
    unittest.main()
