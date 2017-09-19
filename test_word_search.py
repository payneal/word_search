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
    
    def test_word_search_throw_error_if_word_to_search_too_short(self):
        with self.assertRaisesRegexp(ValueError, "INVALID SEARCH WORD"): 
            Word_search("./text_files/too_small_word.txt")
    
    def test_word_search_get_all_seach_words_multiply_words(self):
        search = Word_search("./text_files/two_word_search.txt")
        words = search.words_to_find()
        self.assertEqual(words, ["search", "me"])
    
    def test_word_in_search_is_not_alphabet_letter(self):
        with self.assertRaisesRegexp(ValueError, "INVALID SEARCH WORD"):
            Word_search("./text_files/not_alphabet.txt")        

    def test_word_in_search_two_big_for_puzzle(self):
        with self.assertRaisesRegexp(ValueError, "INVALID SEARCH WORD"):
            Word_search("./text_files/word_too_big_for_search.txt")

    def test_height_and_width_of_puzzle_size(self):
        with self.assertRaisesRegexp(ValueError, "INVALID PUZZLE"):
            Word_search("./text_files/bad_puzzle_size.txt")

    def test_verify_puzzle_exist_after_search(self):
        with self.assertRaisesRegexp(ValueError, "NO PUZZLE ATTACHED"):
            Word_search("./text_files/no_puzzle_just_search.txt")





if __name__ == '__main__':
    unittest.main()
