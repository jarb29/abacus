
# importing the module 
from collections import deque  


class Node:
    def __init__(self, name, amount=0.0, parent=None):
        self.name = name
        self.amount = amount
        self.parent = parent
        self.children = []

        if parent:
            self.parent.children.append(self)


root = Node('Total', amount=1000000.0)
node1 = Node('Bonos', amount=300000.0, parent=root)
node2 = Node('Acciones', amount=700000.0, parent=root)
node3 = Node('Bonos US', amount=100000.0, parent=node1)
node4 = Node('Bonos Chile', amount=200000.0, parent=node1)
node5 = Node('Acciones US', amount=500000.0, parent=node2)
node6 = Node('Acciones Chile', amount=200000.0, parent=node2)
# node7 = Node('Acciones Chileee', amount=500000.0, parent=node4)
# node8 = Node('Acciones Chileeeee', amount=600000.0, parent=node6)

"""
Implementa la función print_tree, que debe recibir como único argumento el nodo
raíz de un árbol e imprime los valores de name y amount de cada nodo
de forma ordenada y con la indentación del ejemplo.
Ejemplo:
>> print_tree(root)
Total: 1000000.0
  Bonos: 300000.0
    Bonos US: 100000.0
    Bonos Chile: 200000.0
  Acciones: 700000.0
    Acciones US: 500000.0
    Acciones Chile: 200000.0
>>
"""


### Version Recursiva
# def print_node(node, nivel):
#   print("{} {}: {} ".format(" "*nivel, node.name, node.amount))
#   if node.children:
#     for child in node.children:
#       print_node(child, nivel+2)
# def print_tree(root_node):
#   print_node(root_node, 0)


### Version Iterativa 
def print_node(val, nivel):
  print("{} {}: {} ".format(" "*2*nivel, val.name, val.amount))

def print_tree(root_node):
  current_node = root_node
  childrens = deque()

  i = 0
  while current_node:
    while current_node:
      print_node(current_node, i)
      i +=1
      val_iter = iter(current_node.children)
      childrens.append(val_iter)
      current_node = next(val_iter, None)
    childrens.pop() 
    i -= 1
    current_node = next(childrens[-1], None)
    while not current_node:
      i -= 1
      if len(childrens) > 1:
        childrens.pop()
      else:
        print("\nMerry XMas!!!")
        return 0
      current_node = next(childrens[-1], None)




if __name__ == "__main__":
    print_tree(root)
