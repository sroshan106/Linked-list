from linkedlist import node,ll

def mergelists(firstlist,secondlist,mergedlist):
    current_first = firstlist.head
    current_second = secondlist.head
    while(current_first!=None and current_second!=None):
        
        if(current_first.data<current_second.data):
            current=current_first.data
            current_first = current_first.next
        else:
            current= current_second.data
            current_second= current_second.next   
        mergedlist.insert(current)
        
    if(current_first is None):
        mergedlist.insert(current_second)
    if(current_second is None):
        mergedlist.insert(current_first.data)



firstNode=node(1)
secondNode=node(3)
thirdNode=node(10)
fourthNode=node(2)
fifthNode=node(4)
sixthNode=node(6)

firstlist = ll()
firstlist.insert(firstNode)
firstlist.insert(secondNode)


secondlist =ll()
secondlist.insert(fourthNode)
secondlist.insert(fifthNode)
secondlist.insert(sixthNode)
secondlist.insert(thirdNode)

print("first list")
firstlist.printlist()
print("second list")
secondlist.printlist()


mergedlist = ll()
mergelists(firstlist,secondlist,mergedlist)
mergedlist.printlist()
