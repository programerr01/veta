import os 
from datetime import datetime 

from helper.inode_helper import check_initialization
from helper.common_helper import generate_latest_tree,set_head_reference,set_index_file
from helper.custom_helper import convert_byte_to_binary
from helper.inode_helper import generate_object
from helper.custom_helper import hash

git_dir = os.path.join(os.getcwd(),".veta")



def commit():
    # commit checks if the veta is initialized or not
    # if not initialized then it returns -1
    # if initialized then it generates the latest tree and create a new commit object   
    if(not check_initialization(git_dir)):
        print("Veta is not initialized")
        return -1;
    tree_data = generate_latest_tree();
    if(tree_data == -2):
        print("No files to commit")
        return -1;
    else:
        print(tree_data);
        tree_hash_value = hash(tree_data)
        generate_object(str(tree_hash_value), tree_data)
        commit_data = generate_latest_commit(tree_hash_value);
        commit_hash_value = hash(commit_data)
        generate_object(str(commit_hash_value), commit_data)    
        #set head reference to latest commit
        set_head_reference(str(commit_hash_value))

        #clear the index file and make it only contain reference of last tree object
        index_file = os.path.join(git_dir,"index")
        ref_ = f"tree {tree_hash_value} NULL\n"
        return set_index_file(ref_)

def generate_latest_commit(tree_reference):
    # generate a new object for the commit with data including 
    # commit message, tree reference and parent commit reference
    commit_data = "";
    date_ = datetime.now().strftime("%a %b %d %H:%M:%S %Y %z")
    commit_data += f"Admin,commit message,{date_}\n"
    commit_data += f"tree,{tree_reference}\n"

    #check for HEAD file to get the parent commit reference
    head_file = os.path.join(git_dir,"HEAD")
    parent_commit = "NULL"
    if(os.path.isfile(head_file)):
        with open(head_file,"r") as f:
            parent_commit = f.read().strip()
    commit_data += f"parent,{parent_commit}\n"
    return commit_data