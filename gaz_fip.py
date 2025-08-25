
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
from PIL import Image
import io

def compress_to_target_size(img_path, target_size):
    img = Image.open(img_path).convert("RGB")
    quality = 95
    while quality >= 5:
        buffer = io.BytesIO()
        img.save(buffer, format='JPEG', quality=quality, subsampling="4:2:0", optimize=True)
        data = buffer.getvalue()
        if len(data) <= target_size:
            break
        quality -= 5
    if len(data) < target_size:
        data += b'\x00' * (target_size - len(data))
    elif len(data) > target_size:
        data = data[:target_size]
    return data

def patch_bin(bin_path, img1_path, img2_path, offset1, offset2, size1, size2, output_path):
    bin_data = bytearray(Path(bin_path).read_bytes())
    jpeg1 = compress_to_target_size(img1_path, size1)
    jpeg2 = compress_to_target_size(img2_path, size2)
    bin_data[offset1:offset1 + size1] = jpeg1
    bin_data[offset2:offset2 + size2] = jpeg2
    Path(output_path).write_bytes(bin_data)

def run_patching():
    try:
        bin_path = filedialog.askopenfilename(title="Select Original BIN File", filetypes=[("BIN Files", "*.bin")])
        img1_path = filedialog.askopenfilename(title="Select First JPEG (4D000)", filetypes=[("JPEG Files", "*.jpg")])
        img2_path = filedialog.askopenfilename(title="Select Second JPEG (7F800)", filetypes=[("JPEG Files", "*.jpg")])
        save_path = filedialog.asksaveasfilename(defaultextension=".bin", title="Save Patched BIN As")

        patch_bin(bin_path, img1_path, img2_path, 0x4D000, 0x7F800, 2284, 40597, save_path)
        messagebox.showinfo("Success", f"✅ Patched BIN saved to:\n{save_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def main():
    root = tk.Tk()
    root.title("Firmware Image Patcher")
    root.geometry("400x200")

    lbl = tk.Label(root, text="Firmware Image Patcher", font=("Arial", 16))
    lbl.pack(pady=20)

    btn = tk.Button(root, text="Start Patching", command=run_patching, font=("Arial", 12), bg="#4CAF50", fg="white")
    btn.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
