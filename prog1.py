str = "mother cleans the window"

def process_string(str):
    """
    This function accepts a sentence and return list of words it is made of.
    @param str: Text string to process
    @return: List of words
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
         result.append(str[alphaIdx:i])
    return result
            
print(process_string(str))
