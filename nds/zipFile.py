import os
import zipfile

def zip_nds_files():
    try:
        current_directory = os.getcwd()
        for filename in os.listdir(current_directory):
            if filename.endswith(".nds"):
                z64_file_path = os.path.join(current_directory, filename)
                zip_file_name = filename.replace(".nds", ".zip")
                zip_file_path = os.path.join(current_directory, zip_file_name)
                with zipfile.ZipFile(zip_file_path, 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
                    zipf.write(z64_file_path, arcname=filename)
                
                print(f"Nén thành công tệp {filename} thành {zip_file_name}")

        print("Hoàn thành nén tệp.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {str(e)}")

zip_nds_files()
