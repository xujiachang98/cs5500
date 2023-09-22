import unittest
import jsonapi

class TestExtendedJSON(unittest.TestCase):
    def test_complex_serialization(self):
        complex_num = 3 + 4j
        json_str = jsonapi.dumps(complex_num)
        loaded_num = jsonapi.loads(json_str)
        self.assertEqual(complex_num, loaded_num)

    def test_range_serialization(self):
        my_range = range(1, 10, 2)
        json_str = jsonapi.dumps(my_range)
        loaded_range = jsonapi.loads(json_str)
        self.assertEqual(list(my_range), list(loaded_range))

if __name__ == '__main__':
    unittest.main()
