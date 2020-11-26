from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
text = "работники предприятие приватизировали приватизировали да не выприватизировали"
b = text.split()
b1 = ''.join(b)
c = Counter(b1)
fig = plt.figure()
plt.bar(*zip(*c.most_common()), width= .5, color=['r', 'b', 'g', 'b', 'y', 'm'])
plt.show()
plt.title('letters counter')
plt.grid(True)
fig.savefig('letters_counter.png', dpi=200)

