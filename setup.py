from setuptools import setup, find_packages

config = {
    'description': 'FIWARE Context Broker instance integration with the BDTI',
    'author': 'CEF Digital',
    'url': 'https://github.com/ConnectingEurope/ContextBroker-BDTI',
    'version': '1.0',
    'install_requires': ['Click', 'requests', 'paramiko', 'configobj'],
    'packages': find_packages(exclude=['ez_setup', 'tests', 'tests.*']),
    'package_data': {'': ['agent_hdfs.conf','logger.yml', 'template.ini', 'internal_conf.ini']},
	'include_package_data': True,
    'py_modules': ['cb_bdti'],
    'name': 'cb-bdti',
	'entry_points': '''
	[console_scripts]
	cb-bdti=cb_bdti.commands:cli
	'''
}

# Add in any extra build steps for cython, etc.
setup(**config)