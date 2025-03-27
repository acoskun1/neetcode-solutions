import typing   

"""
To count the characters in a string into a hashmap use the following method
"""

def countCharacters(s: str) -> dict:
    chars = dict() # create the hashmap

    for i in range(0, len(s)):
        chars[s[i]] = chars.get(s[i], 0) + 1

        # .get(key, default):   key= character whose count is fetched. default= the default value if character does not have a count in the dictionary.

        # chars[s[i]] -> if key character does not exist, adds to the dictionary. If already exists, updates its count.

        # .get(s[i], 0) + 1 increments the count of a character. 
    print(chars)    
    return chars

if __name__ == "__main__":
    countCharacters('hello')
