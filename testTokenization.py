import unittest
import string_to_alpha

class TestStringMethods(unittest.TestCase):

  def test_mother_string(self):
      s = 'mother cleans the window'
      self.assertEqual(string_to_alpha.StringTokenizer.process_string(s),
                       ['mother', 'cleans', 'the', 'window'])

  def test_empty_string(self):
      s = ''
      self.assertEqual(string_to_alpha.StringTokenizer.process_string(s), [])

  def test_no_spaces_string(self):
      s = 'mothercleansthewindow'
      self.assertEqual(string_to_alpha.StringTokenizer.process_string(s),
                       ['mothercleansthewindow'])

  def test_digital_string(self):
      s = '012345'
      self.assertEqual(string_to_alpha.StringTokenizer.process_string(s), [])

  def test_delimiters_string(self):
      s = 'mother_cleans+the-window'
      self.assertEqual(string_to_alpha.StringTokenizer.process_string(s),
                       ['mother', 'cleans', 'the', 'window'])
        
if __name__ == '__main__':
    str = "mother cleans the window"
    print(string_to_alpha.StringTokenizer.process_string(str))
    unittest.main()
