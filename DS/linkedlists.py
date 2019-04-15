#!/usr/bin/env python

class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def AtBegining(self, newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        last = self.headval
        while(last.nextval):
            last = last.nextval
        last.nextval = NewNode

    def RemoveNode(self, RemoveVal):
        HeadVal = self.headval
        if HeadVal is not None:
            if ( HeadVal.dataval == RemoveVal):
                self.headval = HeadVal.nextval
                HeadVal = None
                return
        while HeadVal is not None:
            if HeadVal.dataval == RemoveVal:
                break
            prev = HeadVal
            HeadVal = HeadVal.nextval
        if HeadVal == None:
            return
        prev.nextval = HeadVal.nextval
        HeadVal = None

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list1.headval.nextval = e2
e2.nextval = e3

list1.AtBegining("Sun")
list1.AtEnd("Thu")
list1.RemoveNode("Wed")
list1.listprint()
