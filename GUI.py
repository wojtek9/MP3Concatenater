import tkinter as tk
from tkinter import ttk
from Converter import Converter

class MP3ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("450x350")
        self.root.resizable(False, False)
        self.root.title("MP3 Concatenater")

        self.converter = Converter()
        self.downloaded_files = []

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True)

        self.converter_tab = ttk.Frame(self.notebook)
        self.overview_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.converter_tab, text='Converter')
        self.notebook.add(self.overview_tab, text='Overview')

        #Converter tab
        self.c_headline = ttk.Label(self.converter_tab, text="MP3 Converter", font=('Helvetica', 18))
        self.c_headline.pack(pady=10)

        self.c_select_files = ttk.Button(self.converter_tab, text="Select files", command=self.on_select_files_clicked)
        self.c_select_files.pack(pady=5)

        self.c_list_frame = ttk.Frame(self.converter_tab)
        self.c_list_frame.pack(pady=5)

        self.c_file_list = tk.Listbox(self.c_list_frame, width=50)
        self.c_file_list.pack(side='left', padx=5)

        c_scrollbar = ttk.Scrollbar(self.c_list_frame, orient='vertical', command=self.c_file_list.yview)
        c_scrollbar.pack(side='right', fill='y')
        self.c_file_list.config(yscrollcommand=c_scrollbar.set)

        self.c_download_button = ttk.Button(self.converter_tab, text="Download", command=self.on_download_clicked)
        self.c_download_button.pack(pady=5)

        #Overview tab
        self.o_headline = ttk.Label(self.overview_tab, text="Overview of converted files", font=('Helvetica', 18))
        self.o_headline.pack(pady=10)

        self.o_list_frame = ttk.Frame(self.overview_tab)
        self.o_list_frame.pack(pady=5)

        self.o_file_list = tk.Listbox(self.o_list_frame, width=50)
        self.o_file_list.pack(side='left', padx=5)

        o_scrollbar = ttk.Scrollbar(self.o_list_frame, orient='vertical', command=self.o_file_list.yview)
        o_scrollbar.pack(side='right', fill='y')
        self.o_file_list.config(yscrollcommand=o_scrollbar.set)

    def file_exists_in_c_listbox(self, filename):
        items = self.c_file_list.get(0, 'end')
    
        for item in items:
            if filename == item:
                return True
    
        return False
    
    def file_exists_in_o_listbox(self, filename):
        items = self.o_file_list.get(0, 'end')
    
        for item in items:
            if filename == item:
                return True
    
        return False

    def c_add_file_entry(self, filename):
        self.c_file_list.insert('end', filename)

    def o_add_file_entry(self, filename):
        self.o_file_list.insert('end', filename)

    def on_select_files_clicked(self):
        print(self.converter.selected_files)
        self.converter.select_files()
        for file in self.converter.selected_files:
            if not self.file_exists_in_c_listbox(file):
                self.c_add_file_entry(file)

    def on_download_clicked(self):
        self.converter.choose_save_dir()
        self.handle_file_download()

    def handle_file_download(self):
        #...find a way to check if the file was converted and downloaded correctly from Converter class
        success = True
        if success:
            self.c_file_list.delete(0, 'end')
            for file in self.converter.downloaded_files:
                if not self.file_exists_in_o_listbox(file):
                    self.o_add_file_entry(file)

if __name__ == "__main__":
    root = tk.Tk()
    app = MP3ConverterApp(root)
    root.mainloop()