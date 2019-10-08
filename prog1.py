str = "mother cleans the window"

def process_string(str):
    result = []
    alphaIdx = -1
    i = 0
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
