#!/usr/bin/env python3
import os
import sys
import getopt

from git import Repo

class Dancing():
    
    branch_name = 'dancing_master'
    file_name = '.dancing.log'

    def __init__(self, repo, mode):
        self.repo = Repo.init(repo)
        os.chdir(repo)
        with open(self.file_name, 'a+') as f:
            if len(self.repo.heads) == 0:   # 如果是空仓库, 则进行一次提交，因为不提交的话不能创建新的分支
                self.repo.index.add(items=[self.file_name])
                self.repo.index.commit('first commit')
            
            branch = self.repo.create_head(self.branch_name)    # 创建一个名为dancing_master的分支
            branch.checkout()

        self.mode = mode

    def run(self):
        pass
        

if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "r:m:", ["repo=", "mode="])
    repo, mode = "./example-repo", "random"
    for key, val in opts:
        if key in ("-r", "--repo"):
            repo = val
        elif key in ("-m", "--mode"):
            mode = val
    dancing = Dancing(repo, mode)
    dancing.run()
            