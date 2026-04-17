# TidyFiles-Automation 🚀

A robust Python-based automation tool designed to streamline digital workspaces by automatically organizing cluttered folders (like Downloads and Desktop) into logical categories.

## ✨ Key Features
- **Smart Sorting:** Categorizes files into Images, Videos, Documents, and Music folders.
- **Dynamic Path Handling:** Uses `os.path.expanduser` to work seamlessly across different user profiles and operating systems.
- **User-Interactive:** Allows users to choose specific categories to organize or clean everything at once.
- **Error Safeguards:** Includes `try-except` blocks to handle file access errors gracefully.

## 🛠️ Built With
- **Python 3**
- **Core Libraries:** `os`, `shutil`

## 📖 How to Run
1. Ensure you have Python installed.
2. Download `tidy_files.py`.
3. Run the script via terminal or VS Code:
   ```bash
   python tidy_files.py
