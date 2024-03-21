Dimensi = (input().split())
DimensiTower = input()
DimensiAttack = input()
Defender = 0
Attacker = 0

class Node():
    def __init__(self, data):
        self.prev= None 
        self.data = data
        self.next = None

class doubly_linkedList():
    def __init__(self):
        self.head= None
        self.tail=None

    def insertLast(self, data):
          newNode = Node(data)
          if self.tail is not None:
               self.tail.next = newNode
               newNode.prev = self.tail
          else:
               self.head = newNode
          self.tail = newNode

    def deleteLast(self):
          if self.tail is not None:
               current = self.tail
               if current.prev:
                    current.prev.next= None   
               self.tail = current.prev
    def deleteFirst(self):
         if self.head is not None:
               self.head = self.head.next
    
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()

DimensiTowerList= doubly_linkedList()
for huruf in DimensiTower:
     DimensiTowerList.insertLast(huruf)

DimensiAttackList = doubly_linkedList()
for huruf in DimensiAttack:
     DimensiAttackList.insertLast(huruf)

while True:
    if DimensiTowerList.tail.data == DimensiAttackList.head.data:
        Current = DimensiTowerList.tail
        breaker=0
        while Current.data == DimensiAttackList.head.data:
             breaker+=1
             if Current.prev is None:
                  break
             Current = Current.prev
        for i in range(breaker):
            DimensiTowerList.deleteLast()
             
        DimensiAttackList.deleteFirst()
    else:
         Current = DimensiAttackList.tail
         Data= Current.data
         DimensiTowerList.insertLast(Data)
         DimensiAttackList.deleteFirst()    
    if DimensiTowerList.head == None:
        print("MENANG") 
        break 
    elif DimensiAttackList.head==None:
        print("KALAH") 
        break 

    elif DimensiTowerList.tail ==None:
        print("MENANG")
        break
    elif DimensiAttackList.tail == None:
         print("KALAH")
         break  

        

