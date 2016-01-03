from setuptools import setup

setup(
    name='selenium-odoo-qunit',
    description='Odoo Qunit launcher',
    long_description=open('README.rst').read(),
    author='Pierre Verkest',
    author_email='pverkest@anybox.fr',
    url='https://github.com/petrus-v/selenium-odoo-qunit',
    packages=[
        'selenium_odoo_qunit',
        'selenium_odoo_qunit.nose_plugins'
    ],
    install_requires=[
        'anybox_nose_selenium',
    ],
    dependency_links=[
        'git+https://github.com/petrus-v/anybox_nose_selenium.git@master#'
        'egg=anybox_nose_selenium',
    ],
    entry_points={
        'console_scripts': [
            'soq = selenium_odoo_qunit.selenium_odoo_qunit:main',
        ],
        'nose.plugins.0.10': [
            'odoo-qunit=selenium_odoo_qunit.nose_plugins.odoo_qunit:OdooQunit'
        ]
    },
    license='Mozilla Public License 2.0 (MPL 2.0)',
    keywords='nose selenium CI Odoo OpenERP QUnit',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7']
)
