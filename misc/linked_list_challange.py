
from misc.Util_tim.Linked_list import LinkedList
from misc.Util_tim.Node import Node

# create list
Interlist = LinkedList()
Interlist2 = LinkedList()
# the linkedlist class is set up to take in node values as is
# Getting a particular node and changing its next value would be a pain so
# I decided to hand write the nodes and their connections

# Creating nodes with values
# first list
node_1 = Node("node 1")
node_2 = Node("node 2")
node_3 = Node("node 3")
node_4 = Node("node 4")
node_5 = Node("node 5")
# second list.
node_6 = Node("node 6")
node_7 = Node("node 7")
node_8 = Node("node 8")
node_9 = Node("node 9")
# inserting the intersection by having a copy of another node.
node_10 = node_5
# setting next's
# list 1
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5
node_5.next = None

#list 2
node_6.next = node_7
node_7.next = node_10
node_10.next = node_8
node_8.next = node_9
node_9.next = None

# Setting heads of both lists
Interlist.head = node_1
Interlist2.head = node_6
# position trackers
loc = 1
xloc = 1

# intersection tracker allows for easy breaking of loop
P = False

# iterating over first list
print("intersection test")
for node in Interlist:
    # iterating over second list
    for xnode in Interlist2:
        # Checks if nodes are same
        if node == xnode:
            print(f'intersect at position {loc} node {node} and {xloc} node {xnode} nodes')
            P = True
            break
        # false increment over position tracker for second list
        else:
            xloc += 1
    # if intersection is found break out of loop
    if P:
        break
    # else reset second list tracker and increment over first llist tracker
    else:
        xloc = 1
        loc += 1

# create list
# looplist = LinkedList([1,2,3,4,5,6,7,8])
looplist = LinkedList()
# create nodes
node_a = Node("4")
node_b = Node("3")
node_c = Node("2")
node_d = Node("1")
# setting start of list
looplist.head = node_a
# setting node order
node_a.next = node_b
node_b.next = node_c
# adding loop
node_c.next = node_a
nodes = []
n = 1
print("Loop detection Test")
for node in looplist:
    if node.next not in nodes:
        nodes.append(node)
        n += 1
    else:
        print(f'The list looped at node {n} reference at {node} ')
        break

