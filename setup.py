from setuptools import setup, find_packages

setup(
    name='argt',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'argt-echo=argt.echo:main',
            'argt-square=argt.square:main'
        ]
    },
    # Add other necessary package metadata
    author='Jie Deng',
    author_email='jie.deng28@example.com',
    description='A package containing command line tools for echoing and squaring numbers',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/neojie/argt',
    license='MIT',
    classifiers=[
        # Classifiers help users find your project
        # For a list of valid classifiers, see https://pypi.org/classifiers/
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        # Any required packages
    ],
)

