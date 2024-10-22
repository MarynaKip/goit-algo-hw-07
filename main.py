# Вузол дерева
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

# Знаходження найбільшого значення у BST або AVL
def find_max(node):
    current = node

    # Перехід по правим нащадкам
    while current.right is not None:
        current = current.right

    return current.value

# Приклад використання:
root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.right.right = Node(40)

print("Найбільше значення в дереві:", find_max(root))


# Знаходження найменшого значення у BST або AVL
def find_min(node):
    current = node

    # Перехід по лівим нащадкам
    while current.left is not None:
        current = current.left

    return current.value

# Приклад використання:
print("Найменше значення в дереві:", find_min(root))


# Знаходження суми всіх значень у BST або AVL
def find_sum(node):
    if node is None:
        return 0

    # Рекурсивно обчислюємо суму значень лівого і правого піддерев
    return node.value + find_sum(node.left) + find_sum(node.right)

# Приклад використання:
print("Сума всіх значень в дереві:", find_sum(root))
