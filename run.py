#!/usr/bin/env python3

import os
import time
from git import Repo

repo_dir = os.path.join('./', 'example-repo')
repo = Repo.init(repo_dir)
with open(os.path.join(repo_dir, 'records.txt'), 'w'):
    pass
#git = repo.git
#git.add(os.path.join('./', __file__))
#git.commit(message='提交自己测试')
#git.push()
