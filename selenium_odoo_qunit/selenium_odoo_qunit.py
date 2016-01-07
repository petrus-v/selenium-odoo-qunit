import nose
import os
import sys


def main():
    base_directory = os.path.dirname(os.path.abspath(__file__))
    qunit_test = os.path.join(base_directory, 'odoo_qunit_tests/')
    if 'with-selenium' not in sys.argv:
        sys.argv.extend(['--with-selenium'])
    if 'with-odoo-qunit' not in sys.argv:
        sys.argv.extend(['--with-odoo-qunit'])
    sys.argv.append(qunit_test)
    nose.main()

if __name__ == '__main__':
    main()
