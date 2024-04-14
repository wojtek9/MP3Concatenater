from pydub import AudioSegment
from tkinter import filedialog
import os

class Converter:
    selected_files = []
    downloaded_files = []
    _id = 1

    def select_files(cls):
        file_paths = filedialog.askopenfilenames()
        cls.selected_files.extend(file_paths)

    def choose_save_dir(cls):
        save_path = filedialog.askdirectory()
        if save_path:
            cls.merge_mp3(save_path)

    def merge_mp3(cls, save_path):
        first_file_path = os.path.realpath(os.path.join(save_path, cls.selected_files[0]))
        new_mp3 = AudioSegment.from_mp3(first_file_path)
        
        for file_path in cls.selected_files[1:]:
            file = AudioSegment.from_mp3(os.path.join(save_path, file_path))
            new_mp3 += file

        save_file_name = f"merged_sound_{cls._id}.mp3"
        merged_file_path = os.path.realpath(os.path.join(save_path, save_file_name))
        if os.path.exists(merged_file_path):
            msg = f"file with name: {save_file_name} already exists"
            return print(msg)
        else:
            new_mp3.export(merged_file_path, format="mp3")
            cls.downloaded_files.append(save_file_name)
            cls._id +=1
            cls.selected_files.clear()

