import random


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
        # double linked
        newnode.prev = prevnode
        tempnew = newnode.next
        tempnew.prev = newnode

        print("worked?")

    def deleteBefore(self, curr):
        if curr.prev is None:
            print("Es gibt kein Element davor")
            return
        last = curr.prev
        if last.prev is None:
            self.top = curr
            curr.prev = None;
            return
        lastoflast = last.prev
        curr.prev = lastoflast
        lastoflast.next = curr

    def deleteAfter(self, nodenow):
        todelete = nodenow.next
        nodeAfterDeleted = todelete.next
        nodenow.next = nodeAfterDeleted
        # double linked
        nodeAfterDeleted.prev = nodenow;

    def swap(self, firstNode, secondNode):
        firstNode.val, secondNode.val = secondNode.val, firstNode.val

    def sortAsc(self):
        start = self.top
        nextNode = None
        while start is not None:
            nextNode = start.next
            while nextNode is not None and nextNode.prev is not None and nextNode.val < nextNode.prev.val:
                self.swap(nextNode, nextNode.prev)
                nextNode = nextNode.prev
            start = start.next

    def sortDesc(self):
        start = self.top
        nextNode = None
        while start is not None:
            nextNode = start.next
            while nextNode is not None and nextNode.prev is not None and nextNode.val > nextNode.prev.val:
                self.swap(nextNode, nextNode.prev)
                nextNode = nextNode.prev
            start = start.next





class ArrayListImplementation:
    def __init__(self):
        self.list = []

    def attach(self, val):
        self.list.append(val)

    def deleteAfter(self, index):
        if index >= 0 and index < len(self.list):
            if len(self.list) > index + 1:
                self.list.pop(index + 1)

    def deleteBefore(self, index):
        if 0 <= index < len(self.list):
            if index - 1 > -1:
                self.list.pop(index - 1)

    def insertAfter(self, index, newVal):
        if 0 <= index < len(self.list):
            self.list.insert(index + 1, newVal)

    def insertBefore(self, index, newVal):
        if 0 <= index < len(self.list):
            if index - 1 >= 0:
                self.list.insert(index, newVal)

    # additional Methods

    def deleteVal(self, index):
        if 0 <= index < len(self.list):
            self.list.pop(index)

    def InsertAt(self, index, newVal):
        if 0 <= index < len(self.list):
            self.list.insert(index, newVal)

    def returnAll(self):
        for i in self.list:
            print(i)

    def returnLen(self):
        return len(self.list)

    def find(self, valToFind):
        for i in self.list:
            if i == valToFind:
                print("Value found!")

    def sortAsc(self):
        for i in range(1, self.returnLen()):
            key = self.list[i]
            j = i - 1
            while j >= 0 and key < self.list[j]:
                self.list[j + 1] = self.list[j]
                j -= 1
            self.list[j + 1] = key

    def sortDesc(self):
        for i in range(1, self.returnLen()):
            key = self.list[i]
            j = i - 1
            while j >= 0 and key > self.list[j]:
                self.list[j + 1] = self.list[j]
                j -= 1
            self.list[j + 1] = key

def generateVals(ll,arr,count):
    import random
    for i in range(count):
        x = random.randint(0,1000)
        arr.attach(x)
        ll.attach(Node(x))
def timemeasureLLAsc(ll):
    import time
    startTime = time.time();
    ll.sortAsc()
    endtime = time.time();
    return endtime - startTime
def timemeasureLLDesc(ll):
    import time
    startTime = time.time();
    ll.sortDesc()
    endtime = time.time();
    return endtime - startTime

def timemeasureArrAsc(ar):
    import time
    startTime = time.time();
    ar.sortAsc()
    endtime = time.time();
    return endtime - startTime
def timemeasureArrDesc(ar):
    import time
    startTime = time.time();
    ar.sortDesc()
    endtime = time.time();
    return endtime - startTime


if __name__ == "__main__":
    ll = lList()
    ar = ArrayListImplementation()
    arr = ArrayListImplementation()
    arr.attach(1)
    arr.attach(7)
    arr.attach(4)
    arr.attach(10)

    generateVals(ll,ar,1000)
    #print(ar.returnAll())
    timell=timemeasureLLAsc(ll)
    timear=timemeasureArrAsc(ar)
    #print("sorted:")
    #print(ar.returnAll())
    print("Results:")
    print("Linked List: ", timell)
    print("Array-List: ", timear)
    if(timell> timear):
        print("Linked List brauch Länger (", timell - timear, "Sekunden )")
    else:
        print("Array-List brauch Länger (", timear - timell, "Sekunden )")
    # print(ll.find(6))
    # print(ll.find(1))

    # print("liste länge:")
    # print(ll.returnlenghtLList())
