#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the
    contents of the web_static folder of your
    AirBnB Clone repo, using the function do_pack
"""
import os
from fabric.api import local
from datetime import datetime


def do_pack():
    """ generates a .tgz archive from the contents of the web_static """
    local("mkdir -p versions")
    file_name = "web_static_" + datetim.now().strftime("%Y%m%d%H%M%S") + ".tgz"
    file_path = "versions/" + file_name

    local("tar -cvzf {} web_static".format(file_path))
    if local("test -f {}".format(file_path)).succeeded:
        return file_path
    else:
        return None
