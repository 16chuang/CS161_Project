import sys
import numpy as np

graph = np.zeros((2048, 2048), dtype=int)
lower_paths = np.array((m,n))
upper_paths = np.array((m,n))
shortest_path = np.inf


def LCS(A, B, lower, upper):
	m = len(A)
	n = len(B)

	for col in range(n):
		lower_row = lower[col]
		upper_row = upper[col]

		for row in range(lower_row, upper_row+1):
			# Letters match
			if A[row] == B[col]:
				graph[row][col] = 1
				# If not going to fall off, add previous diagonal
				if (row > lower_row and col > 0):
					graph[row][col] += graph[row-1][col-1]
			# Letters don't match
			else:
				graph[row][col] = 0
				# If not going to fall off, add left or up
				if (row > lower_row and col > 0):
					graph[row][col] += max(graph[row-1][col], graph[row][col-1])

	length = graph[m-1][n-1]

	reconstructPath(lower[0])

	return length

def CLCS(A,B):
	m = len(A)
	n = len(B)

	graph = np.zeros((2048, 2048), dtype=int)
	lower_paths = np.array(m+1)
	upper_paths = np.array(m+1)

	shortest_path, lower_paths[0], upper_paths[0] = LCS(A, B, np.zeros(n), np.full(n, m))
	lower_paths[m] = lower_paths[0]
	upper_paths[m] = upper_paths[0]

	CLCS_recurse(A, B, 0, m)

	return shortest_path

def CLCS_recurse(A, B, lower, upper):
	if upper - lower <= 1:
		return

	mid = (lower + upper) / 2

	path_length, lower_paths[mid], upper_paths[mid] = LCS(A, B, lower_paths[lower], upper_paths[upper])
	if path_length < shortest_path:
		shortest_path = path_length

	# (maybe clear mid)
	CLCS_recurse(A, B, lower, mid)
	# (maybe clear upper)
	CLCS_recurse(A, B, mid, upper)

def main():
	if len(sys.argv) != 1:
		sys.exit('Usage: `python LCS.py < input`')
	
	for l in sys.stdin:
		A,B = l.split()
		print LCS(A,B)
	return

if __name__ == '__main__':
	main()
