===================
Selenium Odoo Qunit
===================

This is a CI launcher to run Odoo Qunit tests on multiple browsers at once using
selenium.

.. warning::

    This is not a lib to help you to write functional test in Odoo, it's intent
    is only to run Qunit tests page.


It's probably easier to set a config file

.. code-block::

    [nosetests]
    with-selenium = 1
    with-odoo-qunit = 1
    selenium-config = selenium.json
    processes = 4
    process-timeout = 120

with it's selenium config file

.. code-block::

    {
  "drivers": [
        {
          "class": "selenium_extra.drivers.local.Firefox"
        },
        {
          "class": "selenium_extra.drivers.remote.Grid",
          "command_executor": "http://127.0.0.1:4444/wd/hub",
          "capabilities": {
          },
          "request_drivers": [
            {
              "browserName": "firefox",
              "platform": "LINUX",
              "version": ""
            },
            {
              "browserName": "chrome",
              "platform": "LINUX",
              "version": ""
            }
          ]
        }
      ]
    }

TODO
====

Contribute
==========

.. note::

    As I'm not aware about Qunit standard, the qunit-interpreter may work on any
    qunit page but there are no warranty and I've no plan to maintain that
    today. If you want to contribute on this part of this PR will be wellcome.
