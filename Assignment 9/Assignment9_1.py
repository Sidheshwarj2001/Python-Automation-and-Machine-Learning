import os

def ExistingFile(FileName):
    if(os.path.exists(FileName)):
        print("File name is exist...")

    else:
        print("File Doesn't exist...")

def main():
    print("Enter file name :")
    name = input()

    ExistingFile(name)

if __name__ == "__main__":
    main()