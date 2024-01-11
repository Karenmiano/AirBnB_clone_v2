#!/usr/bin/python3
"""Defines function do_pack"""

from __future__ import with_statement
from fabric.api import local, settings, put, run, sudo, env
from datetime import datetime
import os.path
import re


env.hosts = ['54.144.142.198', '54.172.80.140']


def do_deploy(archive_path):
    """Deploy archive file to environment hosts"""
    if os.path.isfile(archive_path):
        fileregex = re.compile(r'.*/((.*)\.tgz)')
        filefind = fileregex.search(archive_path)
        file_name = filefind.group(1)
        destination = f"/tmp/{file_name}"
        res1 = put(archive_path, destination)
        if res1.failed is True:
            return False
        decompress_to = f"/data/web_static/releases/{filefind.group(2)}/"
        res2 = run(f"mkdir -p {decompress_to}")
        if res2.failed is True:
            return False
        res3 = run(f"tar -xzf {destination} -C {decompress_to}")
        if res3.failed is True:
            return False
        res4 = run(f"rm {destination}")
        if res4.failed is True:
            return False
        res7 = run(f"mv -u {decompress_to}web_static/* {decompress_to}")
        if res7.failed is True:
            return False
        res8 = run(f"rm -rf {decompress_to}web_static")
        if res8.failed is True:
            return False
        res5 = run("rm -rf /data/web_static/current")
        if res5.failed is True:
            return False
        res6 = run(f"ln -s {decompress_to} /data/web_static/current")
        if res6.failed is True:
            return False
        return True
    return False