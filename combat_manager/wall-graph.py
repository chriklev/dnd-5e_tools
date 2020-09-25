

class WallGraph():
    def __init__(self):


class Node(object):
    """
    docstring
    """
    neighbors = []

    def __init__(self, pos_x, pos_y):
        """ Initializes a new Node with a given position
        """
        self.pos_x = pos_x
        self.pos_y = pos_y


@staticmethod
def connect_nodes(node1, node2):
    """ Adds two nodes to each others neighbor list
    """
    node1.neighbors.append(node2)
    node2.neighbors.append(node1)
