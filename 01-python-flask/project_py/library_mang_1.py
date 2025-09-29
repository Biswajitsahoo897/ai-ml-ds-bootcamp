class library:
    book_list=[]
    def __init__(self):
        self.no_books=0
        self.book_list=[]
    def addbooks(self,book):
        # book=input("Enter the book u want to insert :")   
        self.book_list.append(book)
        
        self.no_books=len(self.book_list)
    def showinfo(self):
        print(f"The no of Books in the library is : {self.no_books} books")
        print(f"the list of the books library has right now :  ")
        # {self.book_list} u can print using a for loop only
        for b in self.book_list:
            print(b)         
l1=library()
l1.addbooks("Harry potter 1")
l1.addbooks("Atomic habits")
l1.addbooks("The power of Silence.")
l1.addbooks("How to win ver friends.")
l1.addbooks("The psychology of money.")
l1.addbooks("Do the Epic Shit.")
l1.showinfo()
# in coding unless and until u find that small bug u know then u are nothing 