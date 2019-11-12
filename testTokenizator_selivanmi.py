import unittest
import string_to_alpha0
import string_to_alpha1

class TestStringMethods(unittest.TestCase):

  def test_mother_string1(self):
      s = 'mother cleans the window'
      self.assertEqual(string_to_alpha1.StringTokenizer.process_string(s),
                       ['mother', 'cleans', 'the', 'window'])

  def test_empty_string1(self):
      s = ''
      self.assertEqual(string_to_alpha1.StringTokenizer.process_string(s), [])

  def test_no_spaces_string1(self):
      s = 'mothercleansthewindow'
      self.assertEqual(string_to_alpha1.StringTokenizer.process_string(s),
                       ['mothercleansthewindow'])

  def test_digital_string1(self):
      s = '012345'
      self.assertEqual(string_to_alpha1.StringTokenizer.process_string(s), [])

  def test_delimiters_string1(self):
      s = 'mother_cleans+the-window'
      self.assertEqual(string_to_alpha1.StringTokenizer.process_string(s),
                       ['mother', 'cleans', 'the', 'window'])
  def test_mother_string0(self):
      s = 'mother cleans the window'
      self.assertEqual(string_to_alpha0.process_string(s),
                       ['mother', 'cleans', 'the', 'window'])

  def test_empty_string0(self):
      s = ''
      self.assertEqual(string_to_alpha0.process_string(s), [])

  def test_no_spaces_string0(self):
      s = 'mothercleansthewindow'
      self.assertEqual(string_to_alpha0.process_string(s),
                       ['mothercleansthewindow'])

  def test_digital_string0(self):
      s = '012345'
      self.assertEqual(string_to_alpha0.process_string(s), [])

  def test_delimiters_string0(self):
      s = 'mother_cleans+the-window'
      self.assertEqual(string_to_alpha0.process_string(s),
                       ['mother', 'cleans', 'the', 'window'])
        
if __name__ == '__main__':
      str = "mother cleans the window"
      print(string_to_alpha1.StringTokenizer.process_string(str))
      unittest.main()
    
