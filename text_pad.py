import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import os
from datetime import datetime

class TextPad:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Pad - Simple Text Editor")
        self.root.geometry("800x600")
        self.root.minsize(400, 300)
        
        # Current file path
        self.current_file = None
        self.is_modified = False
        
        # Configure style
        self.setup_style()
        
        # Create GUI
        self.create_menu()
        self.create_toolbar()
        self.create_text_area()
        self.create_status_bar()
        
        # Bind events
        self.bind_events()
        
        # Set focus to text area
        self.text_area.focus_set()
    
    def setup_style(self):
        """Configure the application style"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure colors
        self.root.configure(bg='#f0f0f0')
        
    def create_menu(self):
        """Create the menu bar"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
        file_menu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_command(label="Save As", command=self.save_as_file, accelerator="Ctrl+Shift+S")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit_app, accelerator="Ctrl+Q")
        
        # Edit menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Cut", command=lambda: self.text_area.event_generate("<<Cut>>"), accelerator="Ctrl+X")
        edit_menu.add_command(label="Copy", command=lambda: self.text_area.event_generate("<<Copy>>"), accelerator="Ctrl+C")
        edit_menu.add_command(label="Paste", command=lambda: self.text_area.event_generate("<<Paste>>"), accelerator="Ctrl+V")
        edit_menu.add_separator()
        edit_menu.add_command(label="Select All", command=lambda: self.text_area.tag_add(tk.SEL, "1.0", tk.END), accelerator="Ctrl+A")
        
        # View menu
        view_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="View", menu=view_menu)
        view_menu.add_command(label="Zoom In", command=self.zoom_in, accelerator="Ctrl++")
        view_menu.add_command(label="Zoom Out", command=self.zoom_out, accelerator="Ctrl+-")
        view_menu.add_command(label="Reset Zoom", command=self.reset_zoom, accelerator="Ctrl+0")
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)
    
    def create_toolbar(self):
        """Create the toolbar"""
        toolbar = ttk.Frame(self.root)
        toolbar.pack(fill=tk.X, padx=5, pady=2)
        
        # New button
        new_btn = ttk.Button(toolbar, text="New", command=self.new_file, width=8)
        new_btn.pack(side=tk.LEFT, padx=2)
        
        # Open button
        open_btn = ttk.Button(toolbar, text="Open", command=self.open_file, width=8)
        open_btn.pack(side=tk.LEFT, padx=2)
        
        # Save button
        save_btn = ttk.Button(toolbar, text="Save", command=self.save_file, width=8)
        save_btn.pack(side=tk.LEFT, padx=2)
        
        # Separator
        ttk.Separator(toolbar, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y, padx=5)
        
        # Font size label and combobox
        ttk.Label(toolbar, text="Font Size:").pack(side=tk.LEFT, padx=2)
        self.font_size_var = tk.StringVar(value="12")
        font_size_combo = ttk.Combobox(toolbar, textvariable=self.font_size_var, 
                                      values=["8", "10", "12", "14", "16", "18", "20", "24"], 
                                      width=5, state="readonly")
        font_size_combo.pack(side=tk.LEFT, padx=2)
        font_size_combo.bind("<<ComboboxSelected>>", self.change_font_size)
        
        # Word wrap toggle
        self.word_wrap_var = tk.BooleanVar(value=True)
        word_wrap_check = ttk.Checkbutton(toolbar, text="Word Wrap", 
                                         variable=self.word_wrap_var, 
                                         command=self.toggle_word_wrap)
        word_wrap_check.pack(side=tk.LEFT, padx=10)
    
    def create_text_area(self):
        """Create the main text area"""
        # Create frame for text area
        text_frame = ttk.Frame(self.root)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Create text widget with scrollbars
        self.text_area = scrolledtext.ScrolledText(
            text_frame,
            wrap=tk.WORD,
            font=("Consolas", 12),
            bg="white",
            fg="black",
            insertbackground="black",
            selectbackground="#0078d4",
            selectforeground="white",
            undo=True,
            maxundo=100
        )
        self.text_area.pack(fill=tk.BOTH, expand=True)
        
        # Configure tags for syntax highlighting (basic)
        self.text_area.tag_configure("bold", font=("Consolas", 12, "bold"))
        self.text_area.tag_configure("italic", font=("Consolas", 12, "italic"))
    
    def create_status_bar(self):
        """Create the status bar"""
        self.status_bar = ttk.Frame(self.root)
        self.status_bar.pack(fill=tk.X, side=tk.BOTTOM)
        
        # Line and column info
        self.line_col_label = ttk.Label(self.status_bar, text="Line: 1, Column: 1")
        self.line_col_label.pack(side=tk.LEFT, padx=5)
        
        # File info
        self.file_label = ttk.Label(self.status_bar, text="New Document")
        self.file_label.pack(side=tk.RIGHT, padx=5)
        
        # Modified indicator
        self.modified_label = ttk.Label(self.status_bar, text="", foreground="red")
        self.modified_label.pack(side=tk.RIGHT, padx=5)
    
    def bind_events(self):
        """Bind keyboard and mouse events"""
        # Text change event
        self.text_area.bind("<<Modified>>", self.on_text_modified)
        
        # Cursor movement
        self.text_area.bind("<KeyRelease>", self.update_cursor_position)
        self.text_area.bind("<ButtonRelease-1>", self.update_cursor_position)
        
        # Keyboard shortcuts
        self.root.bind("<Control-n>", lambda e: self.new_file())
        self.root.bind("<Control-o>", lambda e: self.open_file())
        self.root.bind("<Control-s>", lambda e: self.save_file())
        self.root.bind("<Control-Shift-S>", lambda e: self.save_as_file())
        self.root.bind("<Control-q>", lambda e: self.quit_app())
        self.root.bind("<Control-plus>", lambda e: self.zoom_in())
        self.root.bind("<Control-minus>", lambda e: self.zoom_out())
        self.root.bind("<Control-0>", lambda e: self.reset_zoom())
        
        # Window close event
        self.root.protocol("WM_DELETE_WINDOW", self.quit_app)
    
    def on_text_modified(self, event=None):
        """Handle text modification"""
        if self.text_area.edit_modified():
            self.is_modified = True
            self.modified_label.config(text="*")
            self.text_area.edit_modified(False)
    
    def update_cursor_position(self, event=None):
        """Update cursor position in status bar"""
        try:
            cursor_pos = self.text_area.index(tk.INSERT)
            line, col = cursor_pos.split('.')
            self.line_col_label.config(text=f"Line: {line}, Column: {int(col) + 1}")
        except:
            pass
    
    def new_file(self):
        """Create a new file"""
        if self.is_modified:
            if not self.prompt_save():
                return
        
        self.text_area.delete(1.0, tk.END)
        self.current_file = None
        self.is_modified = False
        self.file_label.config(text="New Document")
        self.modified_label.config(text="")
        self.root.title("Text Pad - New Document")
    
    def open_file(self):
        """Open an existing file"""
        if self.is_modified:
            if not self.prompt_save():
                return
        
        file_path = filedialog.askopenfilename(
            title="Open File",
            filetypes=[
                ("Text files", "*.txt"),
                ("Python files", "*.py"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(1.0, content)
                
                self.current_file = file_path
                self.is_modified = False
                self.file_label.config(text=os.path.basename(file_path))
                self.modified_label.config(text="")
                self.root.title(f"Text Pad - {os.path.basename(file_path)}")
                
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file: {str(e)}")
    
    def save_file(self):
        """Save the current file"""
        if self.current_file:
            self.save_to_file(self.current_file)
        else:
            self.save_as_file()
    
    def save_as_file(self):
        """Save file with a new name"""
        file_path = filedialog.asksaveasfilename(
            title="Save As",
            defaultextension=".txt",
            filetypes=[
                ("Text files", "*.txt"),
                ("Python files", "*.py"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            self.save_to_file(file_path)
    
    def save_to_file(self, file_path):
        """Save content to a specific file"""
        try:
            content = self.text_area.get(1.0, tk.END)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            
            self.current_file = file_path
            self.is_modified = False
            self.file_label.config(text=os.path.basename(file_path))
            self.modified_label.config(text="")
            self.root.title(f"Text Pad - {os.path.basename(file_path)}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file: {str(e)}")
    
    def prompt_save(self):
        """Prompt user to save changes"""
        response = messagebox.askyesnocancel(
            "Save Changes",
            "Do you want to save your changes?"
        )
        
        if response is True:
            return self.save_file()
        elif response is False:
            return True
        else:
            return False
    
    def zoom_in(self):
        """Increase font size"""
        current_size = int(self.font_size_var.get())
        if current_size < 48:
            self.font_size_var.set(str(current_size + 2))
            self.change_font_size()
    
    def zoom_out(self):
        """Decrease font size"""
        current_size = int(self.font_size_var.get())
        if current_size > 6:
            self.font_size_var.set(str(current_size - 2))
            self.change_font_size()
    
    def reset_zoom(self):
        """Reset font size to default"""
        self.font_size_var.set("12")
        self.change_font_size()
    
    def change_font_size(self, event=None):
        """Change the font size"""
        try:
            size = int(self.font_size_var.get())
            self.text_area.configure(font=("Consolas", size))
        except ValueError:
            pass
    
    def toggle_word_wrap(self):
        """Toggle word wrap"""
        if self.word_wrap_var.get():
            self.text_area.configure(wrap=tk.WORD)
        else:
            self.text_area.configure(wrap=tk.NONE)
    
    def show_about(self):
        """Show about dialog"""
        about_text = """Text Pad - Simple Text Editor

A lightweight text editor built with Python and tkinter.

Features:
• Create, open, and save text files
• Basic text editing with undo/redo
• Font size adjustment
• Word wrap toggle
• Line and column counter
• Keyboard shortcuts

Version: 1.0
Built with Python and tkinter"""
        
        messagebox.showinfo("About Text Pad", about_text)
    
    def quit_app(self):
        """Quit the application"""
        if self.is_modified:
            if not self.prompt_save():
                return
        
        self.root.quit()

def main():
    """Main function to run the application"""
    root = tk.Tk()
    app = TextPad(root)
    
    # Add some welcome text
    welcome_text = """Welcome to Text Pad!

This is a simple text editor where you can type, edit, and save your documents.

Features:
• File operations (New, Open, Save, Save As)
• Text editing with undo/redo
• Font size adjustment
• Word wrap toggle
• Line and column counter
• Keyboard shortcuts

Start typing or use the File menu to open an existing document.

Happy typing! 🎉
"""
    
    app.text_area.insert(1.0, welcome_text)
    app.text_area.edit_modified(False)
    
    # Center the window
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    root.mainloop()

if __name__ == "__main__":
    main()
