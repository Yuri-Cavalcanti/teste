import os
import utils
from utils import debug, warn
from git import git, diff_tree, file_exists
from config import git_config
from git_attrs import git_attribute

def teste(old_rev, new_rev):
    changes = diff_tree('-r', old_rev, new_rev)
    nomeArquivos = []

    for item in changes:
        (old_mode, new_mode, old_sha1, new_sha1, status, filename) = item
        debug('diff-tree entry: %s %s %s %s %s %s'
              % (old_mode, new_mode, old_sha1, new_sha1, status, filename),
              level=5)
        nomeArquivos.append(filename)
        git.show(filename)

teste(old_rev,new_rev)