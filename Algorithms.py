class Node :
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Singly_Linkedlist:
    def __init__(self):
        self.head = None
        self.count = 0

    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node
    
    def find_data(self, data): # 입력한 값이 연결리스트 안에 있는지 확인하고 있으면 그 인덱스, 없으면 -1 반환.
        if self.head == None:
            return -1
        index = 0
        temp = self.head
        while temp != None: # while temp 로 줄여서 쓸 수 있다,,
            if temp.val == data:
                return index
            index += 1
            temp = temp.next
        return -1

    def del_with_index(self, idx): # 원하는 인덱스까지 갔다면 이전.넥스트가 현재의 넥스트 노드가 된다.
        temp = self.head
        prev_node = None
        next_node = self.head.next
        i = 0
        if idx == 0:
            self.head = next_node

        while temp:
            if idx == i:
                temp.next=None
                prev_node.next = next_node
                print(temp.val)
                break
            else:
                prev_node, temp, next_node = temp, next_node, next_node.next 
                i += 1

    def show_all(self):
        temp = self.head
        output = ""
        while temp.next:
            output += str(temp.val)
            output += "->"
            temp = temp.next
        return output + str(temp.val)


s = Singly_Linkedlist()
s.append(Node(3))
s.append(Node(2))
s.append(Node(1))
s.append(Node(4))
print(s.show_all())
print(s.find_data(1))
s.del_with_index(2)
#s.insert_with_index(2, Node(5))
#s.insert_with_index(8, Node(5))
print(s.show_all())


