#!/usr/bin/env python3
def Compare(path):
    div = path.split("/")
    if div[len(div) - 1] == "teste.txt":
        return 1
    else:
        return 0

