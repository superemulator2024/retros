import os

def format_file_name(file_name):
    """
    Hàm này chuyển đổi tên file thành dạng yêu cầu: xóa bỏ dấu cách và chuyển ký tự đầu thành chữ hoa.
    """
    # Tách tên file và phần mở rộng
    name, extension = os.path.splitext(file_name)
    # Xóa bỏ dấu cách và chuyển ký tự đầu thành chữ hoa
    formatted_name = name.replace("_", " ").title()
    return formatted_name

def list_zip_files():
    # Lấy đường dẫn của thư mục hiện tại
    current_directory = os.getcwd()

    # Duyệt qua tất cả các tệp trong thư mục hiện tại
    for filename in os.listdir(current_directory):
        # Kiểm tra xem tệp có phải là một tệp .zip không
        if filename.endswith(".zip"):
            # Tách phần tên tệp và phần mở rộng
            file_name, file_extension = os.path.splitext(filename)
            # Chuẩn hóa tên file
            formatted_name = format_file_name(file_name)
            # In ra thông tin về tên tệp
            print(f"array('id' => '{file_name}', 'name' => '{formatted_name}'),")

# Gọi hàm để thực hiện quá trình liệt kê các tệp .zip
list_zip_files()
