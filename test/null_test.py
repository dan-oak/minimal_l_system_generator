import unittest


class NullTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, not False)


if __name__ == '__main__':
    unittest.main()
