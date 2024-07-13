import os 


git_dir = os.path.join(os.getcwd(),".veta")


    
def update_index(hash_value,file_name,type="blob"):
    index_file = os.path.join(git_dir,"index")
    file_contents = "";
    if(os.path.isfile(index_file)):
        with open(index_file,"r") as f:
            file_contents = f.read() 
    if(file_contents):
        for each in file_contents.split("\n"):
            blob_ = each.split(" ")[0]
            cfile_name_  = ' '.join(each.split(" ")[1:])
            cfile_name_ = cfile_name_.strip()
            if(blob_ == hash_value and cfile_name_ == file_name):
                return 0;
    content_to_append =type +" "+hash_value + " "+ file_name
    with open(index_file, "a+") as f:
        f.write(content_to_append+"\n")
        return 0;
    return -1;

def generate_latest_tree():    
    index_file = os.path.join(git_dir,"index")

    file_contents = "";
    if(os.path.isfile(index_file)):
        with open(index_file,"r") as f:
            file_contents = f.read() 
    if(not file_contents):
        return -2;
    file_contents = file_contents.strip().split("\n")
    print(file_contents)
    tree_content = ""
    tree_reference = "NULL\n";
    for each in file_contents:
        file_name = ' '.join(each.strip().split(" ")[2:])
        file_name = file_name.strip()
        hash_value = each.split(" ")[1]
        type_ = each.split(" ")[0]
        if(type_== "tree"):
            tree_reference = f"tree {hash_value} NULL\n"
            continue;
        tree_content += f"blob {hash_value} {file_name}\n"
    tree_content = tree_reference + tree_content
    return tree_content 


def set_head_reference(commit_hash_value):
    head_file = os.path.join(git_dir,"HEAD")
    with open(head_file,"w") as f:
        f.write(commit_hash_value)
    return 0;
    

def set_index_file(dt):
    index_file = os.path.join(git_dir,"index")
    with open(index_file,"w") as f:
        f.write(dt)
        return 0;
    return -1;