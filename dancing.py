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
            year = kargs.get('year')
            dt_end = datetime.now() if year is None else datetime(int(year), 12, 31)
            week_day = dt_end.weekday()
            lask_week_days = 0 if week_day == 6 else week_day + 1
            dt_start = datetime.fromtimestamp(dt_end.timestamp() - (52 * 7 + lask_week_days) * 3600 * 24)
            days = dt_end - dt_start
            date_iter = (datetime.fromtimestamp(dt_start.timestamp() + d * 24 * 3600).date() for d in range(days.days))
            week_map = [[] for _ in range(7)]
            
            with open(self.file_name, 'a+') as f:
                for i, d in enumerate(date_iter):
                    cnt = 0 
                    commit_datetimes = sorted(
                        [datetime(d.year, d.month, d.day, randint(0, 23), randint(0, 59), randint(0, 59)) for _ in range(5)],
                        reverse=True
                    )
                    if randint(0,3) == 0:
                        for n in range(randint(0, 5)):
                            msg = '第' + str(n+1) + '次提交\n'
                            commit_datetime = commit_datetimes.pop()
                            f.write(str(commit_datetime.date()) + ' ' + msg)
                            f.read()
                            cnt += 1
                            self.repo.git.add(self.file_name)   # 这里用self.repo.index报错，不知为何
                            self.repo.git.commit(message=msg, date=commit_datetime)
                    week_map[i % 7].append(cnt)
                self.preview(week_map)
            
    def preview(self, week_map):
        for line in week_map:
            for c in line:
                if c > 0:
                    print('██', end=' ')
                else:
                    print('░░', end=' ')
            print()
        

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
            