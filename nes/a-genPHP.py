import os

def format_filename(filename):
    name = filename.replace("_", " ").title()  
    name = os.path.splitext(name)[0]           
    return name

def create_file_list():
    file_list = []
    for filename in os.listdir():
        if filename.endswith(".ns"):
            id = os.path.splitext(filename)[0]
            name = format_filename(filename)
            file_list.append({'id': id, 'name': name})
    return file_list

if __name__ == "__main__":
    result = create_file_list()
    for item in result:
        print(f"array('id' => '{item['id']}', 'name' => '{item['name']}'),")
