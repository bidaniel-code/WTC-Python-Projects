import unittest
import word_processor
from word_processor import words_lengths_map

class MyTestCase(unittest.TestCase):
    def test_convert_to_word_list_is_empty(self):
        split_str = word_processor.convert_to_word_list('')
        self.assertEqual([], split_str)

    def test_convert_to_word_list_has_spaces(self):
        split_str = word_processor.convert_to_word_list(" hello    there")
        self.assertEqual(['hello', 'there'], split_str)

    def test_words_longer_than_the_lenght_of_10(self):
        words = word_processor.words_longer_than(10, 'These are indeed interesting, an obvious understatement, times. What say you?')
        self.assertEqual(['interesting', 'understatement'], words)

    def test_words_longer_than_the_lenght_of_2(self):
        words = word_processor.words_longer_than(2, 'These are indeed interesting, an obvious understatement, times. What say you?')
        self.assertEqual(['these','are', 'indeed','interesting', 'obvious', 'understatement', 'times', 'what', 'say', 'you'], words) 

    def test_words_longer_than_the_lenght_of_100(self):
        words = word_processor.words_longer_than(100, 'These are indeed interesting, an obvious understatement, times. What say you?')
        self.assertEqual([], words)  

    def test_words_lengths_map_is_empty(self):
        length_counter = word_processor.words_lengths_map('')
        self.assertEqual({}, length_counter)

    def test_words_lengths_map(self):
        length_counter = word_processor.words_lengths_map('These are indeed interesting, an obvious understatement, times. What say you?')
        self.assertEqual({2: 1, 3: 3, 6: 1, 11: 1, 7: 1, 5: 2, 14: 1, 4: 1}, length_counter)

    def test_lettser_count_map_is_empty(self):
        letter_counter = word_processor.letters_count_map('')
        self.assertEqual(
            {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 
            'n': 0,'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}, letter_counter)
    
    def test_letters_count_map(self):
        letter_counter = word_processor.letters_count_map('These are indeed interesting, an obvious understatement, times. What say you?')
        self.assertEqual(
            {'a': 5, 'b': 1, 'c': 0, 'd': 3, 'e': 11, 'f': 0, 'g': 1, 'h': 2, 'i': 5, 'j': 0, 'k': 0, 'l': 0, 'm': 2,
            'n': 6, 'o': 3, 'p': 0, 'q': 0, 'r': 3, 's': 6, 't': 8, 'u': 3, 'v': 1, 'w': 1, 'x': 0, 'y': 2, 'z': 0}, letter_counter)

    def test_most_used_character_is_empty(self):
        max_val = word_processor.most_used_character('')
        self.assertIsNone(max_val)

    def test_most_used_character(self):
        max_val = word_processor.most_used_character('These are indeed interesting, an obvious understatement, times. What say you?')
        self.assertEqual('e', max_val)