from setuptools import setup, find_packages

setup(
    name='readyapi_play',
    version='1.1.0',
    packages=find_packages(),
    install_requires=[
        # Add your package dependencies here
    ],
    author='Md Sulaiman',
    description='This plugin provides an easy way to render a beautiful API reference based on a OpenAPI/Swagger file with ReadyAPI.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/readyapi/play',
    # classifiers=[
    # ],
)
