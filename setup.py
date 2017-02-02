from setuptools import setup

setup(
    name='vtctrans',
    version='0.1.1',
    description='Re-format tool for varnishtest',
    packages=['vtctrans'],
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'vtctrans = vtctrans:main',
        ],
    },
)
