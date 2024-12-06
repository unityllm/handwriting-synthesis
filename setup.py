from setuptools import setup, find_packages

# Read the dependencies from requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='handwriting-synthesis',
    version='0.1.0',
    author='sjvasquez',
    description='A package for handwriting synthesis using recurrent neural networks.',
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'handwriting-synthesis-cli=cli:main',
        ],
    },
)