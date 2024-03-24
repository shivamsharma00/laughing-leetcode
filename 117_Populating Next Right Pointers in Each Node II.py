class Node:
    def __init__(self, val:int=0, left:'Node'=None, right:'Node'=None, next:'Node'=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

root = []
root.append(Node(7))
root.insert(0, None)
root.insert(0, Node(5))
root.insert(0, Node(4))
root.insert(0, Node(3, left=root[2], right=root[3]))
root.insert(0, Node(2, left=root[1], right=root[2]))
root.insert(0, Node(1, left=root[0], right=root[1]))

temp_list = []
root_node = root[0]
temp_list.append(root_node)
temp_list.append(None)
i = 0

# BFS traversal

while i<len(temp_list):

    # print(i)
    if temp_list[i] != None:
        
        if temp_list[i].left != None:
            temp_list.append(temp_list[i].left)
    
        if temp_list[i].right != None:
            temp_list.append(temp_list[i].right)
    
        if temp_list[i+1] == None:
            temp_list.append(None)
        
    i+=1
temp_list.pop()
# print(temp_list)

for i in range(0, len(temp_list)-1):
    if temp_list[i] is not None:
        temp_list[i].next = temp_list[i+1]


for i in temp_list:
    if i is None:
        print(None)
    else:
        print(i.val, i.next)