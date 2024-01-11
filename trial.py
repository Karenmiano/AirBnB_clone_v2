from __future__ import with_statement
from fabric.api import local, settings


def trying():
    result = local("Im not")
    if result.failed:
        print("Hello")