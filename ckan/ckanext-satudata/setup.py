from setuptools import setup, find_packages

setup(
    name='ckanext-satudata',
    version='1.0.0',
    description='Custom theme for Satu Data Kabupaten Konawe',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'ckanext.satudata': [
            'templates/*.html',
            'templates/**/*.html',
            'templates/**/**/*.html',
            'public/css/*.css',
            'public/images/*',
        ],
    },
    entry_points={
        'ckan.plugins': [
            'satudata=ckanext.satudata.plugin:SatuDataPlugin',
        ],
    },
)
