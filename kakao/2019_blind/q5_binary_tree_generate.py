
nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]

import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, x, data, left_bound, right_bound): # x 좌표 추가. 자식 노드는 생성 시에는 None
        self.x = x
        self.data = data # 노드 번호
        self.left_bound = left_bound
        self.right_bound = right_bound
        self.left_node = None
        self.right_node = None
        
pre = []
post = []
# 전위 순회 (Preorder Traversal): 루트를 먼저 방문 후 왼쪽 오른쪽
def pre_order(node):
    pre.append(node.data)
    if node.left_node != None:
        pre_order(node.left_node)
    if node.right_node != None:
        pre_order(node.right_node)

# 후위 순회 (Postorder Traversal): 왼쪽 오른쪽 그리고 마지막에 루트
def post_order(node):
    if node.left_node != None:
        post_order(node.left_node)
    if node.right_node != None:
        post_order(node.right_node)
    post.append(node.data)
    
def solution(nodeinfo):
    # [8, 6, 7] x, y, node number
    nodeinfo = [i + [idx + 1] for idx, i in enumerate(nodeinfo)] # 3번째에 index 추가한 것

    # y좌표가 큰 순서대로 우선 정렬 & x좌표 오름차순 하고싶으면 (x[1], -x[0])
    nodeinfo = sorted(nodeinfo, key = lambda x: (x[1], -x[0]), reverse=True)

    # level별로 노드 담기 (now써서 데이터 다돌면서도 레벨 별로 한번만 리스트 생성!)
    level = [] # [[7], [4,2]]
    now = - 1 # 레벨을 의미
    for i in nodeinfo: 
        y = i[1]
        if y != now: # 현재 레벨과 다르다면
            level.append([]) # 레벨 생성
            now = y
        level[len(level)-1].append((i[0], i[2])) # x and node index # 정렬을 해놨기 때문에 마지막에 넣는 것이 항상 맞음

    # x좌표 정렬 위에서 해놓음

    # 루트 노드따로 시작
    root = Node(level[0][0][0], level[0][0][1], 0, 100000) # x, data, lb, ub
    node_list =[[]]
    node_list[0].append(root) 

    for lev in range(1, len(level)):
        node_list.append([]) # 레벨 생성
        for data in level[lev]: # 각 레벨의 노드마다
            x = data[0]
            idx = data[1]
            for parent in node_list[lev-1]: # 위층의 노드들을 돌면서 찾기
                if parent.left_bound <= x and parent.x > x: # 왼쪽 영역에 들어간다면 (lb 오른쪽, 부모 x보다는 왼쪽)
                    now_node = Node(x, idx, parent.left_bound, parent.x) # 부모보다 왼쪽이니 rb 업데이트
                    parent.left_node = now_node # 부모 왼쪽에 할당
                    node_list[lev].append(now_node) # 노드리스트에도 층 맞게 넣어주기
                    break # 하나에만 속하도록!!
                elif parent.right_bound >= x and parent.x < x: # 오른쪽 영역에 들어간다면
                    now_node = Node(x, idx, parent.x, parent.right_bound) # 부모보다 오른쪽이니 lb 업데이트
                    parent.right_node = now_node 
                    node_list[lev].append(now_node)
                    break # 하나에만 속하도록!!
    pre_order(root)
    post_order(root)
    
    answer = [pre, post]
    return answer

print(solution(nodeinfo))
                
                




