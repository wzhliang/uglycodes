#!env python
import shutil
import subprocess
import os
import sys


def get_last_commit():
    git = subprocess.Popen('git --no-pager show --name-only --oneline HEAD'.split(), stdout=subprocess.PIPE)
    sed = subprocess.Popen(['sed', '1d'], stdin=git.stdout, stdout=subprocess.PIPE)
    git.stdout.close()
    output, err = sed.communicate()
    if err:
        raise ValueError
    return output


def format(f):
    if f.endswith('.py'):
        print('Formatting {}'.format(f))
        os.system('black {}'.format(f))
    elif f.endswith('.java'):
        print('Formatting {}'.format(f))
        os.system('java -jar /tools/google-java-format-1.6-all-deps.jar --replace {}'.format(f))
    elif f.endswith('.go'):
        print('Formatting {}'.format(f))
        os.system('gofmt -w {}'.format(f))
    else:
        print('Unsupported file {}'.format(f))


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
    fs = get_last_commit()
    print('Files changed in last commit:')
    print(fs)
    for f in fs.split(b'\n')[:-1]:
        format(f.strip().decode())  # for some reason, fs is b''
    if has_ugly():
        sys.exit(1)
    else:
        sys.exit(0)
