import os
from nose.plugins import Plugin
from anybox.nose_selenium.selenium import SeleniumTestCase


class OdooQunit(Plugin):
    name = 'odoo-qunit'
    modules = None
    url = None
    odoo_version = None

    def options(self, parser, env=os.environ):
        super(OdooQunit, self).options(parser, env=env)
        parser.add_option('--odoo-qunit-odoo-version',
                          default=env.get('ODOO_QUNIT_ODOO_VERSION', '9'),
                          metavar='VERSION',
                          choices=['7', '7.0', '8', '8.0', '9', '9.0'],
                          help="Odoo main version 7, 8 or 9")
        parser.add_option('--odoo-qunit-base-url',
                          default=env.get('ODOO_QUNIT_BASE_URL',
                                          'http://localhost:8069'),
                          metavar='URL',
                          help="url to odoo instance")
        parser.add_option('--odoo-qunit-modules',
                          default=env.get('ODOO_QUNIT_MODULES', '*'),
                          type=str,
                          help="Odoo Module list where to launch "
                               "Qunit test (comma separator)")

    def configure(self, options, conf):
        super(OdooQunit, self).configure(options, conf)
        if not self.enabled:
            return
        self.url = options.odoo_qunit_base_url
        self.modules = options.odoo_qunit_modules.split(',')
        self.odoo_version = options.odoo_qunit_odoo_version
        OdooQunitTestCase._url = self.url
        OdooQunitTestCase._modules = self.modules
        OdooQunitTestCase._odoo_version = self.odoo_version


class OdooQunitTestCase(SeleniumTestCase):

    _url = None
    _modules = None
    _odoo_version = None
