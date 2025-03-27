
"""
    {length}{delimiter}{string}
"""

def encode(self, strs):
    #create an blank string
    encoded_string = ''

    #for each string, add the length + delimiter, and the string itself
    for s in strs:
        encoded_string += str(len(s)) + '#' + s

    return encoded_string

def decode(self, string):
    #res: array of decoded strings
    #i  : pointer - index
    res, i = [], 0

    while i < len(string):

        #j  : second pointer, to find the end of the delimiter. Initially equal to i
        #the distance between i and j == the length of the string
        j = i

        #j incremented until delimiter is reached
        while string[j] != '#':
            j += 1

        #length of the string is i to j. j is not included. 
        length = int(string[i:j]) #length is integer casted because it is of type str in the string.
        
        #append everything after delimiter -> j + 1 to end of string -> j + 1 + length
        res.append(string[j+1: j + 1 + length])

        #update beginning of next string to end of previous string -> j + 1 + length
        i = j + 1 + length


    return res



