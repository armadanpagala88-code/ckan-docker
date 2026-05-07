from setuptools import setup, find_packages

setup(
    name='ckanext-konawe',
    version='0.1',
    description='Satu Data Konawe Theme',
    license='AGPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.konawe'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    entry_points='''
        [ckan.plugins]
        konawe=ckanext.konawe.plugin:KonawePlugin
    ''',
)
