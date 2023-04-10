import os

def WriteFile(FileName):
    if(os.path.exists(FileName)):
        print("Enter the data that you want to write to the file :")
        Data = input()

        fd = open(FileName , 'a')

        return fd.write(Data)

    else:
        print("File is not existing ")

def main():
    print("Enter the file name to Write with the extension : ")
    Name = input()
    WriteFile(Name)

if __name__ == '__main__':
    main()