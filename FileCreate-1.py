
def CreateFile(FileName):
    Folder = open(FileName,"w") #create the file not their
    # "W" - if file is creted as you can give same name of the
    # file then old file is deleted and new create as same name

def main():
    print("Enter the file name to create with the extension : ")
    Name = input()

    CreateFile(Name)

if __name__ == '__main__':
    main()