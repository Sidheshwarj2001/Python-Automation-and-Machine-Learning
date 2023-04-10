
class BookStore:
    NoOfBook = 0

    def __init__(self):
        self.Name = input("Enter name of book you want : ")
        self.Author = input("Enter Author of book : ")
        BookStore.NoOfBook +=1

    # def InputFromUser(self):

    #     print("Enter which book you want: ")
    #     self.Name = input()
    #
    #     print("Enter Author of book : ")
    #     self.Author = input()

    def Display(self):
        print("\n name of book :",self.Name)
        print(" Author",self.Author)
        print(" Number of books : ",BookStore.NoOfBook)

def main():

    # print("Enter which book you want: ")
    # name = input()
    #
    # print("Enter Author of book : ")
    # author = input()
    #
    # obj1 = BookStore(name,author)
    # obj1.Display()
    #
    # obj2 = BookStore(name,author)
    # obj2.Display()


    obj1 = BookStore()
    obj1.Display()

    print()

    obj2 = BookStore()
    obj2.Display()

if __name__ == "__main__":
    main()