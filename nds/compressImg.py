import os
from PIL import Image

def convert_resize_images(directory):
    # Tạo thư mục bak nếu chưa tồn tại
    bak_dir = os.path.join(directory, 'bak')
    os.makedirs(bak_dir, exist_ok=True)

    # Duyệt qua tất cả các file trong thư mục hiện tại
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            # Kiểm tra xem file có phải là ảnh không
            if any(filename.endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif']):
                try:
                    # Đọc và xử lý ảnh
                    with Image.open(filepath) as img:
                        # Chuyển định dạng và thay đổi kích thước
                        new_img = img.convert('RGB').resize((375, 338))
                        # Lưu ảnh mới
                        new_filename = os.path.splitext(filename)[0] + '.jpg'
                        new_filepath = os.path.join(directory, new_filename)
                        new_img.save(new_filepath)

                        # Di chuyển ảnh gốc vào thư mục bak
                        bak_filepath = os.path.join(bak_dir, filename)
                        os.replace(filepath, bak_filepath)

                        print(f"Đã chuyển {filename} và lưu thành {new_filename}")
                except Exception as e:
                    print(f"Lỗi khi xử lý {filename}: {e}")

# Gọi hàm với thư mục hiện tại
convert_resize_images('.')
