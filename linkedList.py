class Node:
    def __init__(self,x):
        self.x=x
        self.next = None
def createNode(n):
    h=Node(1)
    l=h
    for i in range(2,n+1):
        l.next=Node(i)
        l=l.next
    return h

def InsertNode(h,d,p):
    nn=Node(d)
    if p==1:
        nn.next=h
        h=nn
    else:
        l=h
        for i in range(1,p-1):
            l=l.next
        
        nn.next = l.next
        #l.next.next = None
        l.next =nn  

    return h
def printNode(h):
    l=h
    while l.next != None:
        print(l.x)
        l=l.next
    print(l.x)


if __name__ =="__main__":
    #Create Node of value range [1-10]
    h=createNode(10)
    printNode(h)
    #Change the 6th node value to 60
    head=InsertNode(h,11,11)
    printNode(head)

