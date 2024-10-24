import tkinter as tk
from tkinter import filedialog
import csv

def import_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            documents = sorted(reader, key=lambda x: x['date'])
            
            result_text.delete(1.0, tk.END)
            for doc in documents:
                result_text.insert(tk.END, f"Title: {doc['title']}, Date: {doc['date']}\n")

root = tk.Tk()
root.title("Document Organizer")

import_button = tk.Button(root, text="Import File", command=import_file)
import_button.pack()

result_text = tk.Text(root, height=10, width=50)
result_text.pack()

root.mainloop()
