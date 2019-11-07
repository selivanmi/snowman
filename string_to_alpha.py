"""This module provides a function that tokenizes the given text string"""

class StringTokenizer:
    """This class tokenizes the string using the method 'process_string'"""
    def process_string(str):
        """
        This function accepts a text string 
        and returns a list of words it consists of.
        Word is a text string which consists only of letters.
        @param str: Text string to process
        @return: A list of words
        """
        result = []
        alphaIdx = -1  # Value -1 means that the current character is not a letter
        i = 0          # Index of the current character
        for char in str:
            if char.isalpha():
                if alphaIdx < 0:
                    alphaIdx = i
            else:
                if alphaIdx > -1:
                    result.append(str[alphaIdx:i])
                    alphaIdx = -1
            i += 1
        if alphaIdx > -1:
            # We check if the last character is a letter
            # If it is true, we add the substring to the list of words
            result.append(str[alphaIdx:i])
        return result
            
