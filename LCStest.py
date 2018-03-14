import numpy as np
np.set_printoptions(threshold=np.nan)

a = 'ACBBBCDCEDBADBBEABBEDAEADEBAEB'
b = a + a

for i in range(len(b)):
	print b[i]