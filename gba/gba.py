from PIL import Image
import os

folder_path = os.getcwd()

for filename in os.listdir(folder_path):
    if filename.endswith((".gba",".GBA")):
        new_filename = os.path.join(folder_path, os.path.splitext(filename)[0] + ".ga")
        os.rename(os.path.join(folder_path, filename), new_filename)
        print("Game {} to {}".format(filename, os.path.basename(new_filename)))

for filename in os.listdir(folder_path):
    if filename.endswith(".webp"):
        img = Image.open(os.path.join(folder_path, filename))
        new_filename = os.path.join(folder_path, os.path.splitext(filename)[0] + ".png")
        img.save(new_filename, "png")
        img.close()
        os.remove(os.path.join(folder_path, filename))
        print("Image {} to {}".format(filename, os.path.basename(new_filename)))
