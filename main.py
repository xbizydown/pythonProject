"""

This is just a file that I use as the main one.
I plan to refactor my entire project, and when I am done with it, I will change everything.
The whole structure will be ready, and I will make the necessary changes.

"""
import os

def print_file_structure():
    for root, dirs, files in os.walk("."):
        for dir in dirs:
            print(os.path.join(root, dir))
        for file in files:
            print(os.path.join(root, file))

print_file_structure()