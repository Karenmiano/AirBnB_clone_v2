#!/usr/bin/python3
"""Defines function do_pack"""

from __future__ import with_statement
from fabric.api import local, settings, put, run, sudo, env
from datetime import datetime
import os.path
import re


env.hosts = ['54.144.142.198', '54.172.80.140']


def do_pack():
    """Create a tar gzipped archive of directory web_static"""
    now = datetime.utcnow()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(timestamp)
    local("mkdir -p versions")
    with settings(warn_only=True):
        check = local("tar -czvf {} web_static".format(archive_path))
    if check.failed:
        return None
    else:
        return archive_path


def do_deploy(archive_path):
    """Deploy archive file to environment hosts"""
    if os.path.isfile(archive_path):
        with settings(warn_only=True):
            fileregex = re.compile(r'.*/?((.*)\.tgz)')
            filefind = fileregex.search(archive_path)
            file_name = filefind.group(1)
            destination = "/tmp/{}".format(file_name)
            res1 = put(archive_path, destination)
            decompress_to = "/data/web_static/releases/{}/".format(filefind.group(2))
            res2 = run("mkdir -p {}".format(decompress_to))
            res3 = run("tar -xzf {} -C {}".format(destination, decompress_to))
            res4 = run("rm {}".format(destination))
            res7 = run("mv -u {}web_static/* {}".format(decompress_to, decompress_to))
            res8 = run("rm -rf {}web_static".format(decompress_to))
            res5 = run("rm -rf /data/web_static/current")
            res6 = run("ln -s {} /data/web_static/current".format(decompress_to))
            results = [res1, res2, res3, res4, res5, res6, res7, res8]
            if all(result.succeeded for result in results):
                return True
            return False
    return False
