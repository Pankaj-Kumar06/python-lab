# library management system
class LibraryItem:
    def __init__(self,title,item_id):
        self.title = title
        self.item_id = item_id
        self.issued = False
    def issue(self):
        if self.issued == False:
            self.issued = True
            print("the item is issued:",self.title)
        else:
            print("this item has been already issued:",self.title)

    def return_item(self):
        if self.issued == True:
            self.issued = False
            print("the issued item has been returned",self.title)
        else:
            print("the item has not been issued",self.title)

    def display(self):
        print("Title:",self.title)
        print("ID",self.item_id)


class Book(LibraryItem):
    def display(self):
        super().display()
        print("book:",self.title)

class Magzine(LibraryItem):
    def display(self):
        super().display()
        print("Magzine:",self.title)

class Journal(LibraryItem):
    def display(self):
        super().display()
        print("Journal",self.title)

b = Book("python basic",101)
b.issue()
m = Magzine("sports jagat",102)
m.return_item()
j = Journal("alzeera",104)
b.return_item()
j.issue()
l = LibraryItem("sex magazine",103)
l.display()
