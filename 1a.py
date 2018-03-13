import numpy as np

print np.inf

# arr = np.zeros((2048, 2048), dtype=int)

# def LCS(A,B):
# 	m = len(A)
# 	n = len(B)

# 	for i in range(1,m+1):
# 		for j in range(1,n+1):
# 			if A[i-1] == B[j-1]:
# 				arr[i][j] = arr[i-1][j-1]+1
# 			else:
# 				arr[i][j] = max(arr[i-1][j], arr[i][j-1])

# 	return arr[m][n]

# str2 = 'BBAA'
# str1 = 'AABABB'

# i = 0
# # for i in range(len(str1)):
# for j in range(len(str2)):
# 	A = str1[i:]+str1[:i]
# 	B = str2[j:]+str2[:j]
# 	lcs = LCS(A,B)
# 	print A, '\t', B, '\t', lcs
# print '\n'

# str2 = 'CBBAA'
# str1 = 'CABABB'

# i = 0
# # for i in range(len(str1)):
# for j in range(len(str2)):
# 	A = str1[i:]+str1[:i]
# 	B = str2[j:]+str2[:j]
# 	lcs = LCS(A,B)
# 	print A, '\t', B, '\t', lcs
# print '\n'

# str2 = 'CCBBAA'
# str1 = 'CCABABB'

# i = 0
# # for i in range(len(str1)):
# for j in range(len(str2)):
# 	A = str1[i:]+str1[:i]
# 	B = str2[j:]+str2[:j]
# 	lcs = LCS(A,B)
# 	print A, '\t', B, '\t', lcs
# print '\n'