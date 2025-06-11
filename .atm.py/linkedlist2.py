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
            print(f"this is first string{data}")
            return
        last = self.head
        while last.next:
               last = last.next
        last.next = new_node
        print(f"this the second data {data}")
        
    def display(self):
        if not self.head:
            print("khali h ")
            return
        current = self.head
        while current:
            print(current.data, end="-->") 
            # print("none")/
            current = current.next
        print("none")
        return
show =LinkedList()
show.insert_at_end(6)        
show.insert_at_end(7)        
show.insert_at_end(8)        
show.insert_at_end(9) 
show.display()       


         


            

    

        
    


            
