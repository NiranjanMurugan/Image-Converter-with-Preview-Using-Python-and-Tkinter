import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

class ImageConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Converter with Preview")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.image_path = None
        self.preview_image = None
        self.upload_btn = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_btn.pack(pady=10)
        self.label_path = tk.Label(root, text="No image selected")
        self.label_path.pack()
        self.canvas = tk.Canvas(root, width=300, height=300, bg="white")
        self.canvas.pack(pady=10)
        self.format_var = tk.StringVar(value="jpg")
        self.format_menu = tk.OptionMenu(root, self.format_var, "jpg", "png", "bmp", "gif")
        self.format_menu.pack(pady=5)
        self.convert_btn = tk.Button(root, text="Convert", command=self.convert_image)
        self.convert_btn.pack(pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif")]
        )
        if file_path:
            self.image_path = file_path
            self.label_path.config(text=f"Selected Image: {os.path.basename(file_path)}")
            self.show_preview(file_path)

    def show_preview(self, path):
        img = Image.open(path)
        img.thumbnail((300, 300))
        self.preview_image = ImageTk.PhotoImage(img)
        self.canvas.delete("all")
        self.canvas.create_image(150, 150, image=self.preview_image)

    def convert_image(self):
        if not self.image_path:
            messagebox.showerror("No Image", "Please upload an image first.")
            return
        output_format = self.format_var.get()
        try:
            with Image.open(self.image_path) as img:
                if output_format == "jpg":
                    img = img.convert("RGB")
                save_path = filedialog.asksaveasfilename(
                    defaultextension=f".{output_format}",
                    filetypes=[(f"{output_format.upper()} files", f"*.{output_format}")]
                )
                if save_path:
                    img.save(save_path, output_format.upper())
                    messagebox.showinfo("Success", f"Image saved as {save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to convert image.\n{e}")
root = tk.Tk()
app = ImageConverterApp(root)
root.mainloop()
