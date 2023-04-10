import os



def main():
    current_folder = os.getcwd()

    my_folder_path = os.path.join(current_folder, 'my_folder')

    def create_required_folder(dirname):
        distination_folder = os.path.join(my_folder_path, dirname)

        if not os.path.exists(distination_folder):
            os.makedirs(distination_folder)
        return distination_folder

    for folder ,subfolder , filenames in os.walk(my_folder_path):
        for files in filenames:

            if os.path.splitext(files)[-1]==".txt":
                dirname = "text_only"
                distination_folder = create_required_folder(dirname)
                os.rename(os.path.join(folder , files),f"{distination_folder}/{files}")

            if os.path.splitext(files)[-1]==".py":
                dirname = "python_only"
                distination_folder = create_required_folder(dirname)
                os.rename(os.path.join(folder , files),f"{distination_folder}/{files}")

            if os.path.splitext(files)[-1]==".jpg":
                dirname = "img_only"
                distination_folder = create_required_folder(dirname)
                os.rename(os.path.join(folder , files),f"{distination_folder}/{files}")

if __name__ == '__main__':
    main()