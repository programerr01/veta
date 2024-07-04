import os 


git_dir = os.path.join(os.getcwd(),".veta")


    
def update_index(hash_value,file_name):
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
    content_to_append =hash_value + " "+ file_name
    with open(index_file, "a+") as f:
        f.write(content_to_append+"\n")
    
