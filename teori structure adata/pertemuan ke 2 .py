class node():
    def __init__(self, data):
        self.head = data
        self.next = None
        self.data = data
        self.num = 0

    def get_data(self):
        return self.head
    
    #connenting antar node bisa dilakukan dengan cara memberikan referensi class node lain ke variable pada node sebelumnya
    def connecting(self, data):
        self.next= data

    def get_next(self):
        return self.next.head
    
    def get_by_index(self, data):
        if self.num == data:
            return self.head
        elif self.next == None:
            return
        else:
            num = self.num
            self.next.num = num +1 
            return self.next.get_by_index(data)

class linkedList():
    def __init__(self):
        self.head= None
    def insetFirst(self, data):
        neNode= node(data)
        neNode.next = self.head
        self.head = neNode

    def displayData(self):
        display = self.head

        while display != None:
            print(display.head)
            display = display.next
            # print(display.head)
        
    def find():
        pass
data = node(3)
data2 = node(4)
# print(data.get_data())
# data.connecting(data2)
# print(data.get_next())
# print(data.get_by_index(4))

lis1 = linkedList()
lis1.insetFirst(10)
lis1.insetFirst(8)
lis1.insetFirst(7)
lis1.displayData()


angka1 = int(input())
angka2 = int(input())

if 