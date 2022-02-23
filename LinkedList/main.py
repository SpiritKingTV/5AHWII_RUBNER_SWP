class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None


class lList:
    def __init__(self):
        self.lenght = 0
        self.top = None

    def attach(self, newNode):
        if self.top:
            lastNode = self.top
            while lastNode != None:
                if lastNode.next == None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode
            newNode.prev = lastNode
        else:
            self.top = newNode

    def returnLList(self):
        if self.top:
            print(self.top.val)
            tempvar = self.top
            while tempvar.next != None:
                tempvar = tempvar.next
                print(tempvar.val)

    def returnlenghtLList(self):
        self.lenght = 0
        if self.top is not None:
            self.lenght += 1
            tempvar = self.top
            while tempvar.next is not None:
                self.lenght += 1
                tempvar = tempvar.next
            return self.lenght

    def find(self, searchValue):
        tempentry = self.top
        while tempentry != None:
            if tempentry.val == searchValue:
                return "found"
            tempentry = tempentry.next
        return "not found"

    def insertBefore(self, curr, newnode):
        currprev = curr.prev
        currprev.next = newnode
        curr.prev = newnode
        newnode.prev = currprev
        newnode.next = curr


    def insertAfter(self, prevnode, newnode):
        templast = prevnode.next
        newnode.next = templast
        prevnode.next = newnode
        print("worked?")

    def deleteBefore(self,curr):
        if curr.prev is None:
            print("Es gibt kein Element davor")
            return
        last = curr.prev
        if last.prev is None:
            print("Man müsste Top neu setzen")
            return
        lastoflast = last.prev
        curr.prev = lastoflast
        lastoflast.next = curr


    def deleteAfter(self, nodenow):
        todelete = nodenow.next
        nodeAfterDeleted = todelete.next
        nodenow.next = nodeAfterDeleted


if __name__ == "__main__":
    val1 = Node(6)
    val2 = Node(4)
    val3 = Node(7)
    # 500
    val4 = Node(5)
    val5 = Node(10)

    ll = lList()
    ll.attach(val1)
    ll.attach(val2)
    ll.attach(val3)
    ll.attach(val4)
    ll.attach(val5)

    print(ll.returnLList())
    ll.insertAfter(val3, Node(500))

    print("Print out whole List:")
    print(ll.returnLList())
    print("DELETE: ")
    ll.deleteAfter(val3)
    print(ll.returnLList())
    print("Top:")
    print(ll.top.val)
    print("Insert Before:")
    ll.insertBefore(val3,Node(200))
    print(ll.returnLList())
    print("Delete Before:")
    ll.deleteBefore(val3)
    print(ll.returnLList())

    #print(ll.find(6))
    #print(ll.find(1))

    #print("liste länge:")
    #print(ll.returnlenghtLList())
