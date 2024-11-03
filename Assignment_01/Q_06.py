# Task: Given the string s, use string methods to:
# Split into a list: break the string into a list of substrings based on the delimiter ,.


s:str ="apple,banana,cherry,dates"

words_s = s.split(",")
print(words_s)


# Join with spaces: combine the list of substrings back into a single string, with each element separated by a space.

# s:str ="apple,banana,cherry,dates"


joined = ' '.join( words_s)
print(joined)

