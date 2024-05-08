import os
from PIL import Image

def get_file_path_list(directory_name) :
    file_list = []
    for filename in os.listdir(directory_name):
        f = os.path.join(directory_name, filename)
        if os.path.isfile(f) and filename != '.DS_Store':
            file_list.append(filename)
    return file_list


save_to_dir_path = 'opt/icons/'
file_path_list = []
directory_name='Images'
file_path_list = get_file_path_list(directory_name)
current_dir = os.getcwd()
new_path = os.path.join(current_dir,save_to_dir_path)
if os.path.isdir(new_path) :
    pass
else:
    os.makedirs(new_path)

for image_file in file_path_list:
    f = os.path.join(directory_name,image_file)
    img = Image.open(f)
    icon=img.rotate(270).resize((120,120)).convert('RGB')
    icon.save(new_path+image_file,'JPEG')