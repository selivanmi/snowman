from enum import Enum

"""This module contains methods and a function
that tokenizes the given text string"""

def process_string(string):
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
    for char in string:
        if char.isalpha():
            if alphaIdx < 0:
                alphaIdx = i
        else:
            if alphaIdx > -1:
                result.append(string[alphaIdx:i])
                alphaIdx = -1
        i += 1
    if alphaIdx > -1:
        # We check if the last character is a letter
        # If it is true, we add the substring to the list of words
        result.append(string[alphaIdx:i])
    return result

class StringTokenizer(object):
    """This class tokenizes the string using the method 'process_string'"""
    def tokenize(self,string):
         """
         This method accepts a text string
         and returns a list of words it consists of.
         Word is a text string which consists only of letters.
         @param str: Text string to process
         @return: A list of words
         """
         result = []
         alphaIdx = -1  # Value -1 means that the current character is not a letter
         i = 0          # Index of the current character
         for char in string:
             if char.isalpha():
                 if alphaIdx < 0:
                     alphaIdx = i
             else:
                 if alphaIdx > -1:
                    result.append(string[alphaIdx:i])
                    alphaIdx = -1
             i += 1
         if alphaIdx > -1:
           # We check if the last character is a letter
           # If it is true, we add the substring to the list of words
           result.append(string[alphaIdx:i])
         return result

    def get_char_type(self, char):
        if char.isalpha():
            return TokenType.ALPHA
        if char.isdigit():
            return TokenType.NUMBER
        if char.isspace():
            return TokenType.SPACE
        if (',.?!"\':;-()[]'.find(char) > -1):
            return TokenType.PUNCTUATION
        return TokenType.UNKNOWN
            
    def tokenize_with_token_types(self, string):
        """
        This method splits original string into tokens and
        determines token types
        @param string: a sequence of characters to be tokenized
        @return list of objects containing token information - class Token:
        - Token;
        - Token type;
        - First and last indexes in original string
        """
        if len(string) == 0:
            return []
        result = []
        i = 0          # Index of the current character
        cur_token_type = TokenType.UNKNOWN
        for char in string:
            char_type = self.get_char_type(char)
            if i == 0:    #Initialize variables for first character of string
                cur_token_type = char_type
                begin_idx = 0
            elif cur_token_type != char_type: #currently analyzed character is of different type
                #Add current token to result list and start new token
                result.append(Token(string[begin_idx:i], cur_token_type, begin_idx, i))
                begin_idx = i
                cur_token_type = char_type

            i += 1
        #Add last token to result list
        result.append(Token(string[begin_idx:], cur_token_type, begin_idx, len(string))) 
        return result

class TokenType(Enum):
    """
    Class enumerating token types
    """
    UNKNOWN = 0
    ALPHA = 1
    NUMBER = 2
    PUNCTUATION = 3
    SPACE = 4

class Token(object):
    """
    Class representing information about the token:
    - Substring containing token;
    - Token type;
    - First and last indexes in original string
    """

    def __init__(self, substr, toktype, beg, end):
        """ Method for Token object initialization """
        self.token = substr
        self.token_type = toktype
        self.begin = beg
        self.end = end

    def __repr__(self):
        """ Method for building printable representation of the token """
        return '\n{Token = "' + self.token + '"; type = ' + self.token_type.name + '; begin = ' + str(self.begin) + '; end = ' + str(self.end) + '}'

    def __eq__(self, other):
        """
        Method for token object comparison
        Two tokens are considered equal
        only if all token attributes are equal
        """

        #First of all, classes of compared objects should be equal
        if isinstance(other, Token):
            #check if all attributes are equal
            return (self.token == other.token and
                    self.token_type == other.token_type and
                    self.begin == other.begin and
                    self.end == other.end)
        #If "other" object is not Token then it can't be equal to Token 
        return False


        
def main():
    t = StringTokenizer()
    string = 'Mother loves me 2, she clears the window! (joke) Ha-ha!?'
    print(t.tokenize(string))
    result = process_string(string)
    print(result)
    result = t.tokenize_with_token_types(string)
    print(result)
    

if __name__ == '__main__':
    main()



