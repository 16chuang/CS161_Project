import sys
import numpy as np
np.set_printoptions(threshold=np.nan)

graph = np.zeros((8, 5), dtype = int)
lower_paths = np.zeros((2048, 2048), dtype = int)
upper_paths = np.zeros((2048, 2048), dtype = int)
global shortest_path
shortest_path = np.inf
m = 0
n = 0

def LCS(A, B, start_row, lower, upper):
	for col in range(n):
		lower_row = lower[col]
		upper_row = upper[col]

		for row in range(lower_row, upper_row+1):
			# Letters match
			if A[row%m] == B[col]:
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
				elif row == lower_row and col != 0:
					graph[row][col] += graph[row][col-1]
				elif col == 0 and row != lower_row:
					graph[row][col] += graph[row-1][col]

	length = graph[m-1+start_row][n-1]
	print(graph[0:2*m][0:n])
	upper_path = reconstructPath(A, B, m-1+start_row, n-1, True)
	lower_path =reconstructPath(A, B, m-1+start_row, n-1, False)
	return length, lower_path, upper_path

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
				if upper: # move left
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

	graph = np.zeros((8, 5), dtype = int)
	lower_paths = np.zeros((2048, 2048), dtype = int)
	upper_paths = np.zeros((2048, 2048), dtype = int)

	shortest_path, lower_paths[0][:n], upper_paths[0][:n] = LCS(A, B, 0, np.zeros(n, dtype=int), np.full(n, m-1))
	lower_paths[m] = lower_paths[0]
	upper_paths[m] = upper_paths[0]

	CLCS_recurse(A, B, 0, m)
	return shortest_path

def CLCS_recurse(A, B, lower, upper):
	if upper - lower <= 1:
		return

	mid = (lower + upper) / 2

	path_length, lower_paths[mid][:n], upper_paths[mid][:n] = LCS(A, B, mid, lower_paths[lower], upper_paths[upper])
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
		print (CLCS(A,B))
	return

if __name__ == '__main__':
	main()
