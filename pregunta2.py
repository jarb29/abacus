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
node7 = Node('Acciones Chiiiiiiiiile', amount=800000.0, parent=node3)
node8 = Node('Acciones Chiiiiiiiiileeeeeeeeeee', amount=800000.0, parent=node7)

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
# def print_tree(root_node):
#   current_node = root_node
#   nivel = 0
#   print("{} {}: {} ".format(" "*nivel, current_node.name, current_node.amount))
 
#   for child in current_node.children:
#     nivel = 2
#     print("{} {}: {} ".format(" "*nivel, child.name, child.amount))
#     while child.children:
#       current_node = child
#       nivel +=2
      # for child in child.children:
        # print("{} {}: {} ".format(" "*nivel, child.name, child.amount))
        # current_node = child



def print_tree(root_node):

  current_node = root_node
  print("{}: {} ".format(current_node.name, current_node.amount))
  nivel = 0
  while current_node.children:
    nivel = 2
    for child in current_node.children:
      
      print("{} {}: {} ".format(" "*nivel, child.name, child.amount))
      current_node = child
      nivel += 2
      # for child in child.children:
        
      #   print("{} {}: {} ".format(" "*nivel, child.name, child.amount))
      #   current_node = child





if __name__ == "__main__":
    print_tree(root)
