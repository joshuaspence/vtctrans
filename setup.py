from setuptools import setup

setup(
    name='vtctrans',
    version='0.1.0',
    description='Re-format tool for varnishtest',
    packages=['vtctrans'],
    install_requires=[
        'simplejson',
        'gevent >= 1.0.2, <2.0',
        'boto >=2.0.0, <3.0.0',
        'pyyaml >=3.10, <4.0'
    ],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'vtctrans = vtctrans:main',
        ],
    },
)
