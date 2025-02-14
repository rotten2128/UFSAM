import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import io
import base64

# Base64-encoded image string
logo_base64 = "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"

# Function to set custom logo using base64 string
def set_logo(window, logo_base64):
    try:
        # Decode the base64 string
        logo_data = base64.b64decode(logo_base64)
        
        # Convert to image using PIL
        img = Image.open(io.BytesIO(logo_data))
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
        key=lambda x: int(x.replace(base_name_with_ext + ".split", "")),
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
root.title("UFSAM")
root.geometry("350x250")
root.resizable(False, False)
root.config(bg="black")

# Define dark theme styles
style = ttk.Style()
style.configure("TFrame", background="black")
style.configure("TLabel", background="black", foreground="white")
style.configure("TButton", background="gray", foreground="black")
style.configure("TEntry", fieldbackground="black", foreground="black", insertbackground="black")

set_logo(root, logo_base64)  # Set logo using base64 string

frame = ttk.Frame(root, padding=10)
frame.pack(expand=True)

ttk.Label(frame, text="Unity File Split And Merge", font=("Arial", 12, "bold")).pack(pady=10)

ttk.Label(frame, text="Enter into the text box the extension to put the split files into: ").pack()
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
