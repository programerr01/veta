import os 
from helper.inode_helper import generate_object,check_initialization
from helper.custom_helper import convert_byte_to_binary,hash
from helper.common_helper import update_index
git_dir = os.path.join(os.getcwd(),".veta")


def add_file(file_name):
    if(not check_initialization(git_dir)):
        print("Veta is not initialized")
        return -1;
    file_path = os.path.join(os.getcwd(),file_name)
    if(not os.path.isfile(file_path)):
        print(file_name ,"doesn't exists")
        return -1;
    return add_file_helper(file_name)

def add_file_helper(file_name): 
    file_content = "";
    with open(file_name,"rb") as f:
        file_content = f.read() 
    byte_arr = convert_byte_to_binary(file_content)
    hash_value = hash(byte_arr)
    generate_object(str(hash_value), byte_arr) 
    update_index(hash_value,file_name);

