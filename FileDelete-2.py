import os

def WriteFile(FileName):
    if(os.path.exists(FileName)):
        size = os.path.getsize(FileName)

        if(size==0):
            os.remove(FileName)
            print("file is Deleted successfully......")

        else:
            print("Are you sure to delete the file ? Y/N")
            option = input()

            if(option == 'y' or option == 'Y'):
                os.remove(FileName)

            else:
                print("File is not deleted process stoped...")

    else:
        print("There is no such file is found")

def main():
    print("Enter the file name to Delete with the extension : ")
    Name = input()
    WriteFile(Name)

if __name__ == '__main__':
    main()