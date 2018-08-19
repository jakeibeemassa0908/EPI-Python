"""
Programming Challenge Description:
Write a program that finds the first non repeated character in a string.
Input:
Your program should read lines of text from standard input.
Output:
For each line of input, print the first non-repeated character to standard output, one character per line.


Programming Challenge Description:
Write a program to determine the Mth to last element of a sequence.
Input:
Your program should read lines of text from standard input. Each line will contain a series of space delimited integers. The last integer in the series is M.
Output:
Print to standard output, the Mth integer from the end of the sequence, one integer per line. If M is larger than the sequence size, print a blank line.





Programming Challenge Description:
Write a program to print a 2D array (n x m) in spiral order (clockwise)
Input:
Your program should read lines of text from standard input. Each line contains three semicolon-delimited items. The first is 'n'(rows), the second is 'm'(columns), and the third is a single space delimited list of characters/numbers in row major order.
Output:
Print out the matrix in clockwise fashion, one per line, space delimited.


You are given two strings. Determine if the second string is a substring of the first. The second string may contain an asterisk (*) which should be treated as a wild card that matches zero or more characters. The asterisk can be escaped by a \ char in which case it should be interpreted as a literal * character. The strings can contain English letters and numbers, *, and \.
Input:
Your program should read lines of text from standard input. Each line will contain two strings separated by a comma.
Output:
For each line of input, if the second string is a substring of the first, print "true" (lowercase). Otherwise print "false" (lowercase), one per line.
"""


import sys
line="3;3;1 2 3 4 5 6 7 8 9"
rows = int(line.split(';')[0])
columns = int(line.split(";")[1])
num = line.split(";")[2].strip().split(" ")
result =[]

matx = [[0 for x in range(columns)] for y in range(rows)] 

i=0
for row in range(rows):
    if row%2 == 0:
        for column in range(columns):
            matx[row][column]=num[i]
            i+=1
    else:
        for column in reversed(range(columns)):
            matx[row][column]=num[i]
            i+=1

for row in range(rows):
    for column in range(columns):
        result.append(matx[row][column])

print(" ".join(result))
    
