import pyautogui as pya
import pyperclip
import tkinter as tk
from tkinter import ttk
from PIL import ImageGrab  # Importing Pillow for clipboard image saving
import os
import time
class Window(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Asset Adder")
        self.geometry("300x500")

        self.department_label = tk.Label(self, text="Department")
        self.department_label.pack()
        self.department_name = ttk.Combobox(self, values=["Construction", "Project Management"])
        self.department_name.pack()


        self.asset_type_label = tk.Label(self, text="Cost Code Name")
        self.asset_type_label.pack()

        self.cost_codes = ["1st Rough"]
        self.cost_code_entry = ttk.Combobox(self, values=self.cost_codes)
        self.cost_code_entry.pack()
        self.cost_code_entry.set(self.cost_codes[0])

        self.copy_elipsis = tk.Button(self, text="copy (...)", command=self.save_elipsis)
        self.copy_elipsis.pack()

        self.copy_edit = tk.Button(self, text="copy (edit)", command=self.save_edit)
        self.copy_edit.pack()

        self.copy_department_field = tk.Button(self, text="Copy department field", command=self.save_department_field)
        self.copy_department_field.pack()
    
        self.copy_department_dropdown = tk.Button(self, text="Copy department dropdown", command=self.save_department_dropdown)
        self.copy_department_dropdown.pack()    

        self.copy_cost_code_field = tk.Button(self, text="Copy cost code field", command=self.save_cost_code_field)
        self.copy_cost_code_field.pack()

        self.copy_cost_code_dropdown = tk.Button(self, text="Copy cost code dropdown", command=self.save_cost_code_dropdown)
        self.copy_cost_code_dropdown.pack()

        self.button = tk.Button(self, text="Copy Save Button", command=self.save_save_button_SC)
        self.button.pack()

        self.save_add_assets_button = tk.Button(self, text="Save the department sort", command=self.save_sort)
        self.save_add_assets_button.pack()

        self.start_button = tk.Button(self, text="Start", command=self.start_program)
        self.start_button.pack()

    def save_elipsis(self):
        """Saves the clipboard image as a PNG file."""
        try:
            image = ImageGrab.grabclipboard()  # Get image from clipboard
            if image:  # Check if clipboard contains an image
                filename = "pics/elipsis.png"
                image.save(filename, "PNG")
                print(f"Image saved as {filename}")
            else:
                print("No image found in clipboard.")
        except Exception as e:
            print(f"Error saving image: {e}")

    def save_edit(self):
        """Saves the clipboard image as a PNG file."""
        try:
            image = ImageGrab.grabclipboard()  # Get image from clipboard
            if image:  # Check if clipboard contains an image
                filename = "pics/edit.png"
                image.save(filename, "PNG")
                print(f"Image saved as {filename}")
            else:
                print("No image found in clipboard.")
        except Exception as e:
            print(f"Error saving image: {e}")

    def save_department_field(self):
        """Saves the clipboard image as a PNG file."""
        try:
            image = ImageGrab.grabclipboard()  # Get image from clipboard
            if image:  # Check if clipboard contains an image
                filename = "pics/dpt.png"
                image.save(filename, "PNG")
                print(f"Image saved as {filename}")
            else:
                print("No image found in clipboard.")
        except Exception as e:
            print(f"Error saving image: {e}")

    def save_save_button_SC(self):
        """Saves the clipboard image as a PNG file."""
        try:
            image = ImageGrab.grabclipboard()  # Get image from clipboard
            if image:  # Check if clipboard contains an image
                filename = "pics/save.png"
                image.save(filename, "PNG")
                print(f"Image saved as {filename}")
            else:
                print("No image found in clipboard.")
        except Exception as e:
            print(e)
    
    def save_sort(self):
        """Saves the clipboard image as a PNG file."""
        try:
            image = ImageGrab.grabclipboard()  # Get image from clipboard
            if image:  # Check if clipboard contains an image
                filename = "pics/sort.png"
                image.save(filename, "PNG")
                print(f"Image saved as {filename}")
            else:
                print("No image found in clipboard.")
        except Exception as e:
            print(f"Error saving image: {e}")
    
    def save_cost_code_field(self): 
        """Saves the clipboard image as a PNG file."""
        try:
            image = ImageGrab.grabclipboard()  # Get image from clipboard
            if image:  # Check if clipboard contains an image
                filename = "pics/cost_code.png"
                image.save(filename, "PNG")
                print(f"Image saved as {filename}")
            else:
                print("No image found in clipboard.")
        except Exception as e:
            print(f"Error saving image: {e}")

    def save_department_dropdown(self):
        """Saves the clipboard image as a PNG file."""
        try:
            image = ImageGrab.grabclipboard()  # Get image from clipboard
            if image:  # Check if clipboard contains an image
                filename = "pics/dpt_dropdown.png"
                image.save(filename, "PNG")
                print(f"Image saved as {filename}")
            else:
                print("No image found in clipboard.")
        except Exception as e:
            print(f"Error saving image: {e}")
    
    def save_cost_code_dropdown(self):
        """Saves the clipboard image as a PNG file."""
        try:
            image = ImageGrab.grabclipboard()  # Get image from clipboard
            if image:  # Check if clipboard contains an image
                filename = "pics/cost_code_dropdown.png"
                image.save(filename, "PNG")
                print(f"Image saved as {filename}")
            else:
                print("No image found in clipboard.")
        except Exception as e:
            print(f"Error saving image: {e}")

    def start_program(self):
        while True:
            self.move_and_click_button('pics/sort.png')
            time.sleep(1)
            self.move_and_click_button('pics/elipsis.png')
            time.sleep(.5)
            self.move_and_click_button('pics/edit.png')
            time.sleep(.5)
            self.move_and_click_button('pics/dpt.png')
            time.sleep(.5)
            self.move_and_click_button('pics/dpt_dropdown.png')
            time.sleep(.5)
            self.move_and_click_button('pics/cost_code.png')
            time.sleep(.5)
            self.move_and_click_button('pics/cost_code_dropdown.png')
            time.sleep(.25)
            self.move_and_click_button('pics/save.png')
            time.sleep(.5)


    def move_and_click_button(self, img_path: str):
        attempts = 0
        button_coords = None  # Ensure initialization

        while attempts < 10:  # Limit the number of attempts
            try:
                button_coords = pya.locateOnScreen(img_path, confidence=0.85)
                if button_coords is not None:
                    button_coords = pya.center(button_coords)
                    pya.click(button_coords[0], button_coords[1])
                    return  # Exit function after successful click

            except pya.ImageNotFoundException:
                pass  # Ignore exception and retry

            attempts += 1
            print(f'Attempt #{attempts}: Could not find {img_path}')
            time.sleep(0.8)  # Small delay before retrying

        # Raise an exception when the button is not found after 10 attempts
        raise RuntimeError(f"Failed to find {img_path} after 10 attempts. Program will exit.")


            



        





if __name__ == "__main__":
    Window().mainloop()
