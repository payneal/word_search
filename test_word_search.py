# TEST

import unittest
from word_search import Word_search


class Test_Word_Case(unittest.TestCase):

    def test_word_search_gets_blank_file_it_throws_error(self):
        self.assertRaises(
            "Error: NO FILE FOUND", Word_search("./no_file.txt"))


if __name__ == '__main__':
    unittest.main()
