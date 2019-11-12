import sys

for line in sys.stdin:
    local_ref, local_sha1, remote_ref, remote_sha1 = line.strip().split()
    print(local_sha1.fileName)




