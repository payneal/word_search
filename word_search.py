# word search

class Word_search:
    def __init__(self, file_location):
        self.text_file = self.__get_text_file(file_location)

    def __get_text_file(self, file_location):
        try:
            f = open(file_location)
        except:
            self.__throw_error_message("NO FILE FOUND")

        if len(f.read().strip()) == 0:
            self.__throw_error_message("BLANK FILE")

    def __throw_error_message(self, message):
        raise ValueError(message)
