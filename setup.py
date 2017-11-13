from setuptools import setup

setup(
    name='docker-deployment-example',
    version='0.1',
    packages=['docker_deployment_example'],
    url='https://github.com/FlorisHoogenboom/docker-deployment-example',
    license='',
    author='Floris Hoogenboom',
    author_email='floris.hoogenboom@futurefacts.nl',
    description='A sample python project that automatically deploys a ML learning model.',
    install_requires=[
        'scipy',
        'scikit-learn',
        'numpy',
        'pandas'
    ],
    tests_require=[
        'nose'
    ],
    test_suite='nose.collector'
)
