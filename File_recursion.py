from cgi import print_directory
from contextlib import nullcontext
from operator import truediv
import os
import re


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    isPathExist = os.path.isdir(path)
    fileList = os.listdir(path)
    list = []
   
    if isPathExist:
      print("Path Exist\n")
      print("\nAll Files and directories are: \n")
      print(fileList) 
    else:
      print("Path does not exists")
      return None
    for i in os.listdir(path):
      alldir = os.path.join(path,i)
      if os.path.isfile(alldir):
        if alldir.endswith(suffix):
          list.append(alldir)
        elif os.path.isdir(alldir):
          list = list + find_files(suffix,alldir)
    print("\nAll files with suffix "+ suffix +"\n")
    return list




# Let us print the files in the directory in which you are running this script
# print (os.listdir("./"))

# Let us check if this file is indeed a file!
#print (os.path.isfile("./testdir/khagen1"))

# Does the file end with .py?
#print ("./ex.py".endswith(".py"))

# print(find_files(".c", "./checkdirectory/pyhton"))
print("----test case 1-----\n")         
print(find_files(".py" ,"./checkdirectory"))      
print("\n\n----test case 2-----\n")
print(find_files(".c","./checkdirectory"))