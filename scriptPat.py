#!/usr/bin/env python3
import os
def create():
    Documents = os.popen("git diff --cached --name-status | cut -f2").read()
    for name in Documents:
        print(name)
    return sys_msg
if  __name__ == '__main__':
   create()

