import os
import subprocess
import platform
import shutil
import sys
import tkinter as tk
from tkinter import filedialog
from tqdm import tqdm


# Dostępne rozdzielczości
RESOLUTIONS = {
    "1": ("4K (3840x2160)", "3840x2160"),
    "2": ("2K (2560x1440)", "2560x1440"),
    "3": ("1080p (1920x1080)", "1920x1080"),
    "4": ("720p (1280x720)", "1280x720"),
    "5": ("480p (854x480)", "854x480"),
}

# Funkcja generująca efekt gradientu dla tekstu
def gradient_text(text):
    gradient = [
        "\033[38;5;214m", "\033[38;5;220m", "\033[38;5;215m", "\033[38;5;216m", 
        "\033[38;5;223m", "\033[38;5;214m", "\033[38;5;216m", "\033[38;5;217m", 
        "\033[38;5;222m", "\033[38;5;230m", "\033[38;5;208m", "\033[38;5;220m"
    ]
    colored_text = ""
    color_index = 0
    for char in text:
        colored_text += gradient[color_index % len(gradient)] + char
        color_index += 1
    return colored_text + "\033[0m"  # Resetowanie koloru

# Sprawdzenie czy jest karta NVIDIA lub AMD
def check_gpu():
    if platform.system() == "Windows":
        try:
            nvidia_check = subprocess.run(["nvidia-smi"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if "NVIDIA" in nvidia_check.stdout:
                return "NVIDIA"
        except FileNotFoundError:
            pass

        try:
            amd_check = subprocess.run(["wmic", "path", "win32_VideoController", "get", "name"], stdout=subprocess.PIPE, text=True)
            if "AMD" in amd_check.stdout:
                return "AMD"
        except FileNotFoundError:
            pass

    return "CPU"

# Funkcja konwersji wideo
def convert_video(file_path, resolution, gpu_type):
    output_file = os.path.splitext(file_path)[0] + f"_{resolution}.mp4"

    # Wybór kodeka na podstawie posiadanego sprzętu
    if gpu_type == "NVIDIA":
        codec = "h264_nvenc"
    elif gpu_type == "AMD":
        codec = "h264_amf"
    else:
        codec = "libx264"

    if getattr(sys, 'frozen', False):
        ffmpeg_path = os.path.join(sys._MEIPASS, "ffmpeg.exe")
    else:
        ffmpeg_path = "ffmpeg.exe"  # Wersja developerska

    # Uruchomienie FFmpeg
    command = [
        ffmpeg_path,  # Używa lokalnego ffmpeg.exe
        "-i", file_path,
        "-vf", f"scale={resolution}",
        "-c:v", codec,
        "-preset", "fast",
        "-crf", "23",
        "-c:a", "aac",
        "-b:a", "192k",
        output_file
    ]

    print("\n🔄 **Rozpoczynanie konwersji...**\n")
    print(" ".join(command))
    print("\n📡 **Logi FFmpeg:**\n")

    # Uruchomienie FFmpeg i wyświetlanie logów
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
    for line in process.stdout:
        print(line, end="")

    process.wait()

    if process.returncode == 0:
        print(f"\n✅ **Konwersja zakończona! Plik zapisano jako:** {output_file}")
    else:
        print("\n❌ **Wystąpił błąd podczas konwersji!**")

# Funkcja wyboru pliku za pomocą Tkinter
def choose_file():
    root = tk.Tk()
    root.withdraw()  # Ukrywa główne okno
    file_path = filedialog.askopenfilename(title="Wybierz plik wideo", filetypes=[("Pliki wideo", "*.mp4;*.avi;*.mkv")])
    return file_path

# Funkcja menu
def main_menu():
    while True:
        # Wyświetlanie gradientu na menu głównym
        print(gradient_text("""
███████╗██████╗       ██████╗ ███████╗███████╗ ██████╗██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███████╗██████╗ 
██╔════╝██╔══██╗      ██╔══██╗██╔════╝██╔════╝██╔════╝██║  ██║██╔══██╗████╗  ██║██╔════╝ ██╔════╝██╔══██╗
███████╗██████╔╝█████╗██████╔╝█████╗  ███████╗██║     ███████║███████║██╔██╗ ██║██║  ███╗█████╗  ██████╔╝
╚════██║██╔══██╗╚════╝██╔══██╗██╔══╝  ╚════██║██║     ██╔══██║██╔══██║██║╚██╗██║██║   ██║██╔══╝  ██╔══██╗
███████║██████╔╝      ██║  ██║███████╗███████║╚██████╗██║  ██║██║  ██║██║ ╚████║╚██████╔╝███████╗██║  ██║
╚══════╝╚═════╝       ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
"""))

        print(gradient_text("🎬 **Video Resolution Converter** 🎬"))
        print("1️⃣ Change Video Resolution")
        print("2️⃣ Exit")

        choice = input("\n➡️ Wybierz opcję: ")

        if choice == "1":
            # Użycie Tkinter do wybrania pliku
            file_path = choose_file()
            if not file_path:
                print("\n❌ **Nie wybrano pliku!** Spróbuj ponownie.")
                continue

            print("\n📏 **Dostępne rozdzielczości:**")
            for key, (label, _) in RESOLUTIONS.items():
                print(f"{key}. {label}")

            resolution_choice = input("\n➡️ Wybierz nową rozdzielczość (1-5): ").strip()
            if resolution_choice not in RESOLUTIONS:
                print("\n❌ **Nieprawidłowy wybór!** Spróbuj ponownie.")
                continue

            _, resolution = RESOLUTIONS[resolution_choice]

            # Sprawdzenie GPU
            gpu_type = check_gpu()
            print(f"\n🖥 **Wykryta karta graficzna:** {gpu_type}")
            if gpu_type == "CPU":
                print("⚠️ **Nie wykryto dedykowanej karty graficznej. Konwersja może być wolniejsza.**")

            # Potwierdzenie ustawień
            print("\n🔍 **Podsumowanie ustawień:**")
            print(f"📁 Plik wejściowy: {file_path}")
            print(f"📏 Nowa rozdzielczość: {resolution}")
            print(f"🎥 Kodek: {'h264_nvenc' if gpu_type == 'NVIDIA' else 'h264_amf' if gpu_type == 'AMD' else 'libx264'}")
            print(f"🎵 Dźwięk: AAC 192 kbps")

            confirm = input("\n✅ Czy rozpocząć konwersję? (tak/nie): ").strip().lower()
            if confirm == "tak":
                convert_video(file_path, resolution, gpu_type)
            else:
                print("\n⏪ **Anulowano konwersję.**")

        elif choice == "2":
            print("\n👋 **Dziękujemy za skorzystanie z programu!**")
            break
        else:
            print("\n❌ **Nieprawidłowa opcja!** Spróbuj ponownie.")

# Uruchomienie programu
if __name__ == "__main__":
    main_menu()
