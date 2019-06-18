#!/usr/bin/env python3
import sys
import getopt

class Dancing():
    def __init__(repo, mode):
        pass

if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "r:m:", ["repo=", "mode="])
    repo, mode = "./example-repo", "random"
    for key, val in opts:
        if key in ("-r", "--repo"):
            repo = val
        elif key in ("-m", "--mode"):
            mode = val
    print(repo, mode)
            