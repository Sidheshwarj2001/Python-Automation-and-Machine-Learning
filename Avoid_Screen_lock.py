import time
import pyautogui

def main():
    while True:
        time.sleep(4)
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')

        pyautogui.press('volumedown')
        pyautogui.press('volumedown')
        pyautogui.press('volumedown')

if __name__ == '__main__':
    main()