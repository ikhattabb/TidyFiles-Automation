# ---------------------------------------------------------
# Program: TidyFiles 
# Author: [KHATTAB ALRDADDI]
# Purpose: Automatically organizes Downloads & Desktop into categories
# ---------------------------------------------------------

import os
import shutil

# --- 1. SETUP PATHS ---
# المصادر (الأماكن التي سيتم تنظيفها)
sources = [
    os.path.expanduser("~/Downloads"),
    os.path.expanduser("~/Desktop")
]

# الوجهات (الأماكن التي ستنقل إليها الملفات)
img_dest = os.path.expanduser("~/Pictures/Organized_Images")
vid_dest = os.path.expanduser("~/Videos/Organized_Videos")
doc_dest = os.path.expanduser("~/Documents/Organized_Docs")
music_dest = os.path.expanduser("~/Music/Organized_Music") 

# إنشاء المجلدات إذا لم تكن موجودة
for folder in [img_dest, vid_dest, doc_dest, music_dest]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# --- 2. DEFINE EXTENSIONS ---
image_exts = [".jpg", ".jpeg", ".png", ".jfif", ".gif"]
video_exts = [".mp4", ".mkv", ".mov", ".avi", ".webm"]
doc_exts = [".pdf", ".docx", ".txt", ".xlsx", ".pptx"]
music_exts = [".mp3", ".wav", ".flac", ".m4a"] 

# --- 3. USER INTERACTION ---
print("--- Personal File Assistant ---")
choice = input("What would you like to organize? (images / videos / docs / music / all): ").lower()

# --- 4. THE CORE LOGIC ---
moved_count = 0

# المرور على كل مسار مصدر (التحميلات وسطح المكتب)
for path in sources:
    if not os.path.exists(path):
        continue
        
    for filename in os.listdir(path):
        file_ext = os.path.splitext(filename)[1].lower()
        source_file = os.path.join(path, filename)

        # تخطي المجلدات، نحتاج الملفات فقط
        if os.path.isdir(source_file):
            continue

        target_folder = None
        label = ""

        # تحديد الوجهة بناءً على النوع واختيار المستخدم
        if (choice == "images" or choice == "all") and file_ext in image_exts:
            target_folder, label = img_dest, "IMAGE"
        elif (choice == "videos" or choice == "all") and file_ext in video_exts:
            target_folder, label = vid_dest, "VIDEO"
        elif (choice == "docs" or choice == "all") and file_ext in doc_exts:
            target_folder, label = doc_dest, "DOC"
        elif (choice == "music" or choice == "all") and file_ext in music_exts:
            target_folder, label = music_dest, "MUSIC"

        # تنفيذ عملية النقل إذا انطبقت الشروط
        if target_folder:
            try:
                shutil.move(source_file, os.path.join(target_folder, filename))
                print(f"[{label}] Moved: {filename} from {os.path.basename(path)}")
                moved_count += 1
            except Exception as e:
                print(f"Error moving {filename}: {e}")

print(f"\nClean-up complete! Total files moved: {moved_count}")