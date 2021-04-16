#!/usr/bin/python3
"""
generates a .tgz archive from the contents of the web_static folder
of your AirBnB Clone repo using the function do_pack
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


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
