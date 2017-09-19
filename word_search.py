# word search

class Word_search:
    def __init__(self, file_location):
        self.search_words = None
        self.__get_text_file(file_location)
        
    def words_to_find(self):
        return self.search_words

    def __get_text_file(self, file_location):
        self.__verify_crossword_puzzle(file_location)
            
    def __verify_crossword_puzzle(self, file_location):
        try:
            f = open(file_location)
        except:
            raise ValueError("NO FILE FOUND")
        if len(f.read().strip()) == 0:
            f.close()
            raise ValueError("BLANK FILE")
        f.close()
        self.__get_search_content(file_location)

    def __get_search_content(self, file_location):
        with open(file_location, mode='r') as f:
            content = (f.readline()).split()
        for word in content:
            self.__check_individal_search_word(word)
        self.search_words = content

    def __check_individal_search_word(self, word):
        if len(word) < 2:
            raise ValueError("INVALID SEARCH WORD")
        if not word.isalpha():
            raise ValueError("INVALID SEARCH WORD")

