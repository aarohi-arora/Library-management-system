#1.Library Management System:

# Create classes for Book, Member, and Library.
# Implement methods to add new books, register members, issue books, return books, and display all books and members.
# Use file handling to save and load library data.
# import pickle
# class library:
#     def __init__(self):
#         self.book=0
#         self.name=""
#     def getlibrary(self):
#         self.book=int(input("No of book"))
#         self.name=input("Name of library")
#     def putlibrary(self):
#         print(self.book)
#         print(self.name)

# class book(library):
#     def __init__(self):
#         super().__init__()
#         self.pages=0
#         self.author=""
#         self.bookid=0
#     def getbook(self):
#         self.pages=int(input("no of pages"))
#         self.author=input("name of author")
#         self.bookid=int(input("Enter book id"))
#     def putbook(self):
#         print(self.pages)
#         print(self.author)
#         print(self.bookid)
#     def searchbook(self,bid):
#         return self.bookid==bid

# class member(library):
#     def __init__(self):
#         super().__init__()
#         self.age=0
#         self.gender=""
#     def getmember(self):
#         self.age=int(input("member age"))
#         self.gender=input("member age")
#     def putmember(self):
#         print(self.age)
#         print(self.gender)
    

# def save_records(records,filename="myfile.txt"):
#     with open(filename,"wb")as f:
#         for record in records:
#             pickle.dump(record,f,pickle.HIGHEST_PROTOCOL)  # write to file in binary form
# def load_records(filename="myfile.txt"):
#     records=[]              
#     try:
#         with open(filename,"rb")as f:   #open the file and make f as file object         
#             while True:   # infiite loop
#                 try:
#                     records.append(pickle.load(f))  #read the record and add to list
#                 except EOFError:
#                     break # break the infinite loop  
#     except FileNotFoundError:
#         print("No records found.")
#     return records
# if __name__=="__main__":
#     while True:
#         print("----Books and details----")
#         print("Enter your choice")
#         print("1.Add your records")
#         print("2.View records")
#         print("3.Search record")
#         print("4.Delete record")
#         print("5.Modify record")
#         print("6.exit")
#         ch=int(input())
#         b1=book()

#         if ch==1:
#             records=load_records()  # read from file and bring records to list
#             n=int(input("no of books?"))
#             for _ in range(n):
#                 b1.getbook()
#                 b1.getlibrary()
#                 records.append(b1)  #Append to last of list
#             save_records(records)  #send records to save them
#         elif ch==2:
#             records=load_records()
#             for b1 in records:
#                 b1.putbook()
#                 b1.putlibrary()
#         elif ch == 3:
#             bid = int(input("Enter Book ID: "))
#             records = load_records()
#             print("Total Records =", len(records))
#             found = False
#             for b1 in records:
#                 if b1.searchbook(bid):
#                     print("Found")
#                     b1.putbook()
#                     b1.putlibrary()
#                     found = True
#                     break
#                 if not found:
#                     print("Not Found")                            
#         elif ch==4:
#             bid = int(input("Enter book ID to delete: "))
#             records = load_records()
#             new_records = [b1 for b1 in records if not b1.searchbook(bid)]
#             new_records=[]
#             for b1 in records:
#                 if not b1.searchbook(bid):
#                     new_records.append(b1)
#             if len(records) != len(new_records):
#                 print("Record deleted successfully.")
#                 save_records(new_records)
#             else:
#                 print("Record not found.")

#         elif ch==5:
#             bid=int(input("Enter book id to modify"))
#             records=load_records()
#             modified=False
#             for b1 in records:
#                 if b1.searchbook(bid):
#                     print("Found\n. Enter new details.")
#                     b1.getbook()
#                     b1.getlibrary()
#                     modified = True
#                     break
#             if modified:
#                 save_records(records)
#                 print("Record updated successfully.")
#             else:
#                 print("Record not found.")
