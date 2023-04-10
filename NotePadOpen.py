import os
import subprocess
def main():
    # 1st way to open notepad
    # cmd_path = 'notepad'
    # os.system(cmd_path)

    subprocess.Popen("Notepad.exe")


if __name__ == "__main__":
    main()