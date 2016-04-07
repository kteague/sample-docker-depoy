import subprocess
import os
import sys

def main(base_dir, git_repo):
    app_name = 'sample-app'
    images_dir = base_dir + os.sep + 'images/'
    tag = sys.argv[1]
    
    # copy app source code into Docker directory
    cmd = 'rm -rf %s%s%s' % (images_dir, os.sep, app_name)
    subprocess.call(cmd, shell=True)
    cmd = 'git clone --branch %s %s %s' % (tag, git_repo, images_dir + os.sep +app_name)
    print("CMD: cloning git repo %s at tag %s" % (git_repo, tag))
    subprocess.call(cmd, shell=True)
    
    # create Docker image
    cmd = "/usr/local/bin/docker build -t %s:%s %s" % (app_name, tag, images_dir)
    print("CMD: Building Docker image as %s:%s" % (app_name, tag))
    subprocess.call(cmd, shell=True)
