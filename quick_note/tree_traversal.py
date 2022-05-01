class Node:
    def __init__(self, data, left_node, right_node): # 2019 5번 문제 가보면 활용 사례 나옴
        self.data = data
        self.left_node = left_node
        self.right_node = right_node
        
# 전위 순회 (Preorder Traversal): 루트를 먼저 방문
def pre_order(node):
    print(node.data, end = ' ')
    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.right_node != None:
        pre_order(tree[node.right_node])
# 중위 순회 (Inorder Traversal): 왼쪽 자식을 방문한 후에 루트를 방문

def in_order(node):
    if node.left_node != None:
        in_order(tree[node.left_node])
    print(node.data, end = ' ')
    if node.right_node != None:
        in_order(tree[node.right_node])

# 후위 순회 (Postorder Traversal): 오른쪽 자식을 방문한 후에 루트를 방문
def post_order(node):
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node != None:
        post_order(tree[node.right_node])
    print(node.data, end = ' ')
        
n = int(input())      
tree = {}

for i in range(n): # 데이터, 왼쪽, 오른쪽 주어짐
    data, left_node, right_node = input().split()
    if left_node == 'None':
        left_node = None
    if right_node == 'None':
        right_node = None
    tree[data] = Node(data, left_node, right_node)
    
pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])
print()