#!/usr/bin/env python3

import os
import time
from git import Repo

repo = Repo('./')
git = repo.git
git.add(os.path.join('./', __file__))
git.commit(message='提交自己测试')
git.push()
