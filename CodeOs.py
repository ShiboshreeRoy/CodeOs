import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox, Menu
import os
import subprocess
from fpdf import FPDF

class CodeOS:
    def __init__(self, root):
        self.root = root
        self.root.title("Code OS - Advanced Text Editor")
        self.root.geometry("1000x700")
        
        # Set application icon
        try:
            #self.root.iconbitmap("CodeOs.ioc")
            self.root.iconbitmap(os.path.join(os.path.dirname(__file__), "icon", "CodeOs.png"))

        except:
            print("Icon file not found. Please place 'CodeOs.ioc' in the same directory.")
        
        self.filename = None
        
        self.create_menu()
        self.create_editor()
        self.create_terminal()
    
    def create_menu(self):
        menubar = Menu(self.root)
        
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as)
        file_menu.add_command(label="Export as PDF", command=self.export_as_pdf)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        
        edit_menu = Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Undo", command=lambda: self.editor.edit_undo())
        edit_menu.add_command(label="Redo", command=lambda: self.editor.edit_redo())
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=lambda: self.editor.event_generate("<<Cut>>"))
        edit_menu.add_command(label="Copy", command=lambda: self.editor.event_generate("<<Copy>>"))
        edit_menu.add_command(label="Paste", command=lambda: self.editor.event_generate("<<Paste>>"))
        edit_menu.add_separator()
        edit_menu.add_command(label="Find", command=self.find_text)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        
        view_menu = Menu(menubar, tearoff=0)
        view_menu.add_command(label="Toggle Terminal", command=self.toggle_terminal)
        menubar.add_cascade(label="View", menu=view_menu)
        
        run_menu = Menu(menubar, tearoff=0)
        run_menu.add_command(label="Run Python", command=self.run_python)
        run_menu.add_command(label="Run HTML/CSS/JS", command=self.run_web)
        menubar.add_cascade(label="Run", menu=run_menu)
        
        terminal_menu = Menu(menubar, tearoff=0)
        terminal_menu.add_command(label="Open Terminal", command=self.open_terminal)
        menubar.add_cascade(label="Terminal", menu=terminal_menu)
        
        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)

        
        
        self.root.config(menu=menubar)
    
    def create_editor(self):
        self.editor = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, undo=True)
        self.editor.pack(expand=True, fill='both')
    
    def create_terminal(self):
        self.terminal = tk.Text(self.root, height=8, bg="black", fg="white")
        self.terminal.pack(expand=False, fill='x')
    
    def new_file(self):
        self.filename = None
        self.editor.delete(1.0, tk.END)
    
    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.filename = file_path
            with open(file_path, "r") as file:
                self.editor.delete(1.0, tk.END)
                self.editor.insert(tk.END, file.read())
    
    def save_file(self):
        if self.filename:
            with open(self.filename, "w") as file:
                file.write(self.editor.get(1.0, tk.END))
        else:
            self.save_as()
    
    def save_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            self.filename = file_path
            self.save_file()
    
    def export_as_pdf(self):
        if self.filename:
            pdf = FPDF()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            text = self.editor.get(1.0, tk.END)
            pdf.multi_cell(190, 10, text)
            pdf_filename = self.filename.replace(".txt", ".pdf")
            pdf.output(pdf_filename)
            messagebox.showinfo("Export PDF", f"File saved as {pdf_filename}")
        else:
            messagebox.showerror("Error", "Please save the file before exporting as PDF")
    
    def find_text(self):
        search_query = filedialog.askstring("Find", "Enter text to search:")
        if search_query:
            start = "1.0"
            while True:
                start = self.editor.search(search_query, start, stopindex=tk.END)
                if not start:
                    break
                end = f"{start}+{len(search_query)}c"
                self.editor.tag_add("highlight", start, end)
                self.editor.tag_config("highlight", background="yellow")
                start = end
    
    def run_python(self):
        if self.filename and self.filename.endswith(".py"):
            command = f"python {self.filename}"
            output = subprocess.run(command, shell=True, capture_output=True, text=True)
            self.terminal.delete(1.0, tk.END)
            self.terminal.insert(tk.END, output.stdout + output.stderr)
        else:
            messagebox.showerror("Error", "Please save the file as a .py script before running")
    
    def run_web(self):
        if self.filename and self.filename.endswith((".html", ".css", ".js")):
            os.startfile(self.filename)
        else:
            messagebox.showerror("Error", "Please save the file as .html, .css, or .js")
    
    def toggle_terminal(self):
        if self.terminal.winfo_ismapped():
            self.terminal.pack_forget()
        else:
            self.terminal.pack(expand=False, fill='x')
    
    def open_terminal(self):
        os.system("start cmd")
    
    def show_about(self):
        messagebox.showinfo("About", "Code OS - Advanced Text Editor\nVersion 1.0\nDev Shiboshree Roy")
    
    

if __name__ == "__main__":
    root = tk.Tk()
    app = CodeOS(root)
    root.mainloop()
