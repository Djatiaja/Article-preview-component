#membuat doubly linked list 

class Node():
    def __init__(self, data):
        self.prev= None 
        self.data = data
        self.next = None

class doubly_linkedList():
    def __init__(self):
        self.head= None
        self.index = 0
        self.tail=None
        
    def inserFirst(self, data):
          newNode = Node(data)
          newNode.next = self.head
          if self.head is not None:
               self.head.prev = newNode
          self.head= newNode
          if self.tail is None:
               self.tail = newNode

    def insertLast(self, data):
          newNode = Node(data)
          if self.tail is not None:
               self.tail.next = newNode
               newNode.prev = self.tail
          else:
               self.head = newNode
          self.tail = newNode

    def insert_by_index(self, data, index):
          current = self.head 

          while current is not None:
               if self.index == index:
                    break
               current = current.next 
               self.index +=1 
          
          newNode = Node(data)

          current.prev.next = newNode
          newNode.prev = current.prev
          newNode.next = current
          current.prev = newNode   
          self.resetIndex()


    def display_list(self):
         current = self.head
         print('[' , end='')
         while current is not None:
            if current.next is not None:
               print(current.data, end=',')
            else:
               print(current.data, end='')
            current = current.next
         print("]")

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()

    def delete(self, data):
         current = self.head
         while current is not None:
              if data == current.data :
                    if current.prev is not None:
                         if current.next is not None:
                              current.next.prev = current.prev 
                         else:
                              self.tail= current.prev                   
                         current.prev.next =current.next
                    else:
                         self.head = current.next
                    break
              current = current.next

    def deleteFirst(self):
         if self.head is not None:
               self.head = self.head.next
    
    def deleteLast(self):
          if self.tail is not None:
               current = self.tail
               current.prev.next= None   
               self.tail = current.prev

    def delete_by_index(self, data):
         current = self.head
         while current:
              if data == self.index :
                    if current.prev is not None:
                        current.next.prev = current.prev
                        current.prev.next = current.next
                        break
                    else:
                         self.head = current.next
                         break     
              current = current.next
              self.index +=1
         self.resetIndex()

    def find(self, data):
          Current = self.head 
          Notfound = True
          while Current is not None:
               if Current.data == data:
                   Notfound = False
                   break
               Current = Current.next
          if Notfound:
               return 'Data not found in the list'
          else:
               return f"{Current.data} found"
              
    
    def find_index(self, data):
          Current = self.head 
          Notfound = True
          while Current is not None:
               if Current.data == data:
                   Notfound = False

               Current = Current.next
               self.index +=1

          if Notfound:
               return 'Data not found in the list'
          else:
               index= self.resetIndex()
               return f"{Current.data} found at {index}"
          
    def resetIndex(self):
         Index = self.index
         self.index= 0
         return Index
    

lis1 = doubly_linkedList()
lis1.inserFirst(5)
lis1.inserFirst(1)
lis1.inserFirst(3)
lis1.inserFirst(2)
lis1.display()
print(lis1.find(3))
lis1.display()
