from abc import ABC, abstractmethod
class LibraryItem(ABC):

    def __init__(self, title):
        self.title = title

    @abstractmethod
    def display_info(self):
        pass
class Book(LibraryItem):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author
    def display_info(self):
        print(f"Book Title : {self.title}")
        print(f"Author     : {self.author}")
class Magazine(LibraryItem):

    def __init__(self, title, issue_number):
        super().__init__(title)
        self.issue_number = issue_number

    def display_info(self):
        print(f"Magazine Title : {self.title}")
        print(f"Issue Number   : {self.issue_number}")
class DVD(LibraryItem):

    def __init__(self, title, duration):
        super().__init__(title)
        self.duration = duration

    def display_info(self):
        print(f"DVD Title : {self.title}")
        print(f"Duration  : {self.duration} mins")

        
class Member:
    def __init__(self, name):
        self.name = name
        self.__borrowed_items = []
    def borrow_item(self, item):
        self.__borrowed_items.append(item)
    def return_item(self, title):
        for item in self.__borrowed_items:
            if item.title == title:
                self.__borrowed_items.remove(item)
                return item
        return None
    def show_borrowed_items(self):
        if not self.__borrowed_items:
            print("No Borrowed Items")
            return
        print(f"\nBorrowed Items by {self.name}")
        for item in self.__borrowed_items:
            print("-", item.title)
class Library:

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item.title} added successfully")

    def remove_item(self, title):

        for item in self.items:

            if item.title == title:
                self.items.remove(item)
                print("Item Removed")
                return

        print("Item Not Found")

    def search_item(self, title):

        for item in self.items:

            if item.title.lower() == title.lower():
                print("\nItem Found")
                item.display_info()
                return item

        print("Item Not Found")
        return None

    def display_all_items(self):

        if not self.items:
            print("Library Empty")
            return

        print("\n===== Library Items =====")

        for item in self.items:
            item.display_info()
            print("-" * 25)

    def borrow_item(self, title):

        for item in self.items:

            if item.title.lower() == title.lower():
                self.items.remove(item)
                return item

        return None

    def return_item(self, item):
        self.items.append(item)


library = Library()

book1 = Book("Python Basics", "Tharun")
book2 = Book("FastAPI Guide", "John")

magazine1 = Magazine("Tech Monthly", 101)

dvd1 = DVD("Python Tutorial", 120)

library.add_item(book1)
library.add_item(book2)
library.add_item(magazine1)
library.add_item(dvd1)

member = Member("Rahul")

while True:

    print("\n===== Library Management System =====")
    print("1. Display All Items")
    print("2. Search Item")
    print("3. Borrow Item")
    print("4. Return Item")
    print("5. Show Borrowed Items")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        library.display_all_items()

    elif choice == "2":

        title = input("Enter Title: ")
        library.search_item(title)

    elif choice == "3":

        title = input("Enter Title to Borrow: ")

        item = library.borrow_item(title)

        if item:
            member.borrow_item(item)
            print("Item Borrowed Successfully")
        else:
            print("Item Not Available")

    elif choice == "4":

        title = input("Enter Title to Return: ")

        item = member.return_item(title)

        if item:
            library.return_item(item)
            print("Item Returned Successfully")
        else:
            print("You Have Not Borrowed This Item")

    elif choice == "5":
        member.show_borrowed_items()

    elif choice == "6":
        print("Thank You")
        break

    else:
        print("Invalid Choice")

   




        