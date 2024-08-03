#!/usr/bin/python3

from options import init_parser
from helper.inode_helper import initialize_empty_repo
from helper.add_helper import add_file
from helper.commit_helper import commit
from helper.status_helper import status

def main():
    parser = init_parser()
    parsed_arguments = parser.parse_args()
    if(parsed_arguments.command == "init"):
        initialize_empty_repo()
    if(parsed_arguments.command == "add"):
       add_file(parsed_arguments.file) 
    if(parsed_arguments.command == "commit"):
        if(not parsed_arguments.m):
            print("Enter Commit message")
            return -1;
        commit(parsed_arguments.m)
    if(parsed_arguments.command == "status"):
        status();
if __name__ == "__main__":
    main()
