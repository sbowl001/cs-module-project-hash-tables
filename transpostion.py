# We can use to transform data, like a substitution cipher 


# like a ceasar cypher 

# make a table, mapping every letter to another letter 
# given a string, build a new string by looking up each letter in our transportation table 


# encode_table = {
#     "A": "",
#     "B": "",
#     "C": "",
#     "D": "",
#     "E": "",
#     "F": "",
#     "G": "",
#     "H": "", 
#     "I": "", 
#     "J": "", 
#     "K": "", 
#     "L": "", 
#     "M": "", 
#     "N": "", 
#     "O": "", 
#     "P": "", 
#     "Q": "", 
#     "R": "", 
#     "S": "", 
#     "T": "", 
#     "U": "", 
#     "V": "", 
#     "W": "", 
#     "X": "", 
#     "Y": "", 
#     "Z": "", 
# }
import string 
encode_table = {}

for i in range(26):
    letter = string.ascii_uppercase[i]
    other_letter = string.ascii_uppercase[i - 13]
    encode_table[letter] = other_letter

print(encode_table) 



def encode(s):
    s = s.upper()

    new_string = ""

    for letter in s:
        if letter.isspace():
            new_string += letter 
        else:
            new_string += encode_table[letter]
    return new_string

print(encode("hellow everyone"))