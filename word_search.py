# word search

class Word_search:
    def __init__(self, file_location):
        self.__get_text_file(file_location)
        self.file_location = file_location
        self.search_words = ["search"]

    def words_to_find(self):
        return self.search_words

    def __get_text_file(self, file_location):
        self.__verify_crossword_puzzle(file_location)
            
    def __verify_crossword_puzzle(self, file_location):
        try:
            f = open(file_location)
        except:
            self.__throw_error_message("NO FILE FOUND")

        if len(f.read().strip()) == 0:
            f.close()
            self.__throw_error_message("BLANK FILE")
        f.close()
        
        with open(file_location, mode='r') as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        
        for x in content:
            if len(x) < 2:
                self.__throw_error_message("INVALID SEARCH WORD")
            


    def __throw_error_message(self, message):
        raise ValueError(message)
