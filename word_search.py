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
        for word_count, word in enumerate(self.search_words):
            self.answer_string += "{}: ".format(
                word) if word_count ==0 else " {}: ".format(word)
            self.__start_looking(word, word_count)
        return self.answer_string


    # helper functions
    def __start_looking(self, word, word_count):
        for word_idx, letter in enumerate(word):
            result= self.__look_for_letter_in_puzzle(
                word, word_count, word_idx, letter)
            if result is True:                
                return True


    def __look_for_letter_in_puzzle(self, word, word_count, word_idx, letter):

        hold= []
        for index_row, row  in enumerate(self.puzzle):
            for index_col, col in enumerate(row):
                if letter == self.puzzle[index_row][index_col]:
                    hold = []
                    if self.__check_for_next_letters(
                            word, index_row, index_col, word_idx, hold):
                        hold = []
                        return True
                    else:
                        hold = []


    def __check_for_next_letters(self, word, index_row, index_col, word_idx, hold):
        if index_row +1 >= len(self.puzzle) or index_col + 1 >= len(self.puzzle):
            return self.__check_word_is_reversed(
                index_row, index_col, word_idx, hold, word)
        else: 
            return self.__check_all_possibilities(
                index_row, index_col, word_idx, hold, word)


    def __check_all_possibilities(self, index_row, index_col, word_idx, hold, word):
       
        result = False 
        if index_col + 1 >=  len(word) or index_row + 1 >= len(word):
            hold = []
            result = self.__check_word_is_reversed(
                index_row, index_col, word_idx, hold, word) 
      
        if len(word) <=  word_idx +1:
            return False

        if result == False and self.puzzle[index_row][index_col+1] ==\
                word[word_idx+ 1]:
            hold = []
            result = self.__check_certain_direction(
                word, index_row, index_col, word_idx, hold, "straight")
        
        if result == False and self.puzzle[index_row +1][index_col] ==\
                word[word_idx+1]:
            hold = []
            result = self.__check_certain_direction(
                word, index_row, index_col, word_idx, hold, "down")
        
        if result == False and self.puzzle[index_row+1][index_col+1] == word[word_idx+1]:
            hold = []
            result = self.__check_certain_direction(
                    word, index_row, index_col,
                    word_idx, hold,"diagonally-descend-forward")
        return result 
    
    def __check_word_is_reversed(self, index_row, index_col, word_idx, hold, word):
        word_found =False
        if len(word) <=  word_idx +1:
            return False

        if word_found == False:
            if index_col -1 >= 0 and self.puzzle[index_row][index_col-1] ==\
                    word[word_idx+1]:
                hold = []
                word_found = self.__check_certain_direction(
                    word, index_row, index_col, word_idx, hold, "backwards")

            if word_found == False and index_row - 1>= 0 and self.puzzle[index_row-1][index_col] ==\
                    word[word_idx+1]:
                hold = []
                word_found =  self.__check_certain_direction(
                    word, index_row, index_col, word_idx, hold, "bottom-up")
            
            if word_found == False:
                hold = []
                word_found = self.__check_diagonally(
                    index_row, index_col, word, word_idx, hold, word_found)
        return word_found


    def __check_diagonally(self, index_row, index_col, word, word_idx, hold, word_found):
        if index_row -1 >= 0 and index_col -1 >=0 and\
                self.puzzle[index_row -1][index_col-1] == word[word_idx+1]:
            word_found = self.__check_certain_direction(
                word, index_row, index_col, word_idx, hold,"diagonally-accend-back")
        
        if word_found == False and index_col + 1 <= len(word) and index_row -1 >= 0:
                if  self.puzzle[index_row - 1][index_col+1] == word[word_idx+1]:
                    word_found = self.__check_certain_direction(
                        word,  index_row, index_col, word_idx, hold,
                        "diagonally-accend-forward") 
        
        if index_col -1 >= 0: 
            if index_row + 1 <  len(self.puzzle): 
                 if word_found == False and self.puzzle[index_row +1][index_col-1] == word[word_idx+1]:
                    word_found = self.__check_certain_direction( 
                        word, index_row, index_col, word_idx, hold,
                        "diagonally-descend-back")
        return word_found
  

    def __check_certain_direction(
            self, word, index_row, index_col,word_idx, hold, direction):

        result = False
        for i in range(0, len(word)):

            if direction == "bottom-up":
                result = self.__do_check(
                    index_row -i , index_col, word_idx+i, hold, word)
            elif direction == "backwards":
                result = self.__do_check(
                    index_row, index_col-i, word_idx +i, hold, word)
            elif direction == "diagonally-accend-back":
                result = self.__do_check(
                    index_row-i, index_col-i, word_idx +i, hold, word)
            elif direction == "straight":
                result = self.__do_check(
                    index_row, index_col+i, word_idx +i, hold, word)
            elif direction == "down":
                result = self.__do_check(
                    index_row+i, index_col, word_idx +i, hold, word)
            elif direction == "diagonally-descend-forward":
                result = self.__do_check(
                    index_row+i, index_col+i, word_idx +i, hold, word)
            elif direction == "diagonally-descend-back":
                result =self.__do_check(
                    index_row+i, index_col-i, word_idx+i, hold, word)
            elif direction == "diagonally-accend-forward":
                result = self.__do_check(
                    index_row -i, index_col +i, word_idx+i, hold, word)
            
            if result == False:
                return False
        return self.__create_answer_from_collected_cords(hold)
    

    def __do_check(self, row_value, col_value, word_idx_value, hold, word):

        if word_idx_value  > len(word)+1:
            return False
        elif  self.puzzle[row_value][col_value] == word[word_idx_value]:
            hold.append((col_value, row_value))
            return True
        else:
            return False
    

    def __create_answer_from_collected_cords(self, hold):
        for x in hold:
            self.answer_string += str(x).replace(" ", "") + " , " 
        self.answer_string = self.answer_string[:-3]
        return True


    def __get_text_file(self, file_location):
        self.__verify_file_and_search_words(file_location)
        with open(file_location, mode='r') as f:
            puzzle = [((x.strip()).replace(" ", "")).split(',') \
                for x in f.readlines()[1:]]
        self.__verify_crossword_puzzle(puzzle)
        self.puzzle = puzzle


    def __verify_crossword_puzzle(self, puzzle):
        if len(puzzle) == 0:
            raise ValueError("NO PUZZLE ATTACHED")
        else:
            puzzle_height, puzzle_width =\
                self.__check_search_words_vs_puzzle_size(puzzle)
            self.__check_puzzle_dimensions(
                puzzle, puzzle_width, puzzle_height)


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
        words = []
        for word in content:
            hold = word.split(',')
            self.__check_individal_search_word(hold[0])
            words.append(hold[0])
        self.search_words = words


    def __check_individal_search_word(self, word):
        if len(word) < 2:
            raise ValueError("INVALID SEARCH WORD")
        if not word.isalpha():
            raise ValueError("INVALID SEARCH WORD")
