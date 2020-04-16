from linkedlist import node,ll

def commonlist(first,second,cl):
    current1 = first.head
    prev1 = current1
    current2 = second.head
    prev2 = current2
            


node1 = node(1)
node2 = node(2)
node3 = node(5)
first= ll()
first.insert(node1)
first.insert(node2)
first.insert(node3)
node4 = node(2)
node5 = node(5)
node6 = node(7)
second = ll()
second.insert(node4)
second.insert(node5)
second.insert(node6)

cl= ll()
commonlist(first,second,cl)
cl.printlist()
