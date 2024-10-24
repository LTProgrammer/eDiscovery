import tkinter as tk  # Import the tkinter library for creating GUI applications
from tkinter import filedialog, messagebox  
# Import filedialog to allow users to select files, and messagebox for dialogs
import csv  
# Import the csv library to handle reading CSV files

# Function to import and sort the file
def import_file():
    # Open a file dialog to allow the user to select a text file
    file_path = filedialog.askopenfilename()
    if file_path:
        # Open the selected file in read mode
        with open(file_path, mode='r') as file:
            # Read the file using csv.DictReader, assuming 'title' and 'date' columns
            reader = csv.DictReader(file)
            # Sort the documents by the 'date' column
            documents = sorted(reader, key=lambda x: x['date'])
            
            # Clear any previous content in the text area
            result_text.delete(1.0, tk.END)
            # Loop through the sorted documents and display each in the text area
            for doc in documents:
                result_text.insert(tk.END, f"Title: {doc['title']}, Date: {doc['date']}\n")

# Create the main application window
root = tk.Tk()
root.title("Document Organizer")  # Set the title of the window

# Show a dialog when the application starts
messagebox.showinfo("Hello eDiscovery Pro", "Hello eDiscovery Pro")

# Create a button that calls the 'import_file' function when clicked
import_button = tk.Button(root, text="Import File", command=import_file)
import_button.pack()  # Place the button on the window

# Create a text area where the sorted documents will be displayed
result_text = tk.Text(root, height=10, width=50)
result_text.pack()  # Place the text area on the window

# Start the tkinter main loop (this runs the application)
root.mainloop()
