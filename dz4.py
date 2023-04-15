class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.color = "red"

class RedBlackTree():

    COLOR_RED = "red"
    COLOR_BLACK = "black"

    def __init__(self):
        self.root = None

# Метод правого вращения ноды на одну ступень к левой части дерева 
    def rotate_left(self, my_node):
        child = my_node.right
        child_left = child.left
        child.left = my_node
        my_node.right = child_left
        return child

# Метод левого вращения ноды на одну ступень к правой части дерева 
    def rotate_right(self, my_node):
        child = my_node.left
        child_right = child.right
        child.right = my_node
        my_node.left = child_right
        return child

# Метод проверяет, есть ли у данной ноды ненулевое значение, цвет равен ли красному 
    def is_red(self, my_node):
        return my_node != None and my_node.color == RedBlackTree.COLOR_RED

# Метод меняет цвета нод 
    def swap_colors(self, node1, node2):
        temp = node1.color
        node1.color = node2.color
        node2.color = temp

# Метод вставляет ноду с указанным значением в дерево. Если корневой ноды нет, то она корневая 
    def insert(self, data):
        node = None
        if self.root:
            node = self.insert_balance(self.root, data)
            if not node:
                return False
        else:
            node = Node(data)
        self.root = node
        self.root.color = RedBlackTree.COLOR_BLACK
        return True

# Метод сбалансированности дерева  
    def insert_balance(self, my_node, data):
        if my_node == None:
            return Node(data)
        if my_node.data > data:
            my_node.left = self.insert_balance(my_node.left, data)
        elif my_node.data < data:
            my_node.right = self.insert_balance(my_node.right, data)
        else:
            return None
        return self.balanced(my_node)

# Метод проверяет, есть ли у ноды левый или правый указатель, вызывать ли метод balanced
    def balanced(self, my_node):
        if self.is_red(my_node.right) and not self.is_red(my_node.left):
            my_node = self.rotate_left(my_node)
            self.swap_colors(my_node, my_node.left)
        if self.is_red(my_node.left) and self.is_red(my_node.left.left):
            my_node = self.rotate_right(my_node)
            self.swap_colors(my_node, my_node.right)
        if self.is_red(my_node.left) and self.is_red(my_node.right):
            my_node.color = RedBlackTree.COLOR_RED
            my_node.left.color = RedBlackTree.COLOR_BLACK
            my_node.right.color = RedBlackTree.COLOR_BLACK
        return my_node

# Метод для отображния дерева
    def draw_tree(self,node, offset=0):
        if node is not None:
            self.draw_tree(node.right, offset + 4)
            print(' ' * offset + str(node.data) + ' (' + node.color + ')')
            self.draw_tree(node.left, offset + 4)

if __name__ == "__main__":
     node = RedBlackTree()
     print("-----------------------")
     node.insert(4)
     node.draw_tree(node.root)
     print("-----------------------")
     node.insert(2)
     node.draw_tree(node.root)
     print("-----------------------")
     node.insert(9)
     node.draw_tree(node.root)
     print("-----------------------")
     node.insert(7)
     node.draw_tree(node.root)
     print("-----------------------")
     node.insert(1)
     node.draw_tree(node.root)
     print("-----------------------")
     node.insert(-3)
     node.draw_tree(node.root)
     print("-----------------------")
     node.insert(15)
     node.draw_tree(node.root)
     print("-----------------------")
     node.insert(8)
     node.draw_tree(node.root)
     print("-----------------------")
     node.insert(3)
     node.draw_tree(node.root)
     print("-----------------------")
     node.insert(12)
     node.draw_tree(node.root)
     print("-----------------------")
     node.insert(6)
     node.draw_tree(node.root)
     print("-----------------------")
     node.insert(5)
     node.draw_tree(node.root)
     