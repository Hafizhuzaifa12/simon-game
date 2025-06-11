class Node :
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        new_node = Node(data)
        if not self.head:
          self.head = new_node
          print(f"this isthe beginig{data}")
          return  # ✅ `return` کو `if` بلاک کے اندر رکھیں
         
      
        last =self.head
        while last.next:
            last =last.next
        last.next =new_node
        print(f"this is end of {data}")
      
       
    def display(self):
        if not self.head:
            print("list is empty")
            return
        current = self.head
        while current:
            print(current.data ,end=" ->")
            current = current.next
       
        print("none")
show = LinkedList()
# show.display()
show.insert_at_end(1)
show.insert_at_end(2)
show.insert_at_end(4)
show.insert_at_end(5)
show.display()
  











