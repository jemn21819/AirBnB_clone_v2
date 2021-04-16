#!/usr/bin/python3
"""
 (based on the file 1-pack_web_static.py) that distributes an archive to your
 web servers, using the function do_deploy
"""

from fabric.api import env, put, run, local, cd, lcd, sudo
import os
import re
from os.path import exists, isdir
from datetime import datetime
env.hosts = ['35.231.81.64', '34.74.73.209']


def do_pack():
    """ return the archive path if the archive has been correctly generated."""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_path = "versions/web_static_{}.tgz".format(time)
        local("tar -cvzf {} web_static".format(file_path))
        return file_path
    except:
        return None


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False


def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)


def do_clean(number=0):
    """Deletes out-of-date archives"""
    files = local("ls -1t versions", capture=True)
    file_names = files.split("\n")
    n = int(number)
    if n in (0, 1):
        n = 1
    for i in file_names[n:]:
        local("rm versions/{}".format(i))
    dir_server = run("ls -1t /data/web_static/releases")
    dir_server_names = dir_server.split("\n")
    for i in dir_server_names[n:]:
        if i is 'test':
            continue
        run("rm -rf /data/web_static/releases/{}"
            .format(i))
