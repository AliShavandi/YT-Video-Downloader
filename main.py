import customtkinter as tk
import tkinter
from pytube import YouTube
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def download():
    try:
        yt_link = link.get()
        print(yt_link)
        yt = YouTube(yt_link, on_progress_callback=download_progress)
        video = yt.streams.get_highest_resolution()
        video.download(output_path="/Users/alishavandi/Downloads")
        downloaded.configure(text="Video Downloaded", text_color="green")
    except Exception as e:
        downloaded.configure(text="Downlod Failed\nTry Again.", text_color="red")

def download_progress(stream, chunk, bytes_remaining):
    file_size = stream.filesize
    bytes_downloaded = file_size - bytes_remaining
    percent = bytes_downloaded / file_size * 100
    per = str(int(percent))
    progress_percent.configure(text=f"{per}%")
    progress_percent.update()
    progress_bar.set(float(percent) / 100)
    progress.configure(text=f"{round(bytes_downloaded / 1000000, 2)} MB / {round(file_size / 1000000, 2)} MB")

window = tk.CTk()
window.title("YouTube Video Downloader")
window.geometry("800x500")

tk.set_appearance_mode("dark")
tk.set_default_color_theme("green")

title = tk.CTkLabel(window, text="Youtube Video Downloader", font=("Arial", 25))
title.pack(padx=10, pady=50)
header = tk.CTkLabel(window, text="Enter youtube video link:", font=("Arial", 18))
header.pack(padx=10, pady=10)

url = tkinter.StringVar()
link = tk.CTkEntry(window, width=600, textvariable=url)
link.pack()



download_button = tk.CTkButton(window, text="DOWNLOAD", command=download)
download_button.pack(padx=20, pady=20)

progress_percent = tk.CTkLabel(window, text="", font=("Arial", 18))
progress_percent.pack(padx=10, pady=10)
progress = tk.CTkLabel(window, text="", font=("Arial", 18))
progress.pack(padx=10, pady=10)

progress_bar = tk.CTkProgressBar(window, width=600)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)

downloaded = tk.CTkLabel(window, text="", font=("Arial", 16))
downloaded.pack(padx=20, pady=20)



window.mainloop()