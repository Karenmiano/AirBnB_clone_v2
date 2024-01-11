#!/usr/bin/python3
"""Defines function do_pack"""

from __future__ import with_statement
from fabric.api import local, settings
from datetime import datetime


def do_pack():
    """Create a tar gzipped archive of directory web_static"""
    now = datetime.utcnow()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_path = f"versions/web_static_{timestamp}.tgz"
    local("mkdir -p versions")
    with settings(warn_only=True):
        check = local(f"tar -czvf {archive_path} web_static")
    if check.failed:
        return None
    else:
        return archive_path
