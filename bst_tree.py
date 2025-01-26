class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # Розмітка дерева
    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

# Функція для вставлення значень в дерево
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

# Пошук Значення
def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

# Видалення Значення
def delete(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        root.val = min_value_node(root.right).val
        root.right = delete(root.right, root.val)
    return root

# Функція для отримання  максимального значення
def get_max_value(node):
    current = node
    while current.right:
        current = current.right
    return current.val

# Функція для отримання  мінімального значення
def get_min_value(node):
    current = node
    while current.left:
        current = current.left
    return current.val
            

# 1. додати корінь 
# 2. якщо є лівий опуститися вліво, додати, 
# 3. якщо є правий опуститися вправо, додати
def sum_oll_values(node):
    if not node:
        return 0
    return node.val + sum_oll_values(node.left) + sum_oll_values(node.right)


# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 9)
root = insert(root, 1)
root = insert(root, 31)
root = insert(root, 22)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)

root = delete(root, 7)
print(root)

max_value = get_max_value(root)
min_value = get_min_value(root)
print(f"Максимальне значення - {max_value}, Мінімальне значення - {min_value}")

total_sum = sum_oll_values(root)
print(f"Сума всіх значень: {total_sum}")