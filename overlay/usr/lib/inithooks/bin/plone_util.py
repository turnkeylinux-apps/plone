#!/usr/bin/python

import sys
from glob import glob
import subprocess

password = sys.argv[1]

BASEPATH = '/usr/local/share/plone'

ZOPEPATH = glob('%s/buildout-cache/eggs/ZServer-*.egg/' % BASEPATH)[0]
sys.path.append(ZOPEPATH)
sys.path.append(glob('%s/buildout-cache/eggs/Zope-*.egg/' % BASEPATH)[0])
sys.path.append(glob('%s/buildout-cache/eggs/zope.deferredimport-*.egg/' % BASEPATH)[0])
sys.path.append(glob('%s/buildout-cache/eggs/zope.proxy-*.egg/' % BASEPATH)[0])
sys.path.append(glob('%s/buildout-cache/eggs/zope.interface-*.egg/' % BASEPATH)[0])

from Zope2.utilities import zpasswd

for i in (1, 2):
    with open(
            '/usr/local/share/plone/zeocluster/parts/client%d/inituser' % i,
            'w') as f:
        f.write('admin:' + zpasswd.generate_passwd(password, 'SHA'))

for i in ('.installed', 'buildout'):
    subprocess.call([
        'sed', '-i', 's/turnkey/%s/g' % password,
        '%s/zeocluster/%s.cfg' % (BASEPATH, i)
    ])

subprocess.call(['service', 'plone', 'restart'])
