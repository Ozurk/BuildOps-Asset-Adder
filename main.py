import pyautogui
import pyperclip
import csv

with open("assets/assets.csv", mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        asset = row
        for info in row:
            if info != "":
                print(info)
                input("Press enter to copy")
                pyperclip.copy(info)


file.close()        
