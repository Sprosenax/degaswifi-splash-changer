# degaswifi-splash-changer
this changes the splash screen of Samsung Galaxy Tab 4 7.0 (degaswifi)

# 📦 Firmware Image Patcher GUI

A simple cross-platform tool to patch custom splash images into `PARAM.bin` or similar firmware files.  
Supports **Windows & Linux**, with a drag-and-drop GUI for easier use.

---

## ✨ Features
- ✅ Extract and patch splash screen images at known offsets (`0x4D000`, `0x7F800`, etc.)
- ✅ Automatically resizes & converts input images to the correct format
- ✅ GUI built with **Tkinter** (no terminal required)

---

## 🚀 Getting Started

### Option 1: Run from Python
Requirements:
- Python **3.11+**
- Pillow (`pip install pillow`)

Clone this repo and run:
```bash
python firmware_image_patcher_gui.py
```

## 📂 Usage
1. Select the original `PARAM.bin`
2. Pick your replacement splash images (`.jpg`, `.png`)
3. The tool will:
   - Convert and resize images to the correct resolution
   - Patch them into the binary at the right offsets
   - Save the new `PARAM_patched.bin`

Flash the patched binary to your device and enjoy your new splash screen 🎉

---

## 🖼️ Image Requirements
- Correct resolution **800×1280** 
- Supported formats: `.jpg`, `.png`
- The tool will pad/convert automatically if needed

---

## ⚠️ Disclaimer
- This tool modifies **firmware binaries**.  
- Use at your own risk — flashing invalid files may brick your device.  
- Always keep a backup of your original `PARAM.bin`.

---

## 📜 License
MIT License – feel free to fork, modify, and share.
