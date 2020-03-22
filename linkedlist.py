class node:
    def __init__(self,data):
        self.data = data
        self.next = None

    
class ll:
    def __init__(self):
        self.head=None

    def listlength(self):
        lastnode = self.head
        count=1
        while(lastnode.next!=None):
            count+=1
            lastnode=lastnode.next
        return count
        
    def insert(self,newNode):
        if(self.head==None):
            self.head=newNode
        else:
            lastNode= self.head
            while(lastNode.next!=None):
                lastNode= lastNode.next
            lastNode.next=newNode

    def insertBeg(self,newNode):
        if(self.head==None):
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode
    def insertat(self,newNode,pos):
        if(pos<0 or pos >self.listlength()):
            print("Invalid position")
            return
        currentnode=self.head
        currentpos=0
        
        while True:
            if(currentpos==pos):
                previousnode.next=newNode
                newNode.next=currentnode
                break
            previousnode=currentnode
            currentnode=currentnode.next
            currentpos+=1
    def delete(self):
        currentnode=self.head
        while(currentnode.next!=None):
            previousnode= currentnode
            currentnode=currentnode.next
        previousnode.next=None

    def deletebw(self,pos):
        if(pos<0  or pos>self.listlength()):
            print("Invalid")
            return
        
        currentnode=self.head
        currentpos=0
        while(currentpos!=pos):
            previousnode=currentnode
            currentnode=currentnode.next
            currentpos+=1
        previousnode.next=currentnode.next
        currentnode.next=None
        
    def printlist(self):
        node = self.head
        while(node!=None):
            print(node.data)
            node = node.next
            
            

'''firstnode= node("Roshan")
secondNode=node("Anchal")
thirdNode= node("asha")
fourthNode = node("indrajeet")
linked = ll()
linked.insert(firstnode)
linked.insert(secondNode)
linked.insertBeg(fourthNode)
linked.insertat(thirdNode,1)
print(linked.listlength())
linked.printlist()
linked.delete()
print("nodes after deletion ")
linked.printlist()
print("deletion at 2nd position")
linked.deletebw(2)
linked.printlist()
'''