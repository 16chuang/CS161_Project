import sys
import numpy as np
np.set_printoptions(threshold=np.nan)

graph = np.zeros((2048, 2048), dtype = int)
lower_paths = np.zeros((2048, 2048), dtype = int)
upper_paths = np.zeros((2048, 2048), dtype = int)
longest_subsequence = -1
m = 0
n = 0

# TODO: don't assume A is the shorter string

def LCS(A, B, start_row, lower, upper):
	global graph

	lowest_row = lower[0]

	for col in range(n):
		lower_row = lower[col]
		upper_row = upper[col]

		for row in range(max(start_row, lower_row), upper_row+1):
			# Letters match
			if A[row%m] == B[col]:
				graph[row][col] = 1
				# If not going to fall off, add previous diagonal
				if (row > start_row and col > 0):
					graph[row][col] += graph[row-1][col-1]
			# Letters don't match
			else:
				graph[row][col] = 0
				# If not going to fall off, add left or up
				if (row > max(start_row, lower_row) and col > 0):
					graph[row][col] += max(graph[row-1][col], graph[row][col-1])
				# Left
				elif row == max(start_row, lower_row) and col != 0:
					graph[row][col] += graph[row][col-1]
				# Up
				elif col == 0 and row != max(start_row, lower_row):
					graph[row][col] += graph[row-1][col]

	subseq_len = graph[m-1+start_row][n-1]
	print 'lower', lower
	print 'upper', upper
	print 'subseq_len', subseq_len, 'start_row', start_row
	print 'graph', graph.shape
	print np.array2string(graph)#.replace('\n', '')
	upper_path = reconstructPath(A, B, m-1+start_row, n-1, True)
	lower_path =reconstructPath(A, B, m-1+start_row, n-1, False)
	print 'lower_path', lower_path
	print 'upper_path', upper_path
	print '\n'
	return subseq_len, lower_path, upper_path

def reconstructPath(A, B, row, col, upper):
	# NOTE: if running slowly, change this to directly reference already 
	#		allocated upper and lower_paths arrays
	path = np.zeros(n, dtype=int)
	path[n-1] = row

	first_row = row - m + 1
	while col >= 0 and row >= first_row:
		if row == first_row and col == 0:
			break
		if row == first_row:
			col -= 1
			path[col] = row
		elif col == 0:
			row -= 1
			if upper:
				path[col] = max(row, path[col])
			else:
				path[col] = row
		# letters match
		elif A[row%m] == B[col]:
			row -= 1
			col -= 1
			path[col] = row
		else: # letters do not match
			left = graph[row][col-1]
			up = graph[row-1][col]
			if left == up:
				if not upper: # move left
					col -= 1
				else: # move up
					row -= 1
				path[col] = row
			elif left > up:
				# go left
				col -= 1
				path[col] = row
			else: # up > left; go up
				row -= 1
				if upper:
					path[col] = max(row, path[col])
				else:
					path[col] = row
	return path
						
				
def CLCS(A,B):
	global m
	m = len(A)
	global n
	n = len(B)

	global longest_subsequence
	longest_subsequence = -1

	global graph
	graph = np.zeros((2*m,n), dtype = int)
	global lower_paths
	lower_paths = np.zeros((m+1, n), dtype = int)
	global upper_paths
	upper_paths = np.zeros((m+1, n), dtype = int)

	longest_subsequence, lower_paths[0][:n], upper_paths[0][:n] = LCS(A, B, 0, np.zeros(n, dtype=int), np.full(n, m-1))
	lower_paths[m] = lower_paths[0]+m
	upper_paths[m] = upper_paths[0]+m

	CLCS_recurse(A, B, 0, m)
	return longest_subsequence

def CLCS_recurse(A, B, lower, upper):
	if upper - lower <= 1:
		return

	mid = int((lower + upper) / 2)

	global longest_subsequence
	print 'longest_subsequence', longest_subsequence
	subseq_len, lower_paths[mid][:n], upper_paths[mid][:n] = LCS(A, B, mid, lower_paths[lower], upper_paths[upper])
	if subseq_len > longest_subsequence:
		longest_subsequence = subseq_len

	# (maybe clear mid)
	CLCS_recurse(A, B, lower, mid)
	# (maybe clear upper)
	CLCS_recurse(A, B, mid, upper)

def main():
	if len(sys.argv) != 1:
		sys.exit('Usage: `python LCS.py < input`')
	
	for l in sys.stdin:
		A,B = l.split()
		print(CLCS(A,B))
	return

if __name__ == '__main__':
	main()
