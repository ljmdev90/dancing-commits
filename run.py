#!/usr/bin/env python3

import os
import shutil
from datetime import datetime
from random import randint
from git import Repo

repo_dir = os.path.join('./', 'example-repo')
if os.path.exists(repo_dir):
    shutil.rmtree(repo_dir)
repo = Repo.init(repo_dir)
os.chdir(repo_dir)
record_file = 'records.txt'
with open(record_file, 'a+') as f:
    f.seek(0)
    f.truncate()

    dt_now = datetime.now()
    week_num = dt_now.weekday()
    dt_start = dt_now.timestamp() - (52 * 7 + week_num + 1) * 3600 * 24
    days = dt_now - datetime.fromtimestamp(dt_start)
    days_iter = (datetime.fromtimestamp(dt_start + d * 24 * 3600).date() for d in range(days.days))
    days_map = [[] for _ in range(7)]
    git = repo.git
    for i, d in enumerate(days_iter):
        cnt = 0 
        commit_times = sorted([datetime(d.year, d.month, d.day, randint(0, 23), randint(0, 59), randint(0, 59))
        for _ in range(5)], reverse=True)
        if randint(0,3) == 0:
            for n in range(randint(0, 5)):
                msg = '第' + str(n+1) + '次提交\n'
                commit_time = commit_times.pop()
                f.write(str(commit_time) + ' ' + msg)
                f.read()
                cnt += 1
                git.add(record_file)
                git.commit(message=msg, date=commit_time)
        days_map[i % 7].append(cnt)
for line in days_map:
    for c in line:
        print(c, end=' ')
    print()
