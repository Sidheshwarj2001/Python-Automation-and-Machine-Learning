import os
def CreateFile(FileName):
    if(os.path.exists(FileName)):
        print("File is already existing")
        return
    else:
        Folder = open(FileName,"w")

def main():
    print("Enter the file name to create with the extension : ")
    Name = input()

    CreateFile(Name)

if __name__ == '__main__':
    main()