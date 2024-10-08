## Veta 
Simple Version Control System for Learning Purposes. 
Inspired from git

## Inspiration
The idea for this repo is to get intuition behind git and how version control works. Its ideal for beginners who have  basic understanding about git commands but don't know what goes behind the scenes. 



## Basic Entities in Version Control 
The Basic Entity to git version control is Objects. 
Objects are file based entities that represent either :- 
* Blob (Large Binary object)
* Tree ( Tree of changes) 
* Commit ( Commited Changes ) 


## Commands & Workings 


**`init`** 
Init command initializes the folder and files for working of version control. It sets `.veta` folder with `objects` folder and `index` file 

**`add`**
adds particular file to tracking and create object file of the given file, the object file consists of compressed data of original file and hash of the file is added to `index` file along with file name and other information  

**`commit`** 
commit represent a specific point in project's history. It is represented by commit object , commit object consists of metadata including commit message and date. It also points to tree that represent state of the project at that commit and includes previous commit object.


## Contribution 
You are free to share your ideas and code to improve this Repo. This repo is designed such that anyone can come and understand what's going behind the scenes. Code Readability is first priority rather than functionality or performance given existing tools like git are pretty much in standard use. 

## Resources 
[Git Internals by John Britton of GitHub](https://www.youtube.com/watch?v=lG90LZotrpo)

[Git Internals - How Git Works](https://www.youtube.com/watch?v=P6jD966jzlk)