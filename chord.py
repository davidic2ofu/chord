try:
	import networkx as nx
	import matplotlib.pyplot as plt
except:
	print 'This program requires networkx and matplotlib packages.'
	exit()


def redraw(func):
	def wrapper(*args, **kwargs):
		plt.close()
		func(*args, **kwargs)
		nx.draw_shell(G, with_labels=True)
	return wrapper


def prepare_graph(G):
	G.add_node(1)
	plt.ion()
	plt.show()
	nx.draw_shell(G, with_labels=True)


@redraw
def add(G):
	G.add_node(list(G.nodes)[-1]+1)
	G.add_edge(list(G.nodes)[-1], list(G.nodes)[-2])

	
@redraw
def delete(G):
	G.remove_node(list(G.nodes)[-1])
	# G.add_edge(list(G.nodes)[-1], list(G.nodes)[-2])


title = '''
 CHORD implementation program
-============================-
'''
instructions = '''
 User choices:
  1. Add node
  2. Delete node
  3. Exit
'''


if __name__ == '__main__':
	G = nx.Graph()
	prepare_graph(G)
	print title
	while True:
		print instructions
		choice = raw_input('Enter your choice: ')
		if choice == '1':
			add(G)
		if choice == '2':
			delete(G)
		if choice == '3':
			exit()
