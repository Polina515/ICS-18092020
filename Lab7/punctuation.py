from collections import Counter
import numpy as np
import csv
import sys
import matplotlib.pyplot as plt
seps = ['.', '?', '!', '...']
 
s = '''
Розрізняють системне програмне забезпечення...Які види програмного забезпечення є?Прикладне програмне забезпечення використовується для виконання конкретних завдань.Чи виконання програмного забезпечення комп'ютером полягає у маніпулюванні інформацією та керуванні апаратними компонентами комп'ютера? Наприклад, типовим для персональних комп'ютерів є відтворення інформації на екран та отримання її з клавіатури!Розрізняють системне, інструментальне та прикладне програмне забезпечення.
'''
l = [i for i in s if i in seps]
 
d = {}
i = 0
 
while i < len(s):
  if s[i] in seps:
    if s[i] != '.'  and s[i] != '?' and s[i] != '!':
      if s[i] not in d:
        d[s[i]] = 1
      else:
        d[s[i]] += 1
        
    elif s[i] == '.':
      if i+1 != len(s):
        if s[i+1] == '.':
          if '...' not in d:
            d['...'] = 1
            i += 3
            continue
          else:
            d['...'] = 1
            i += 3
            continue
        else:
          if '.' not in d:
            d['.'] = 1
          else:
            d['.'] += 1
      else:
        if '.' not in d:
          d['.'] = 1
        else:
          d['.'] += 1
          
    
    elif s[i] == '?':
      if i+1 != len(s):
        if s[i+1] == '!':
          
            continue
        else:
          if '?' not in d:
            d['?'] = 1
          else:
            d['?'] += 1
      else:
        if '?' not in d:
          d['?'] = 1
        else:
          d['?'] += 1
    
    elif s[i] == '!':
      if i+1 != len(s):
        if s[i+1] == '?':
          
            continue
        else:
          if '!' not in d:
            d['!'] = 1
          else:
            d['!'] += 1
      else:
        if '!' not in d:
          d['!'] = 1
        else:
          d['!'] += 1
  i += 1
  

c = Counter(d)
fig = plt.figure()
plt.bar(*zip(*c.most_common()), width= .1, color=['b','g','y'])
plt.title('Кількість знаків ')
fig.savefig('punctuation marks.png', dpi=200)
plt.show()

