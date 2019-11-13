#!/usr/bin/env python3
def Compare(path):
    div = path.split("/")
    print(div[len(div) -1])
    if div[len(div) - 1] == "teste.txt":
        return 1
    else:
        return 0

