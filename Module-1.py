import os

def main():
    current_folder = os.getcwd()

    my_folder_path = os.path.join(current_folder, 'my_folder')

    distination_folder_txt = os.path.join(my_folder_path , 'text_only')
    distination_folder_jpg = os.path.join(my_folder_path, 'jpg_only')
    distination_folder_py = os.path.join(my_folder_path, 'py_only')

    if not os.path.exists(distination_folder_txt):
        os.makedirs(distination_folder_txt)

    if not os.path.exists(distination_folder_jpg):
        os.makedirs(distination_folder_jpg)


    if not os.path.exists(distination_folder_py):
        os.makedirs(distination_folder_py)

    for folder ,subfolder , filenames in os.walk(my_folder_path):
        for files in filenames:

            if os.path.splitext(files)[-1]==".txt":
                os.rename(os.path.join(folder , files),f"{distination_folder_txt}/{files}")



            if os.path.splitext(files)[-1]==".py":
                os.rename(os.path.join(folder , files),f"{distination_folder_py}/{files}")



            if os.path.splitext(files)[-1]==".jpg":
                os.rename(os.path.join(folder , files),f"{distination_folder_jpg}/{files}")


if __name__ == '__main__':
    main()