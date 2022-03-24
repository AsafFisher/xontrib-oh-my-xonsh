#!/usr/bin/env python
import setuptools

try:
    with open('README.md', 'r', encoding='utf-8') as fh:
        long_description = fh.read()
except (IOError, OSError):
    long_description = ''

setuptools.setup(
    name='xontrib-oh-my-xonsh',
    version='0.0.1',
    license='MIT',
    author='Asaf Fisher',
    author_email='asaffisher@icloud.com',
    description="A shameless copy of oh-my-zsh",
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    install_requires=['xonsh'],
    packages=['xontrib'],
    package_dir={'xontrib': 'xontrib'},
    package_data={'xontrib': ['*.xsh']},
    platforms='any',
    url='https://github.com/AsafFisher/xontrib-oh-my-xonsh',
    project_urls={
        "Documentation": "https://github.com/AsafFisher/xontrib-oh-my-xonsh/blob/master/README.md",
        "Code": "https://github.com/AsafFisher/xontrib-oh-my-xonsh",
        "Issue tracker": "https://github.com/AsafFisher/xontrib-oh-my-xonsh/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: System :: Shells",
        "Topic :: System :: System Shells",
        "Topic :: Terminals",
    ]
)
