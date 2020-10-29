import csv
import sys

from collections import Counter
filename = "task3.txt"
num_words = 0

five_time_words = set()
words_array = []
list1 =[]
list2 = []
with open ( filename, 'r',encoding= 'utf-8') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
        cnt = Counter(words)
        print("кількість повторів кожного слова в тексті:",cnt)
cnt1 = cnt.most_common(3)
print("")
print("Найбільш повторювані слова:",cnt1)
f.close()


























#print(list(cnt1.keys()))

    #print(list(cnt.keys()))
   # if cnt.values >= 5:
       # print(cnt.keys())
        #words_array.appended(cnt.keys(i))
        
#print (())

        
#print(list(cnt.keys()))
#print(num_words)
f.close()
