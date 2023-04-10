import hashlib
import os

def DirectoryWatecher(path):
    walker = os.walk(path)
    UniqueFile = dict()
    for Folder , SubFolder , Filenames in walker:
        for files in Filenames:
            filepath = os.path.join(Folder,files)
            file_hash = hashlib.md5(open(filepath , "rb").read()).hexdigest()

            if file_hash in UniqueFile:
                os.remove(filepath)
                print("this file has been deleted"+filepath)
            else:
                UniqueFile[file_hash] = path

def main():
    DirectoryWatecher("ABC")


if __name__ == '__main__':
    main()