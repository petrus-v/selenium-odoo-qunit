# -*- coding: utf-8 -*-
import logging
from selenium_odoo_qunit.nose_plugins.odoo_qunit import OdooQunitTestCase
from selenium.webdriver.support.ui import WebDriverWait
from urlparse import urlparse, urljoin

log = logging.getLogger(__name__)


class TestOdooQunit(OdooQunitTestCase):
    def setUp(self):
        super(TestOdooQunit, self).setUp()
        log.debug(self.selenium.capabilities)
        self.sel = self.selenium
        self.base_url = self._url
        self.sel.implicitly_wait(60)
        self.modules = self._modules
        self.odoo_version = self._odoo_version

    def get_login_url(self):
        odoo = urlparse(self.base_url)
        return urljoin(odoo.geturl(), '/web/login?%s' % odoo.query)

    def get_qunit_url(self, module, module_attribute=None):
        odoo = urlparse(self.base_url)
        query = odoo.query
        if module and module.strip() != '*':
            query = '%s&%s=%s' % (odoo.query, module_attribute, module)
        return urljoin(odoo.geturl(), '/web/tests?%s' % query)

    def test_odoo_qunit(self):
        sel, odoo_ver = self.sel, self.odoo_version

        def end_qunit_tests(browser):
            title = browser.title
            return (title.startswith(u'✔ ') or title.startswith(u'✖ '))

        if odoo_ver > 7:
            sel.get(self.get_login_url())
            sel.find_element_by_tag_name('html')
        module_attribute = 'module'
        if odoo_ver < 8:
            module_attribute = 'mod'

        for module in self.modules:
            sel.get(self.get_qunit_url(
                    module, module_attribute=module_attribute))
            WebDriverWait(self.sel, 60).until(end_qunit_tests)
            title = sel.title
            elt = sel.find_element_by_id('qunit-testresult')
            log.info("%s %s(%s) - %s - Module %s - %s",
                     sel.capabilities.get('platform', ''),
                     sel.capabilities.get('browserName', ''),
                     sel.capabilities.get('version', ''),
                     title, module, elt.text)
            message = elt.text + '\n'
            passed = title.startswith(u'✔ ')
            if not passed:
                sel.find_element_by_css_selector('#qunit-filter-pass').click()
                log.warning(self.driver.name)
                failed_elements = sel.find_elements_by_css_selector(
                    '#qunit-tests > li.fail')
                for elt in failed_elements:
                    log.warning(elt.text)
            self.assertTrue(passed, message)
