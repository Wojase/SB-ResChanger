# 🎬 **SB-ResChanger 🎬**

Welcome to the **Video Resolution Converter**! 🎥 This program allows you to easily convert your video files to different resolutions using **FFmpeg**. It supports various resolutions, leverages your GPU for faster encoding, and gives you a colorful and interactive command-line experience. 🚀

---

## 📜 **Features**

- 🖥️ **GPU Acceleration**: Uses NVIDIA or AMD GPUs for faster video conversion.
- 🎯 **Multiple Resolutions**: Choose from 4K, 2K, 1080p, 720p, and 480p.
- ⚡ **Fast Encoding**: Based on your hardware (GPU or CPU), the program selects the best encoder.
- 🎨 **Colorful Command-Line Interface**: The program has a gradient-colored text interface for an exciting user experience.
- 🎶 **Audio**: Output videos are encoded with AAC audio at 192 kbps.
- 💻 **Windows Compatible**: The executable is ready to be run on Windows.

---

## 🏗️ **Installation**

### **Precompiled Windows ****`.exe`**** File** 💻

1. Go to the [releases section](https://github.com/Wojase/SB-ResChanger/releases/tag/SB-ResChanger_1.0) on this repository.
2. Download the latest `.exe` file for your Windows system.
3. Run the `.exe` file and follow the instructions in the command line.

---

## 🚀 **How to Use**

### Step 1: Select a Video 📂

- After launching the program, you'll be prompted to select a video file (.mp4, .avi, .mkv) using a file dialog.

### Step 2: Choose a Resolution 📏

- Choose one of the available resolutions:
  - **4K (3840x2160)** 🌟
  - **2K (2560x1440)** 📱
  - **1080p (1920x1080)** 💻
  - **720p (1280x720)** 📺
  - **480p (854x480)** 📉

### Step 3: Confirm Settings ✅

- The program will show a summary of your selected settings:
  - **Input File** 🎥
  - **Selected Resolution** 📏
  - **Encoder** 🎬 (e.g., `h264_nvenc` for NVIDIA GPUs)
  - **Audio** 🎵 (AAC 192 kbps)

### Step 4: Start Conversion 🔄

- After confirmation, the program will begin converting your video and show logs in the terminal.

### Step 5: Enjoy Your New Video 🎉

- Once the conversion is complete, the new video file will be saved in the same directory as the original with the new resolution applied.

---

## 🔧 **Requirements**

- **Windows** OS (tested on Windows 10)
- **FFmpeg**: The program includes FFmpeg for video encoding. Ensure you have it installed, or use the one packaged with the executable.

---

## 🛠️ **How It Works**

1. **GPU Detection** 🖥️: The program checks if you have an NVIDIA or AMD graphics card. If neither is found, it defaults to CPU encoding.
2. **Resolution Selection** 📏: You can select your preferred video resolution from a list of common options.
3. **Video Conversion** 🔄: Using **FFmpeg**, the program converts your video to the selected resolution with optimized encoding for your hardware.
4. **Colorful CLI** 🌈: The program uses a gradient-colored text interface, making the process more visually engaging.

---

## ⚠️ **Notes**

- 🛑 **GPU Acceleration**: If you don’t have a dedicated GPU, the conversion may take longer as the CPU will be used for encoding.
- ⚙️ **Output Format**: The output is always an `.mp4` file, with the selected resolution and AAC audio.

---

## 📝 **Contributing**

We welcome contributions! If you have suggestions or find bugs, please create an issue or submit a pull request.

---

## 🙋‍♂️ **Support**

For questions or feedback, feel free to reach out by opening an issue in this repository.

---

## 🏆 **Credits**

- **FFmpeg**: The powerful multimedia framework used for encoding videos. [FFmpeg Official](https://ffmpeg.org/)
- **Tkinter**: Used for selecting files in a GUI-like window in the terminal. [Tkinter Docs](https://docs.python.org/3/library/tkinter.html)

---

Enjoy converting your videos with the **Video Resolution Converter**! 🎉📹

---
