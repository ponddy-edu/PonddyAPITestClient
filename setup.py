from setuptools import setup


setup(
    name='ponddy-api-test-client',
    version='0.0.1',
    description='The test client for Ponddy API',
    long_description='',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    python_requires='>3.6',
    keywords='django api client ponddy',
    url='https://github.com/ponddy-edu/PonddyAPITestClient',
    author='lambdaTW',
    author_email='lambda@lambda.tw',
    license='MIT',
    packages=['ponddy_api_test_client'],
    install_requires=[
        'Django',
    ],
    zip_safe=False
)
