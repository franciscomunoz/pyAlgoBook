"""Recursive find for ocurrences of a file in a directory"""
import os

def find(path,filename):

    if os.path.isdir(path):
        for i_path in os.listdir(path):
            """Need to rejoin and look inside a new directory"""
            childpath = os.path.join(path,i_path)
            find(childpath,filename)

    else:
        if os.path.basename(path) == filename:
            print("Found file name : {0}".format(path))

if __name__ == '__main__':

    find("/home/francisco/", "delete.me")
