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

    def test_show_the_puzzle(self):
        search = Word_search("./text_files/easy_puzzle.txt")
        puzzle = search.show_puzzle()
        self.assertEqual(puzzle, [["M","E"],["I", "T"]])
    
    def test_get_puzzle_answer_response_serching_horizontal(self):
        search = Word_search("./text_files/easy_puzzle.txt")
        answer = search.solve()
        self.assertEqual(answer, "ME: (0,0) , (0,1)")

    def test_get_puzzle_answer_response_serching_horizontal_2(self):
        search = Word_search("./text_files/just_as_easy.txt")
        answer = search.solve()
        self.assertEqual(answer, "IT: (0,0) , (0,1)")
    
    def test_get_puzzle_answer_response_searching_backwards(self):
        search = Word_search("./text_files/backward_easy.txt")
        answer = search.solve()
        self.assertEqual(answer, "TO: (0,1) , (0,0)")
    
    def test_get_puzzle_answer_response_searching_vertical(self):
        search = Word_search("./text_files/vertical_easy.txt")
        answer = search.solve()
        self.assertEqual(answer, "BE: (0,0) , (1,0)")

    def test_get_puzzle_answer_response_searching_vertical_2(self):
        search = Word_search("./text_files/vertical_as_easy.txt")
        answer = search.solve()
        self.assertEqual(answer, "AT: (1,0) , (0,0)")
    
    def test_get_puzzle_answer_response_diagonally_descending(self):
        search = Word_search("./text_files/diagonally_decending_easy.txt")
        answer = search.solve()
        self.assertEqual(answer, "GO: (0,0) , (1,1)")
    
    def test_get_puzzle_answer_response_diagnally_accending(self):
        search = Word_search("./text_files/diagonally_accending_easy.txt")
        answer = search.solve()
        self.assertEqual(answer, "BY: (1,1) , (0,0)")

    def test_get_puzzle_answer_response_backwards_in_middle(self):
        search = Word_search("./text_files/backward_middle.txt")
        answer = search.solve()
        self.assertEqual(answer, "HA: (0,2) , (0,1)")

    def test_get_puzzle_answer_response_bottom_up_in_middle(self):
        search = Word_search("./text_files/bottom_up_middle.txt")
        answer = search.solve()
        self.assertEqual(answer, "IN: (2,1) , (1,1)") 

if __name__ == '__main__':
    unittest.main()
