fin = open("input.txt", "r", encoding="utf8")
fout = open("output.txt", "w", encoding="utf8")

my_lines= fin.readlines()

qnt_lines = len(my_lines)

letters = 0
words = 0
temp1=''

for line in my_lines:
    for letter in line:
        if letter.isalpha():
            letters += 1
            temp1 += letter
        else:
            temp1 += ' '
    words += len(temp1.split())
    temp1=''

print('Input file contains:\n', letters, ' letters\n', words, ' words\n', qnt_lines, ' lines\n', sep='', file=fout)

fin.close()
fout.close()