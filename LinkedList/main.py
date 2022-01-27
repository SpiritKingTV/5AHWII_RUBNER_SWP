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


if __name__ == "__main__":
    val1 = Node(6)
    val2 = Node(4)
    val3 = Node(7)

    ll = lList()
    ll.attach(val1)
    ll.attach(val2)
    ll.attach(val3)

    print("Print out whole List:")
    print(ll.returnLList())


    print("liste länge:")
    print(ll.returnlenghtLList())
