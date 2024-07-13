import argparse 

def init_parser():
    parser = argparse.ArgumentParser(description="Simple Version Control Tool")
    
    subparsers = parser.add_subparsers(dest="command",required=True) 

    parser_init = subparsers.add_parser("init",help="Initialize Empty Repo")
    
    parser_add = subparsers.add_parser("add",help="Add file to repo")
    parser_add.add_argument("file",type=str,help="File to add")

    parser_commit = subparsers.add_parser("commit",help="Commit changes to repo")
    return parser

if __name__ == "__main__":
    init_parser();
