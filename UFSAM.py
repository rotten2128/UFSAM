import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk

# Function to set custom logo
def set_logo(window, logo_path):
    try:
        img = Image.open(logo_path)
        icon = ImageTk.PhotoImage(img)
        window.iconphoto(False, icon)
    except Exception as e:
        print(f"Error loading logo: {e}")

def merge_files():
    start_file = filedialog.askopenfilename(title="Select First Split File")
    if not start_file:
        return
    
    directory = os.path.dirname(start_file)
    base_name_with_ext = os.path.basename(start_file).rsplit(".split", 1)[0]
    file_extension = file_extension_entry.get().strip()
    
    # Find all matching split files
    split_files = sorted(
        [f for f in os.listdir(directory) if f.startswith(base_name_with_ext + ".split")],
        key=lambda x: int(x.replace(base_name_with_ext + ".split", ""))
    )
    
    output_file = os.path.join(directory, base_name_with_ext)
    
    with open(output_file, "wb") as outfile:
        for split in split_files:
            file_path = os.path.join(directory, split)
            with open(file_path, "rb") as infile:
                outfile.write(infile.read())
    
    messagebox.showinfo("Success", f"Merged into {output_file}")

def split_file():
    file_path = filedialog.askopenfilename(title="Select File to Split")
    if not file_path:
        return
    
    chunk_size = 1024 * 1024  # 1024 KB
    directory = os.path.dirname(file_path)
    base_name_with_ext = os.path.basename(file_path)
    
    with open(file_path, "rb") as infile:
        i = 0
        while chunk := infile.read(chunk_size):
            split_file_path = os.path.join(directory, f"{base_name_with_ext}.split{i}")
            with open(split_file_path, "wb") as outfile:
                outfile.write(chunk)
            i += 1
    
    messagebox.showinfo("Success", f"Split into {i} parts in {directory}")

# Tkinter GUI Setup
root = tk.Tk()
root.title("Unity Asset Split & Merge")
root.geometry("350x250")

set_logo(root, "assets/UFSAM-ICON-FEATHER.jpg")

frame = ttk.Frame(root, padding=10)
frame.pack(expand=True)

ttk.Label(frame, text="Unity Asset Split & Merge", font=("Arial", 12, "bold")).pack(pady=10)

ttk.Label(frame, text="The file type you want to get from the merger:").pack()
file_extension_entry = ttk.Entry(frame)
file_extension_entry.insert(0, "")
file_extension_entry.pack(pady=5)

merge_btn = ttk.Button(frame, text="Merge Split Files", command=merge_files)
merge_btn.pack(pady=5)

split_btn = ttk.Button(frame, text="Split File", command=split_file)
split_btn.pack(pady=5)

exit_btn = ttk.Button(frame, text="Exit", command=root.quit)
exit_btn.pack(pady=5)

root.mainloop()