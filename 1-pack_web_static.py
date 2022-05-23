#!/usr/bin/python3
"""Generate a .tgz file with contents of the web_static folder"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Function to compress the web_static folder
    """
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file = "versions/web_static_{}.tgz".format(time)
    try:
        local("mkdir -p ./versions")
        local("tar -cvz --file={} ./web_static".format(file))
        local("chmod 664 {}".format(file))
        return file
    except Exception as err:
        return None
