import os
import zipfile

def convert_n64_to_z64(filename):
    """
    Hàm này chuyển đổi phần mở rộng .n64 thành .z64 cho một tệp cụ thể.
    """
    new_filename = filename[:-4] + ".z64"
    os.rename(filename, new_filename)
    return new_filename

def zip_z64_files():
    try:
        # Lấy đường dẫn của thư mục hiện tại
        current_directory = os.getcwd()

        # Duyệt qua tất cả các tệp trong thư mục hiện tại
        for filename in os.listdir(current_directory):
            # Kiểm tra xem tệp có phải là một tệp .z64 không
            if filename.endswith(".z64"):
                # Tạo đường dẫn đầy đủ cho tệp .z64
                z64_file_path = os.path.join(current_directory, filename)

                # Tạo tên cho tệp zip
                zip_file_name = filename.replace(".z64", ".zip")
                
                # Tạo đường dẫn đầy đủ cho tệp zip
                zip_file_path = os.path.join(current_directory, zip_file_name)

                # Tạo một đối tượng zip sử dụng thuật toán nén tốt nhất
                with zipfile.ZipFile(zip_file_path, 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
                    # Thêm tệp .z64 vào tệp zip với cùng tên
                    zipf.write(z64_file_path, arcname=filename)
                
                print(f"Nén thành công tệp {filename} thành {zip_file_name}")

            # Kiểm tra xem tệp có phải là một tệp .n64 không
            elif filename.endswith(".n64"):
                # Chuyển đổi phần mở rộng .n64 thành .z64
                new_filename = convert_n64_to_z64(filename)
                print(f"Đã chuyển {filename} thành {new_filename}")

        print("Hoàn thành nén tệp.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {str(e)}")

# Gọi hàm để thực hiện quá trình nén
zip_z64_files()
