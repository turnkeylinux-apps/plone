#!/usr/bin/python
"""Set Plone initial admin password

Option:
    --pass=     unless provided, will ask interactively
"""

import sys
import getopt
from executil import system

from dialog_wrapper import Dialog

BASEPATH = '/usr/local/share/plone'

# will probably have to be changed for newer versions of Plone/Zope
sys.path.append('%s/buildout-cache/eggs/Zope2-2.13.24-py2.7.egg/Zope2/utilities' % BASEPATH)
import zpasswd

def usage(s=None):
    if s:
        print >> sys.stderr, "Error:", s
    print >> sys.stderr, "Syntax: %s [options]" % sys.argv[0]
    print >> sys.stderr, __doc__
    sys.exit(1)

DEFAULT_DOMAIN="www.example.com"

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass='])
    except getopt.GetoptError, e:
        usage(e)

    user = ''
    password = ''
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            password = val

    if not password:
        d = Dialog('TurnKey Linux - First boot configuration')
        password = d.get_password(
            "Plone Password",
            "Enter new password for the Plone 'admin' account.")

    for i in (1, 2):
        with open('/usr/local/share/plone/zeocluster/parts/client%d/inituser' % i, 'w') as f:
            f.write('admin:' + zpasswd.generate_passwd(password, 'SHA'))

    for i in ('.installed', 'buildout'):
        system('sed -i "s/turnkey/%s/g" %s/zeocluster/%s.cfg' % (password, BASEPATH, i))

if __name__ == "__main__":
    main()

