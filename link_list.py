class Sll:
     def __init__(self):
          self.head=None
          self.size=0

     class Node:
          def __init__(self,d):
               self.data=d
               self.next=None 
          
     def insertAtBeg(self,d):
          n=self.Node(d)
          n.next=self.head
          self.head=n

     def removeAtBeg(self):
          if self.head==None:
               print("ll is underflow")
          temp=self.head
          self.head=temp.next
          return temp.data
          
     def insertAtLast(self,d):
          n=self.Node(d)
          if self.head==None:
               self.head=n 
          else:
               temp=self.head
               while temp.next!=None:
                    temp=temp.next
               temp.next=n  

     def removeAtLast(self):
          if self.head==None:
               print("ll is underflow")
          elif self.head.next==None:
               temp=self.head 
               self.head=None
               return temp.data            
          else:   
               temp=self.head
               while temp.next!=None:
                    temp=temp.next
               y=temp.next
               temp.next=None
               return y.data            

                   
      
     def traversal(self):
          if self.head==None:
               print("ll is underflow") 
          else:
               temp=self.head
               while temp.next!=None:  
                    print(temp.data , end=" ")
                    temp=temp.next      
 

insert = Sll()
insert.insertAtBeg(10)
insert.insertAtBeg(20)
insert.insertAtBeg(30)
insert.traversal() 





         