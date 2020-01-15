import unittest
import string_to_alpha0
from string_to_alpha0 import StringTokenizer
from string_to_alpha0 import TokenType
from string_to_alpha0 import Token

class TestStringTokenizerWithTypes(unittest.TestCase):

     def setUp(self):
         self.t = StringTokenizer()

     def test_alpha_string(self):
          s = 'mother cleans the window'
          self.assertEqual(self.t.tokenize_with_token_types(s)[0],
                       Token("mother", TokenType.ALPHA, 0, 6))
          self.assertEqual(len(self.t.tokenize_with_token_types(s)), 7)

     def test_class_empty_string(self):
          s = ''
          self.assertEqual(self.t.tokenize(s), [])

     def test_digit_string(self):
          s = '2 mothers clean 100 windows!!!'
          self.assertEqual(self.t.tokenize_with_token_types(s)[0],
                       Token("2", TokenType.NUMBER, 0, 1))
          self.assertEqual(len(self.t.tokenize_with_token_types(s)), 10)

     def test_punct_string(self):
          s = '- Can 2 mothers clean 100 windows???'
          self.assertEqual(self.t.tokenize_with_token_types(s)[0],
                       Token("-", TokenType.PUNCTUATION, 0, 1))
          self.assertEqual(len(self.t.tokenize_with_token_types(s)), 14)

     def test_space_string(self):
          s = ' 2 mothers clean 100 windows???'
          self.assertEqual(self.t.tokenize_with_token_types(s)[0],
                       Token(" ", TokenType.SPACE, 0, 1))
          self.assertEqual(len(self.t.tokenize_with_token_types(s)), 11)

     def test_last_character_string(self):
          s = '2 mothers clean 100 windows???'
          self.assertEqual(self.t.tokenize_with_token_types(s)[9],
                       Token("???", TokenType.PUNCTUATION, 27, 30))
          self.assertEqual(len(self.t.tokenize_with_token_types(s)), 10)
          
     def test_alpha_string(self):
          s = 'мама мыла раму'
          self.assertEqual(self.t.tokenize_with_token_types(s)[0],
                       Token("мама", TokenType.ALPHA, 0, 4))
          self.assertEqual(len(self.t.tokenize_with_token_types(s)), 5)

          
class TestStringTokenizer(unittest.TestCase):

     def setUp(self):
         self.t = StringTokenizer()


     def test_class_mother_string(self):
          s = 'mother cleans the window'
          self.assertEqual(self.t.tokenize(s),
                       ['mother', 'cleans', 'the', 'window'])

     def test_class_empty_string(self):
          s = ''
          self.assertEqual(self.t.tokenize(s), [])

     def test_class_no_spaces_string(self):
          s = 'mothercleansthewindow'
          self.assertEqual(self.t.tokenize(s),
                       ['mothercleansthewindow'])

     def test_class_digital_string(self):
          s = '012345'
          self.assertEqual(self.t.tokenize(s), [])

     def test_class_delimiters_string(self):
          s = 'mother_cleans+the-window'
          self.assertEqual(self.t.tokenize(s),
                       ['mother', 'cleans', 'the', 'window'])    

class TestStringMethods(unittest.TestCase):

    def test_mother_string(self):
          s = 'mother cleans the window'
          self.assertEqual(string_to_alpha0.process_string(s),
                       ['mother', 'cleans', 'the', 'window'])

    def test_empty_string(self):
          s = ''
          self.assertEqual(string_to_alpha0.process_string(s), [])

    def test_no_spaces_string(self):
          s = 'mothercleansthewindow'
          self.assertEqual(string_to_alpha0.process_string(s),
                       ['mothercleansthewindow'])

    def test_digital_string(self):
          s = '012345'
          self.assertEqual(string_to_alpha0.process_string(s), [])

    def test_delimiters_string(self):
          s = 'mother_cleans+the-window'
          self.assertEqual(string_to_alpha0.process_string(s),
                       ['mother', 'cleans', 'the', 'window'])
  
  
        
if __name__ == '__main__':
    unittest.main()
