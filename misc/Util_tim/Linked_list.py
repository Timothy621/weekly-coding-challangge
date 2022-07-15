from misc.Util_tim.Node import Node


class LinkedList:
    # creates the list and sets start of list to non
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    # defines the reference for the list moving through all the nodes
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return str(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
