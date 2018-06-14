#!env python
import shutil
import subprocess
import os
import sys


def get_last_commit(ext):
    git = subprocess.Popen('git show --name-only --oneline HEAD'.split(), stdout=subprocess.PIPE)
    grep = subprocess.Popen(['grep', '-i', '%s$' % ext], stdin=git.stdout, stdout=subprocess.PIPE)
    git.stdout.close()
    output, err = grep.communicate()
    if err:
        raise ValueError
    return output


def format(f):
    ff = os.path.splitext(f.lower())
    if ff == '.py':
        os.system('black {}'.format(f))
    elif ff == '.java':
        os.system('java --jar /tools/google-java-format-1.6-all-deps.jar --replace {}'.format(f))
    elif ff == '.go':
        os.system('gofmt -w {}'.format(f))


def has_ugly():
    git = subprocess.Popen('git status --short'.split(), stdout=subprocess.PIPE)
    grep = subprocess.Popen(['grep', ' M'], stdin=git.stdout, stdout=subprocess.PIPE)
    git.stdout.close()
    output, err = grep.communicate()
    if err:
        raise ValueError
    print(output)
    return len(output) != 0
    

if __name__ == '__main__':
    os.chdir(sys.argv[2])
    for f in get_last_commit(sys.argv[1]).split(b'\n'):
        format(f)
    if has_ugly():
        sys.exit(1)
    else:
        sys.exit(0)
