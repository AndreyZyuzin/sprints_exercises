import sys

n_days = int(input())
line = sys.stdin.readline().rstrip()


l_max = 0
search_word = ''
for word in line.split():
    if len(word) > l_max:
        l_max = len(word)
        search_word = word


print(search_word, str(l_max), sep='\n')
