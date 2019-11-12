import sys
import git

#for line in sys.stdin:
 #   local_ref, local_sha1, remote_ref, remote_sha1 = line.strip().split()
 #   print(sys.stdin.file)
repo = Repo



for commit in repo.iter_commits('master'):
	print(commit)  


