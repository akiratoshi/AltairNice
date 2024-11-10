import os
import re

def rename_files_and_replace_content(root_dir, old_name="cygnus", new_name="altairnice"):
    # Biểu thức chính quy để tìm các tệp chứa "cygnus" trong tên (không phân biệt hoa thường)
    filename_pattern = re.compile(old_name, re.IGNORECASE)
    
    # Duyệt qua toàn bộ thư mục và tệp trong root_dir
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            # Nếu tên tệp chứa "cygnus", chúng ta sẽ đổi tên
            if filename_pattern.search(filename):
                old_filepath = os.path.join(dirpath, filename)
                new_filename = filename_pattern.sub(new_name, filename)  # Đổi tên tệp mới
                new_filepath = os.path.join(dirpath, new_filename)
                
                # Đổi tên tệp
                os.rename(old_filepath, new_filepath)
                print(f"Renamed file: {old_filepath} -> {new_filepath}")
                
                # Thay đổi nội dung của tệp nếu cần
                replace_content(new_filepath, old_name, new_name)

def replace_content(filepath, old_text="cygnus", new_text="altairnice"):
    # Đọc nội dung của tệp
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Thay thế nội dung từ "cygnus" sang "altairnice"
    new_content = content.replace(old_text, new_text)
    
    # Ghi lại nội dung đã thay thế vào tệp
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(new_content)
    print(f"Updated content in: {filepath}")

# Chạy mã khi file này được thực thi trực tiếp
if __name__ == "__main__":
    # Thay đổi đường dẫn thư mục ở đây
    root_dir = r"D:\in3d\AltairNice\Firmware\Keyboard\zmk-config"
    rename_files_and_replace_content(root_dir)