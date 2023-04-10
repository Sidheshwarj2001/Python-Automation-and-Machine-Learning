import os

def WriteFile(FileName):
    if(os.path.exists(FileName)):
        os.remove(FileName)
        print("file is Deleted successfully......")
    else:
        print("File is not existing ")

def main():
    print("Enter the file name to Delete with the extension : ")
    Name = input()
    WriteFile(Name)

if __name__ == '__main__':
    main()