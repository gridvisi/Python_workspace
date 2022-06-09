from random import random
print([round(random(),2) for _ in range(17) ])
hight = [round(random(),2) for _ in range(17)]
seq = [round(i,2) for i in list(map(lambda x:x+1,hight))]
print(seq)
print(seq[::-1])
for i in range(len(seq)):
    if seq[i] == seq[::-1][i]:
        print(i,seq[i])

import numpy as np
print(np.random.rand(17))

import numpy as np
print(np.random.sample(17))


import numpy as np
print(np.random.random(17))


import numpy as np
print(np.random.choice(17))

import numpy as np
print(np.random.randint(17))