try:
	import networkx as nx
	import matplotlib.pyplot as plt
except:
	print 'This program requires networkx and matplotlib packages.'
	exit()


def redraw(func):
	def wrapper(*args, **kwargs):
		plt.close()
		if G.has_edge(list(G.nodes)[0], list(G.nodes)[-1]):
			G.remove_edge(list(G.nodes)[0], list(G.nodes)[-1])
		func(*args, **kwargs)
		G.add_edge(list(G.nodes)[0], list(G.nodes)[-1])
		pos = nx.circular_layout(G)
		color_map = ['blue' if x % 2 == 0 else 'red' for x in list(G.nodes)]
		size_map = [300 if x % 2 == 0 else 600 for x in list(G.nodes)]
		nx.draw(G, pos, node_color=color_map, node_size=size_map, with_labels=True)
	return wrapper


@redraw
def prepare_graph(G):
	G.add_node(1)
	plt.ion()


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
	m = 5
	G = nx.path_graph(2 ** m)
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
