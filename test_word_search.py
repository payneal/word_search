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

    def test_word_serach_gets_all_search_words(self):
        search = Word_search("./text_files/search_words_only.txt")
        words = search.words_to_find()
        self.assertEqual(len(words), 1)        

    def test_word_search_actually_gets_words_in_requested_search(self):
        search = Word_search("./text_files/search_words_only.txt")
        words = search.words_to_find()
        self.assertEqual(words,['search'])

if __name__ == '__main__':
    unittest.main()
