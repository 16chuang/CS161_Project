import numpy as np
np.set_printoptions(threshold=np.nan)

def LCS(A,B):
	m = len(A)
	n = len(B)
	arr = np.zeros((m+1, n+1), dtype=int)

	for i in range(1,m+1):
		for j in range(1,n+1):
			if A[i-1] == B[j-1]:
				arr[i][j] = arr[i-1][j-1]+1
			else:
				arr[i][j] = max(arr[i-1][j], arr[i][j-1])

	print arr
	return arr[m][n]

LCS('ABBA', 'ABABB')