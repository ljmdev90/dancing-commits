#!/usr/bin/env python3
import os
import sys
import getopt
from datetime import datetime
from random import randint

from git import Repo

class Dancing():
    
    branch_name = 'dancing_master'
    file_name = '.dancing.log'

    modes = ['random']

    def __init__(self, repo):
        self.repo = Repo.init(repo)
        os.chdir(repo)
        with open(self.file_name, 'a+') as f:
            if len(self.repo.heads) == 0:   # 如果是空仓库, 则进行一次提交，因为不提交的话不能创建新的分支
                self.repo.index.add(items=[self.file_name])
                self.repo.index.commit('first commit')
            
            branch = self.repo.create_head(self.branch_name)    # 创建一个名为dancing_master的分支
            branch.checkout()

    def run(self, mode, **kargs):
        if mode not in self.modes:
            raise ValueError

        if mode == 'random':
            print(kargs)
            
            year = kargs.get('year')
            dt_end = datetime.now() if year is None else datetime(int(year), 12, 31)
            week_day = dt_end.weekday()
            lask_week_days = 0 if week_day == 6 else week_day + 1
            dt_start = datetime.fromtimestamp(dt_end.timestamp() - (52 * 7 + lask_week_days) * 3600 * 24)
            print(dt_end, dt_start)
            days = dt_end - dt_start
            print(days)
        

if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "r:m:y", ["repo=", "mode=", "year="])
    repo, mode = "./example-repo", "random"
    params = {}
    for key, val in opts:
        if key in ("-r", "--repo"):
            repo = val
        elif key in ("-m", "--mode"):
            mode = val
        elif key in ("-y", "--year"):
            params['year'] = val
    dancing = Dancing(repo)
    dancing.run(mode, **params)
            