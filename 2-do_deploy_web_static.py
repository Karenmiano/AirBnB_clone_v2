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
        with settings(warn_only=True):
            fileregex = re.compile(r'.*/?((.*)\.tgz)')
            filefind = fileregex.search(archive_path)
            file_name = filefind.group(1)
            destination = f"/tmp/{file_name}"
            res1 = put(archive_path, destination)
            decompress_to = f"/data/web_static/releases/{filefind.group(2)}/"
            res2 = run(f"mkdir -p {decompress_to}")
            res3 = run(f"tar -xzf {destination} -C {decompress_to}")
            res4 = run(f"rm {destination}")
            res7 = run(f"mv -u {decompress_to}web_static/* {decompress_to}")
            res8 = run(f"rm -rf {decompress_to}web_static")
            res5 = run("rm -rf /data/web_static/current")
            res6 = run(f"ln -s {decompress_to} /data/web_static/current")
            results = [res1, res2, res3, res4, res5, res6, res7, res8]
            if all(result.succeeded for result in results):
                return True
            return False
    return False
