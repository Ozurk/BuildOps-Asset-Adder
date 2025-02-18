import pyautogui as pya
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Use PIL for image processing
from PIL import ImageGrab  # Importing Pillow for clipboard image saving
import time
import os

class Window(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Taskify")
        self.geometry("800x800")
        self.image_thumbnails = {}  # Stores PhotoImage references
        self.image_labels = {}      # Stores Label widgets


        # Configure grid layout
        self.columnconfigure(0, weight=3)  # Main area
        self.columnconfigure(1, weight=1)  # Parameter frame

        # Frame for the main buttons and checkboxes
        self.button_frame = tk.Frame(self)
        self.button_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Frame for parameters
        self.param_frame = tk.Frame(self, relief=tk.RAISED, borderwidth=2)
        self.param_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Dictionary to store checkbutton variables
        self.image_options = {}
        self.image_thumbnails = {}  # Store references to avoid garbage collection

        # Add buttons, checkboxes, and thumbnails
        self.add_buttons_with_checkboxes_and_thumbnails()

        # Add parameter settings inside the parameter frame
        self.add_parameters()

    def add_buttons_with_checkboxes_and_thumbnails(self):
        """Creates buttons, checkboxes, and thumbnails."""
        button_texts = [
            ("Copy Image 1", "pics/img1.png"),
            ("Copy Image 2", "pics/img2.png"),
            ("Copy Image 3", "pics/img3.png"),
            ("Copy Image 4", "pics/img4.png"),
            ("Copy Image 5", "pics/img5.png"),
            ("Copy Image 6", "pics/img6.png"),
            ("Copy Image 7", "pics/img7.png"),
            ("Copy Image 8", "pics/img8.png")
        ]

        for i, (text, img) in enumerate(button_texts):
            # Button
            btn = tk.Button(self.button_frame, text=text, command=lambda img=img: self.save_image(img))
            btn.grid(row=i, column=0, padx=10, pady=5, sticky="ew")

            # Checkbox
            var = tk.BooleanVar(value=True)  # Default: checked (included)
            chk = tk.Checkbutton(self.button_frame, variable=var)
            chk.grid(row=i, column=1, padx=5, pady=5)

            # Store checkbox state
            self.image_options[img] = var

            # Load and display the thumbnail
            thumbnail_label = self.load_thumbnail(img)
            if thumbnail_label:
                thumbnail_label.grid(row=i, column=2, padx=5, pady=5, sticky="w")  # Position to the right

    def load_thumbnail(self, img_path):
        """Loads and resizes an image to create a thumbnail."""
        if not os.path.exists(img_path):
            print(f" File not found: {img_path}")
            return tk.Label(self.button_frame, text="[No Image]")  # Return placeholder label

        try:
            # Open, resize, and create PhotoImage
            img = Image.open(img_path)
            img = img.resize((50, 50), Image.Resampling.LANCZOS)
            img_tk = ImageTk.PhotoImage(img)

            # Store reference persistently (prevents garbage collection)
            self.image_thumbnails[img_path] = img_tk

            label = tk.Label(self.button_frame, image=img_tk)
            return label

        except Exception as e:
            print(f"⚠️ Error loading thumbnail for {img_path}: {e}")
            return tk.Label(self.button_frame, text="[Error Loading]")  # Fallback label
        

    def update_thumbnail(self, img_path):
        """Updates the thumbnail in the UI after saving an image."""
        # Remove the old label if it exists
        if img_path in self.image_labels:
            self.image_labels[img_path].destroy()  # Destroy old label
        
        # Create and store the new thumbnail
        new_label = self.load_thumbnail(img_path)
        new_label.grid(row=self.get_image_row(img_path), column=2, padx=5, pady=5, sticky="w")
        
        # Store the new label reference
        self.image_labels[img_path] = new_label


    def get_image_row(self, img_path):
        """Returns the row number for an image in the UI."""
        img_list = ["pics/img1.png", "pics/img2.png", "pics/img3.png", "pics/img4.png", 
                    "pics/img5.png", "pics/img6.png", "pics/img7.png", "pics/img8.png"]
        return img_list.index(img_path) if img_path in img_list else 0  # Default to row 0 if not found
        
    def add_parameters(self):
        """Creates and places parameter inputs inside the parameter frame."""
        tk.Label(self.param_frame, text="Settings", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=5)

        # Iterations
        tk.Label(self.param_frame, text="Iterations:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.iterations = tk.Entry(self.param_frame)
        self.iterations.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Delay
        tk.Label(self.param_frame, text="Delay (seconds):").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.delay = tk.Entry(self.param_frame)
        self.delay.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        tk.Label(self.param_frame, text="Determine the percent accuracy needed to identify the images [0 - 1]\n1 = Exact Match").grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        self.confidence = tk.Entry(self.param_frame)
        self.confidence.grid(row=4, column=0, columnspan=2, padx=5, pady=5,)

        # Run Button
        self.run_button = tk.Button(self.param_frame, text="Run Program", background="grey", command=self.run_program)
        self.run_button.grid(row=5, column=0, columnspan=2, padx=5, pady=20, sticky="ew")


    def save_image(self, img_path: str):
        """Saves the clipboard image and updates the thumbnail."""
        try:
            image = ImageGrab.grabclipboard()
            if image:
                # Ensure the directory exists
                os.makedirs(os.path.dirname(img_path), exist_ok=True)
                
                # Save image
                image.save(img_path, "PNG")
                print(f" Image saved: {img_path}")

                # Immediately refresh the UI to show the new thumbnail
                self.update_thumbnail(img_path)

            else:
                print(" No image found in clipboard.")

        except Exception as e:
            print(f"Error saving image: {e}")


    def run_program(self):
        """Runs the program based on user-defined parameters."""
        try:
            iterations = int(self.iterations.get())  # Convert to int
            delay = float(self.delay.get())  # Convert to float
        except ValueError:
            print("Please enter valid numbers for iterations and delay.")
            return

        selected_images = [img for img, var in self.image_options.items() if var.get()]

        if not selected_images:
            print("No images selected for processing.")
            return

        for _ in range(iterations):
            for img in selected_images:
                self.move_and_click_button(img)
                time.sleep(delay)

    def move_and_click_button(self, img_path: str):
        """Attempts to locate and click a button image on the screen."""
        attempts = 0
        button_coords = None  # Ensure initialization

        while attempts < 10:  # Limit the number of attempts
            try:
                button_coords = pya.locateOnScreen(img_path, confidence=float(self.confidence.get()))
                if button_coords is not None:
                    button_coords = pya.center(button_coords)
                    pya.click(button_coords[0], button_coords[1])
                    return  # Exit function after successful click

            except pya.ImageNotFoundException:
                pass  # Ignore exception and retry

            attempts += 1
            print(f'Attempt #{attempts}: Could not find {img_path}')
            time.sleep(float(self.delay.get()))  # Small delay before retrying

        # Raise an exception when the button is not found after 10 attempts
        raise RuntimeError(f"Failed to find {img_path} after 10 attempts. Program will exit.")

if __name__ == "__main__":
    Window().mainloop()
