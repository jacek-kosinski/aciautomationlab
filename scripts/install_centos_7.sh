#!/usr/bin/env bash
yum install -y epel-release # <1>
yum install -y python2-pip python-devel # <2>
yum groupinstall -y "Development Tools" # <3>
pip install --upgrade pip # <4>
pip install acitoolkit # <5>
