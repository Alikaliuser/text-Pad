# Text Pad - Simple Text Editor

A lightweight, feature-rich text editor built with Python and tkinter. Perfect for quick note-taking, code editing, and document creation.

![Text Pad Screenshot](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

## 🚀 Features

### ✨ Core Functionality
- **Rich Text Editing**: Full-featured text area with undo/redo support
- **File Management**: Create, open, save, and save-as functionality
- **Multiple File Types**: Support for .txt, .py, and all file formats
- **Auto-save Prompts**: Never lose your work with smart save reminders

### 🎨 User Interface
- **Modern GUI**: Clean, intuitive interface built with tkinter
- **Menu Bar**: Complete menu system with File, Edit, View, and Help options
- **Toolbar**: Quick access buttons for common operations
- **Status Bar**: Real-time line/column counter and file information
- **Modified Indicator**: Visual indicator for unsaved changes

### ⚙️ Customization Options
- **Font Size Control**: Adjustable font size from 8pt to 24pt
- **Word Wrap Toggle**: Enable/disable automatic word wrapping
- **Zoom Controls**: Zoom in/out with keyboard shortcuts
- **Theme Support**: Clean, modern appearance

### ⌨️ Keyboard Shortcuts
| Shortcut | Action |
|----------|--------|
| `Ctrl+N` | New file |
| `Ctrl+O` | Open file |
| `Ctrl+S` | Save file |
| `Ctrl+Shift+S` | Save As |
| `Ctrl+X` | Cut |
| `Ctrl+C` | Copy |
| `Ctrl+V` | Paste |
| `Ctrl+A` | Select All |
| `Ctrl++` | Zoom In |
| `Ctrl+-` | Zoom Out |
| `Ctrl+0` | Reset Zoom |
| `Ctrl+Q` | Quit Application |

## 📋 Requirements

- **Python**: 3.6 or higher
- **Operating System**: Windows, macOS, or Linux
- **Dependencies**: Only uses Python standard library (tkinter)

## 🛠️ Installation

### Option 1: Direct Download
1. Download the `main.py` file
2. Ensure Python is installed on your system
3. Run the application:
   ```bash
   python main.py
   ```

### Option 2: Clone Repository
```bash
git clone <repository-url>
cd text-pad
python main.py
```

### Option 3: Create Executable (Optional)
If you want to create a standalone executable:

```bash
# Install PyInstaller
pip install pyinstaller

# Create executable
pyinstaller --onefile --windowed main.py

# The executable will be in the dist/ folder
```

## 🎯 Usage Guide

### Getting Started
1. **Launch the Application**: Run `python main.py`
2. **Start Typing**: The text area is ready for immediate use
3. **Save Your Work**: Use `Ctrl+S` or the Save button in the toolbar

### Basic Operations

#### Creating a New Document
- Click **File → New** or press `Ctrl+N`
- Or click the **New** button in the toolbar

#### Opening Existing Files
- Click **File → Open** or press `Ctrl+O`
- Navigate to your file and select it
- Supported formats: .txt, .py, and all file types

#### Saving Documents
- **Save**: `Ctrl+S` or toolbar button (saves to current file)
- **Save As**: `Ctrl+Shift+S` (saves with new name/location)

#### Text Editing
- **Undo/Redo**: Built-in support for multiple undo levels
- **Copy/Paste**: Standard `Ctrl+C`, `Ctrl+V` operations
- **Select All**: `Ctrl+A` to select entire document

### Advanced Features

#### Font Customization
- Use the **Font Size** dropdown in the toolbar
- Or use keyboard shortcuts: `Ctrl++` to zoom in, `Ctrl+-` to zoom out
- Reset to default size with `Ctrl+0`

#### Word Wrap
- Toggle **Word Wrap** checkbox in the toolbar
- When enabled, long lines wrap to the next line
- When disabled, horizontal scrolling is available

#### Status Information
- **Line/Column Counter**: Shows current cursor position
- **File Name**: Displays the name of the current file
- **Modified Indicator**: Red asterisk (*) shows unsaved changes

## 🏗️ Project Structure

```
text-pad/
├── main.py              # Main application file
├── README.md           # This documentation
└── requirements.txt    # Dependencies (empty - uses stdlib only)
```

## 🔧 Technical Details

### Architecture
- **GUI Framework**: tkinter (Python's standard GUI library)
- **Text Widget**: ScrolledText with advanced features
- **File Handling**: UTF-8 encoding support
- **Event System**: Comprehensive keyboard and mouse event handling

### Key Components
- `TextPad` class: Main application class
- Menu system with cascading menus
- Toolbar with quick access buttons
- Status bar with real-time information
- Text area with scrollbars and formatting

### Error Handling
- File operation error handling
- Graceful application shutdown
- User-friendly error messages
- Auto-save prompts for unsaved changes

## 🐛 Troubleshooting

### Common Issues

#### Application Won't Start
- **Check Python Installation**: Ensure Python 3.6+ is installed
- **Verify tkinter**: tkinter should be included with Python
- **Run from Terminal**: Use `python main.py` from command line

#### File Save Issues
- **Check Permissions**: Ensure write permissions in target directory
- **Disk Space**: Verify sufficient disk space
- **File Lock**: Close file if opened in another application

#### Display Issues
- **Font Rendering**: Try different font sizes if text appears blurry
- **Window Size**: Application has minimum size requirements (400x300)
- **High DPI**: Application should work with high DPI displays

### Getting Help
1. Check this README for common solutions
2. Verify Python and tkinter installation
3. Try running from command line for error messages
4. Check file permissions and disk space

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Report Bugs**: Create an issue with detailed description
2. **Feature Requests**: Suggest new features or improvements
3. **Code Contributions**: Submit pull requests with improvements
4. **Documentation**: Help improve this README or add comments

### Development Setup
```bash
# Clone the repository
git clone <repository-url>
cd text-pad

# Run the application
python main.py

# Make your changes and test
# Submit a pull request
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with Python's tkinter library
- Inspired by simple, efficient text editors
- Thanks to the Python community for excellent documentation

## 📞 Support

If you need help or have questions:
- Create an issue in the repository
- Check the troubleshooting section above
- Ensure you're using Python 3.6 or higher

---

**Happy Typing! 🎉**

*Text Pad - Simple, Fast, Reliable Text Editing* 
