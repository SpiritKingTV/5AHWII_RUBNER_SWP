


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
        print("added",val)

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
        allvals = ""
        for i in self.list:
            print(i)

    def returnLen(self):
        print(len(self.list))

    def find(self, valToFind):
        for i in self.list:
            if i == valToFind:
                print("Value found!")

    def sortAsc(self):
        for i in self.list:
            j = self.list.index(i)
            while j > 0:
                if self.list[j - 1] > self.list[j]:
                    self.list[j - 1], self.list[j] = self.list[j], self.list[j - 1]
                else:
                    break
                j -= 1

    def sortDesc(self):
        for i in self.list:
            j = self.list.index(i)
            while j > 0:
                if self.list[j - 1] < self.list[j]:
                    self.list[j - 1], self.list[j] = self.list[j], self.list[j - 1]
                else:
                    break
                j -= 1


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
    ll.insertBefore(val3, Node(200))
    print(ll.returnLList())
    print("Delete Before:")
    ll.deleteBefore(val3)
    print(ll.returnLList())
    print("Sort ASC")
    ll.sortAsc()
    print(ll.returnLList())
    print("Sort DESC")
    ll.sortDesc()
    print(ll.returnLList())

    alist = ArrayListImplementation()
    
    print("ArrayList Implementation...")


import kivy
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from kivymd.app import MDApp


class MainScreen(Screen):
    pass


class LinkedListScreen(Screen):
    pass


class ArrayListScreen(Screen):
    ar = ArrayListImplementation()


class MainApp(MDApp):
    def build(self):
        self.sm = ScreenManager(transition=NoTransition())
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"

MainApp().run()
