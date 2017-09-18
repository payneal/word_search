# TEST

import unittest
from word_search import Word_search


class Test_Word_Case(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_word_search_gets_bad_file_location_throws_error(self):
        with self.assertRaisesRegexp(ValueError, "NO FILE FOUND"): 
            Word_search("./no_file.txt")

    def test_word_search_gets_bad_file_location_throws_error(self):
        with self.assertRaisesRegexp(ValueError, "BLANK FILE"): 
            Word_search("./text_files/empty.txt")

 
    



if __name__ == '__main__':
    unittest.main()
