import getpass
import os
import sys

import builddoc
import makemsi

VER = '2.0.0.0'
VERSION = 'Version=%s' % VER
MANUFACTURER = '"Manufacturer=Oleksis Fraga"'
X86 = 'Platform=x86'
X64 = 'Platform=x64'
TOWIN = 'ToWindows'


def main():
    # signpwd = getpass.getpass('Password for signing:')
    # os.environ['SIGNPWD'] = signpwd

    builddoc.main()
    makemsi.main(['-o', 'launchwin-%s' %
                 VER, X86, VERSION, MANUFACTURER, TOWIN, 'launcher'])
    makemsi.main(['-o', 'launcher-%s' %
                 VER, X86, VERSION, MANUFACTURER, 'launcher'])
    makemsi.main(['-o', 'launchwin-%s' %
                 VER, X64, VERSION, MANUFACTURER, TOWIN, 'launcher'])
    makemsi.main(['-o', 'launcher-%s' %
                 VER, X64, VERSION, MANUFACTURER, 'launcher'])


if __name__ == '__main__':
    sys.exit(main())
