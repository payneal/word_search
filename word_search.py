import sys
# word search

class Word_search:
    def __init__(self, file_location):
        self.search_words = None
        self.puzzle = None
        self.answer_string = ''
        self.__get_text_file(file_location)
        

    def words_to_find(self):
        return self.search_words

    def show_puzzle(self):
        return self.puzzle
 
    def solve(self): 
        for word in self.search_words:
            self.__start_looking(word)
        return self.answer_string

    # helper functions
    def __start_looking(self, word):
        for word_idx, letter in enumerate(word):
            result= self.__look_for_letter_in_puzzle(word, word_idx, letter)
            if result is True:
                return True

    def __look_for_letter_in_puzzle(self, word, word_idx, letter):
        self.answer_string += "{}: ".format(word)  
        hold= []
        for index_row, row  in enumerate(self.puzzle):
            for index_col, col in enumerate(row):
                if letter == self.puzzle[index_row][index_col]:
                    hold.append((index_row,index_col))
                    if self.__check_for_next_letters(
                            word, index_row, index_col, word_idx, hold)  is True:
                        return True
                        

    def __check_for_next_letters(self, word, index_row, index_col, word_idx, hold):
        for i in range(1, len(word)):
            if len(self.puzzle) <=  index_col+i:
                 return self.__check_certain_direction_in_reverse(
                    word, index_row, index_col,word_idx, hold, "backwards")
            elif len(self.puzzle) <= index_row+i:
                return self.__check_certain_direction_in_reverse(
                    word, index_row, index_col,word_idx, hold, "bottom-up")
            elif self.puzzle[index_row][index_col+i] == word[word_idx+ i]:
                hold.append((index_row, index_col+i))
            elif self.puzzle[index_row +i][index_col] == word[word_idx+i]:
                hold.append((index_row+i, index_col))
            elif self.puzzle[index_row+i][index_col+i] == word[word_idx+i]:
                hold.append((index_row+i, index_col+i))
            else:
                break
        return self.__create_answer_from_collected_cords(hold) 
  

    def __check_certain_direction_in_reverse(self, word, index_row, index_col,word_idx, hold, direction):
        for i in range(1, len(word)):
            if len(self.puzzle) < index_col+i:
                hold = []
                break
            if direction == "bottom-up":
                self.__reverse_check(index_row -i , index_col, word_idx+i, hold, word)
            elif direction == "backwards":
                self.__reverse_check(index_row, index_col-i, word_idx +i, hold, word)
            else:
                break
        return self.__create_answer_from_collected_cords(hold)
    
    def __reverse_check(self, row_value, col_value, word_idx_value, hold, word):
        if self.puzzle[row_value][col_value] == word[word_idx_value]:
            hold.append((row_value, col_value))
        
    def __create_answer_from_collected_cords(self, hold):
        for x in hold:
            self.answer_string += str(x).replace(" ", "") + " , " 
        self.answer_string = self.answer_string[:-3]
        return True


    def __get_text_file(self, file_location):
        self.__verify_file_and_search_words(file_location)
        with open(file_location, mode='r') as f:
            puzzle = [((x.strip()).replace(" ", "")).split(',') for x in f.readlines()[1:]]
        self.__verify_crossword_puzzle(puzzle)
        self.puzzle = puzzle

    def __verify_crossword_puzzle(self, puzzle):
        if len(puzzle) == 0:
            raise ValueError("NO PUZZLE ATTACHED")
        else:
            puzzle_height, puzzle_width = self.__check_search_words_vs_puzzle_size(
                puzzle)
            self.__check_puzzle_dimensions(puzzle, puzzle_width, puzzle_height)

    def __check_search_words_vs_puzzle_size(self, puzzle):
        puzzle_height = len(puzzle)
        puzzle_width = []
        for line in puzzle:
            puzzle_width.append(len(line))
            for word in self.search_words:
                if len(word) > len(line):
                    raise ValueError("INVALID SEARCH WORD")
        return puzzle_height, puzzle_width

    def __check_puzzle_dimensions(self, puzzle, puzzle_width_list, puzzle_height):
        if len(puzzle) > 0:
            if puzzle_width_list[1:] == puzzle_width_list[:-1]:
                if puzzle_width_list[0] != puzzle_height:
                    raise ValueError("INVALID PUZZLE")
            else:
                raise ValueError("INVALID PUZZLE")

    def __verify_file_and_search_words(self, file_location):
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

