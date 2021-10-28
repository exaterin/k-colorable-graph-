import sys
import itertools

vertices = []
edges = []
dictionary = dict()

def read_graph(filename, k, m):
	with open(filename) as f:
		vert_num = -1
		edg_num = -1
		for line in f.readlines():
			if line.startswith('c '): # ignore comments
				continue
			if line.startswith('e '): # add an edge, check vertex number are consistent
				parts = line.split(' ')
				u, v = int(parts[1]), int(parts[2])
				if u > vert_num or v > vert_num:
					print('Warning: invalid vertex number found in edge:', line)
				edges.append((u, v))
				
			if line.startswith('p edge'): # parse problem specification
				parts = line.split(' ')
				vert_num = int(parts[2])
				edg_num = int(parts[3])
				vertices = list(range(1, vert_num + 1))

		if edg_num != len(edges):
			print('Warning: number of edges does not match file header: %d != %d' % (int(m) * len(k), edg_num))

	return vertices, edges

def create_dictinary(m,k):
	count = 0

	for i in range(1, int(k) + 1):
		for j in range(1, int(m) + 1):
			string = str(j) + "," + str(i)
			count += 1
			dictionary[string] = count
			

def write_cnf(cnf, filename, m, k):

	variables =  max(map(abs, itertools.chain(*cnf))) # find the maximum number of a variable used
	cnf_str = '\n'.join(map(lambda c: ' '.join(map(str, c)) + ' 0', cnf)) # concatenate clauses into a string

	print('CNF created, it has %d variables and %d clauses' % (int(m) * int(k), len(cnf)))

	with open(filename, 'w') as f:
		f.write('p cnf %d %d\n' % (int(m) * int(k), len(cnf))) # write basic CNF information
		f.write(cnf_str)

def generate_cnf(vertices, edges, k, m):
	clauses = []
	clause = []
	for j in range (1, int(m) + 1):
		for i in range (1, int(k) + 1):
			clause.append(dictionary.get(str(j) + "," + str(i)))
		clauses.append(clause)
		clause = []

	for i in edges:
		for j in range(1, int(k) + 1):
			clause.append(- int(dictionary.get(str(i[0]) + "," + str(j))))
			clause.append(- int(dictionary.get(str(i[1]) + "," + str(j))))
			clauses.append(clause)
			clause = []


	return clauses

if __name__ == '__main__':
	vertices, edges = read_graph(sys.argv[1],len(vertices) ,sys.argv[2])

	print('Number of vertices:', len(vertices))
	print('Number of edges:', len(edges))
	create_dictinary(len(vertices), sys.argv[2])

	cnf = generate_cnf(vertices, edges, sys.argv[2], len(vertices))

	#print(dictinary)
	write_cnf(cnf, sys.argv[1] + '.cnf', len(vertices), sys.argv[2])