#!/usr/bin/python3

import sys
from glob import glob
import subprocess
from base64 import b64encode
from hashlib import sha1

password = sys.argv[1]

BASEPATH = '/usr/local/share/plone'


for i in (1, 2):
    with open(
            '/usr/local/share/plone/zeocluster/parts/client%d/inituser' % i,
            'w') as f:
        f.write('admin:{SHA}' +
                b64encode(sha1(password.encode()).digest()).decode())

for i in ('.installed', 'buildout'):
    subprocess.call([
        'sed', '-i', 's/turnkey/%s/g' % password,
        '%s/zeocluster/%s.cfg' % (BASEPATH, i)
    ])

subprocess.call(['service', 'plone', 'restart'])
