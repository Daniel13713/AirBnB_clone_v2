#!/usr/bin/python3
"""Generate a .tgz file with contents of the web_static folder"""

from fabric.api import local, env, run, cd, put, lcd
from datetime import datetime

env.use_ssh_config = True
# env.hosts = ["webserver1", "webserver2"]
env.hosts = ["34.138.238.195", "54.82.92.255"]
env.user = "ubuntu"
time = datetime.utcnow().strftime('%Y%m%d%H%M%S')


def do_pack():
    """
    ------------------------------------------
    Function to compress the web_static folder
    ------------------------------------------
    """
    file = "versions/web_static_{}.tgz".format(time)
    try:
        local("mkdir -p ./versions")
        local("tar -zcf {} ./web_static".format(file))
        # local("chmod 664 {}".format(file))
        return file
    except Exception as err:
        return None


def do_deploy(archive_path):
    """
    ------------------------------
    Deploy the files o web servers
    ------------------------------
    """
    if not archive_path:
        run("echo $HOSTNAME")
        return False
    try:
        file = archive_path.split("/")[1]
        name = file.replace(".tgz", "")
        path_data = "/data/web_static/releases/{}".format(name)
        # Upload the file to remotes servers
        put(archive_path, "/tmp", use_sudo=True)
        # create folder with name of the file .tgz without extension
        run("mkdir -p {}".format(path_data))
        # Uncomprese the file .tgz
        run("tar xvzf /tmp/{0} -C {1}".format(file, path_data))
        # delete file .tgz
        run("rm /tmp/{}".format(file))
        # move all data from web_static to ..
        with cd("{}/web_static".format(path_data)):
            run("mv * ../")
        # delete symbolix link and create a new
        run("rm -rf /data/web_static/current")
        run("ln -sf {} /data/web_static/current".format(path_data))
        print("New version deployed!")
        return True
    except Exception as err:
        print(err)
        return False


def deploy():
    """
    ---------------------------------------------
    Call the another functions to full deployment
    ---------------------------------------------
    """

    # create localy a compresse file of the data
    file = do_pack()
    if file is None:
        return False

    # Deploy the data to servers
    deploy_value = do_deploy(file)

    return deploy_value


def do_clean(number=0):
    """
    ------------------------------------------
    Delete not needs archives and keep version
    0 or 1: keep only the most recent version of your archive
    2:  keep the most recent, and second most recent versions of your archive.
    etc...
    """

    number = int(number)
    if number in [0, 1]:
        number = 2
    else:
        number += 1
    # delete files
    with lcd("./versions"):
        local("rm -rf $(ls -t | grep web_static | tail -n+{})".format(number))
    with cd("/data/web_static/releases"):
        run("rm -rf $(ls -t | grep web_static | tail -n+{})".format(number))
