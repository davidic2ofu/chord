import random
import math

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
		pos = nx.circular_layout(G)
		color_map = ['blue' if not G.node[i]['value'] else 'red' for i in list(G.nodes)]
		size_map = [200 if not G.node[i]['value'] else 600 for i in list(G.nodes)]
		nx.draw(G, pos, node_color=color_map, node_size=size_map, with_labels=True)
	return wrapper


def check_valid(func):
	def wrapper(*args, **kwargs):
		key = args[1]
		if is_valid_node(G, key):
			func(*args, **kwargs)
		else:
			print '{} is not a valid node.'.format(key)
	return wrapper


@redraw
def prepare_graph(G):
	plt.ion()
	nx.set_node_attributes(G, {i: None for i in list(G.nodes)}, 'value')
	add(G)


@redraw
def add(G, value='default'):
	while True:
		num = random.randint(0, len(list(G.nodes)) - 1)
		if not G.node[num]['value']:
			break
	insert = '** {} data at node {} **'.format(value, num) if value == 'default' else value
	G.node[num]['value'] = insert
	update_node(G, num)
	update_node(G, G.node[num]['succ'])
	update_node(G, G.node[num]['pred'])


@check_valid
@redraw
def delete(G, num):
	G.node[num]['value'] = None
	update_node(G, G.node[num]['succ'])
	update_node(G, G.node[num]['pred'])


def update_node(G, num):
	print 'Updating successor, predecessor, and finger table data for node {}...'.format(num)
	G.node[num]['succ'] = get_succ(G, num)
	G.node[num]['pred'] = get_pred(G, num)
	G.node[num]['finger_table'] = create_finger_table(G, num)


def get_succ(G, k):
	for i in range(1, len(list(G.nodes)) + 1):
		index = (i + k) % (len(list(G.nodes)))
		if G.node[index]['value']:
			return index


def get_pred(G, k):
	for i in range(len(list(G.nodes)) - 1, -1, -1):
		index = (i + k) % (len(list(G.nodes)))
		if G.node[index]['value']:
			return index


def create_finger_table(G, k):
	def get_finger_value(k):
		for i in range(0, len(list(G.nodes)) + 1):
			index = (i + k) % (len(list(G.nodes)))
			if G.node[index]['value']:
				return index
	finger_table = {}
	m = int(math.log(len(list(G.nodes)), 2))
	for i in range(m):
		f = (k + 2 ** i) % len(list(G.nodes))
		g = (k + 2 ** (i + 1))
		finger_range = [j % len(list(G.nodes)) for j in range(f, g)]
		finger_table[i] = (finger_range, get_finger_value(f))
	return finger_table


def get_finger_table(G, k):
	if G.node[num]['finger_table']:
		G.node[num]['value'] = None
	else:
		print '!! Node at id {} does not exist !!'.format(num)


@check_valid
def print_node_info(G, key):
	print '\nNODE {} INFO'.format(key)
	print '{}\'s successor: {}'.format(key, G.node[key]['succ'])
	print '{}\'s predecessor: {}'.format(key, G.node[key]['pred'])
	print '{}\'s finger table:'.format(key)
	print '\nindex    finger range    finger value'
	m = int(math.log(len(list(G.nodes)), 2))
	for i in range(m):
		finger_range = '[{}...{}]'.format(G.node[key]['finger_table'][i][0][0], G.node[key]['finger_table'][i][0][-1])
		print '{: <9}{: <16}{}'.format(i, finger_range, G.node[key]['finger_table'][i][1])


@check_valid
def lookup(G, node):
	def find_successor(node, id):
		succ = G.node[node]['succ']
		g = succ if succ > node else succ + len(G.nodes)
		check_range = [j % len(list(G.nodes)) for j in range(node, g + 1)]
		print '\nChecking table at node {}...'.format(node)
		if id in check_range:
			result = G.node[node]['succ']
			print '\nLOOKUP SUCCESSFUL!\nData found at node {}: {}'.format(result, G.node[result]['value'])
			return result
		else:
			n_prime = get_pred(G, id)
			print '\nTable at node {} points to node {}'.format(node, n_prime)
			return find_successor(n_prime, id)
	key = int(raw_input('Enter key id to lookup from node {}: '.format(node)))
	if key in range(len(list(G.nodes))):
		succ = find_successor(node, key)
	else:
		print '{} is not a valid key.'.format(key)


def is_valid_node(G, k):
	return True if G.node[k]['value'] else False


title = '''
 CHORD implementation program
-============================-
'''
instructions = '''
 User choices:
  1. Add node
  2. Delete node
  3. Lookup data
  4. View node configuration (succ, pred, finger table)
  5. Exit
'''


if __name__ == '__main__':
	print title
	G = nx.cycle_graph(2 ** 6)
	prepare_graph(G)
	while True:
		print instructions
		choice = raw_input('Enter your choice: ')
		if choice == '1':
			add(G)
		if choice == '2':
			key = int(raw_input('Which node id to delete: '))
			delete(G, key)
		if choice == '3':
			node = int(raw_input('Enter node id to lookup from: '))
			lookup(G, node)
		if choice == '4':
			key = int(raw_input('Enter node id to analyze: '))
			print_node_info(G, key)
		if choice == '5':
			print '\nHave a nice day!\n'
			exit()
