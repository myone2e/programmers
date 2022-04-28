class Node:
    def __init__(self, data, next = None): #data 만 입력시 next 초기값은 None이다.
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self): # empty list
        self.no = 0 # 노드의 개수 
        self.head = None # 머리 노드 => head is None 으로 빈 리스트인지 확인 가능 & head.next is None으로 노드가 1개인지도 확인 가능
        self.current = None # 주목하고 있는 노드
        
    def __len__(self):
        return self.no # 연결 리스트의 길이를 반환
    
    def search(self, data):
        cnt = 0
        ptr = self.head # 머리 노드를 참조하도록 초기화
        while ptr is not None:
            if ptr.data == data: # 검색에 성공한 경우
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1 # 검색 실패
    
    def __contains__(self, data):
        return self.search(data) >= 0 # -1 리턴되는거 아니면 True
    
    def add_first(self, data):
        ptr = self.head # 삽입 전의 머리노드
        self.head = self.current = Node(data, ptr) # ptr 집어넣어서 삽입하기 이전의 머리노드 였던 애를 참조하도록 # 헤드는 삽입한 노드를 참조하도록 업데이트
        self.no += 1
    
    def add_last(self, data):
        if self.head is None: # 빈 리스트라면
            self.add_rist(data)
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = self.current = Node(data, None)
            self.no += 1
    
    
    
    
    
    
    

node1 = Node(1) # data = 1, next = None
node2 = Node(3)
node1.next = node2 # 노드 연결하기! => print(node1.next.data) 하면 3 나옴
head = node1
