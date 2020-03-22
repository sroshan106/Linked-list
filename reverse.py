from linkedlist import node,ll
def reverse(link):
    prev=None
    current = link.head
    if not current:
        return
    while(current):
        nextnode = current.next
        current.next = prev
        prev = current
        current = nextnode       
    link.head = prev


def add(link):
    cur = link.head
    if not cur:
        return
    while(cur):
        if(cur.data+1)%10 != 0:
            cur.data+=1
            break;
        else:
            cur.data = 0
            cur=cur.next
node1 = node(1)
node2 = node(9)
node3 = node(6)
link = ll()
link.insert(node1)
link.insert(node2)
link.insert(node3)
rev = ll()
reverse(link)
add(link)
reverse(link)
link.printlist()

