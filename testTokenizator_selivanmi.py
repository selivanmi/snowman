import unittest
import string_to_alpha0
from string_to_alpha0 import StringTokenizer


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
