import nose
import os
import sys


def main():
    base_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base_directory)
    qunit_test = os.path.join(base_directory, 'odoo_qunit_tests/')
    nose_config = os.path.join(base_directory, 'nose.cfg')
    if '-c' not in sys.argv and '--config' not in sys.argv:
        sys.argv.extend(['-c', nose_config])
    sys.argv.append(qunit_test)
    nose.main()

if __name__ == '__main__':
    main()
