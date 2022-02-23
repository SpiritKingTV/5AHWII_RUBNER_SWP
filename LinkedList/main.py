class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None



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
            print(self.lenght)

        # val = data
        # top = head

    def find(self, searchValue):
        tempentry = self.top
        while tempentry != None:
            if tempentry.val == searchValue:
                return "found"
            tempentry = tempentry.next
        return "not found"

    def insertBefore(self):
        # mach i nita --> double linked list
        pass

    def insertAfter(self, prevnode, newnode):
        templast = prevnode.next
        newnode.next = templast
        prevnode.next = newnode
        print("worked?")

    def deleteBefore(self):
        # mach i nita --> double linked list
        pass

    def deleteAfter(self, nodenow):
        todelete = nodenow.next
        nodeAfterDeleted = todelete.next
        nodenow.next = nodeAfterDeleted







if __name__ == "__main__":
    val1 = Node(6)
    val2 = Node(4)
    val3 = Node(7)
    #
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
    print("DELETE THIS MOTHERFUCKER: ")
    ll.deleteAfter(val3)
    print(ll.returnLList())
    print("Top:")
    print(ll.top.val)

    #print(ll.find(6))
    #print(ll.find(1))

    #print("liste länge:")
    #print(ll.returnlenghtLList())
