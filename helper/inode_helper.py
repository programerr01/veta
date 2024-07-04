""" 
 files and directories  operations

"""
import os 


def initialize_empty_repo():
    curr_dir = os.getcwd();
    curr_dir = os.path.join(curr_dir,".veta")
    if(check_initialization(folder_path=curr_dir)):
        print("Reinitialized repo in ", curr_dir);
        return 3;
    return initialize_empty_repo_folder() 


def initialize_empty_repo_folder(folder_path=None):
    if(not folder_path):
        folder_path = os.getcwd()
    complete_folder_path =os.path.join(folder_path,".veta")
    try:
        os.makedirs(complete_folder_path)
    except Exception as e:
        print("Some Issue in the initialization process")
        return -3
    ## Blobs, Commits and Trees makes most of the git files which are represented as objects 
    objects_folder = os.path.join(complete_folder_path,"objects");
    try:
        os.makedirs(objects_folder)
    except Exception as e:
        print("Some Issue in the initialization process")
        return -3;
    print("Initialized Empty Git Repo in ", complete_folder_path)
    return 0;



def check_initialization(file_name=None, folder_path=None):
    if(not folder_path):
        folder_path = os.getcwd();
    if(not file_name):
        file_name = "";
    full_path = os.path.join(folder_path,file_name)
    return not os.path.isfile(full_path) and os.path.isdir(full_path)


def generate_object(file_name,data):
    base_path = os.path.join(os.getcwd(),".veta","objects")
    complete_path = os.path.join(base_path,file_name)
    if(not os.path.isfile(complete_path)): 
        with open(complete_path,"wb") as f:
            f.write(bytes(data.encode('utf-8'))) 
    return 0;
