from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='repotext',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A tool to pack repositories into AI-friendly files',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/repotext",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click>=8.0.3',
    ],
    entry_points={
        'console_scripts': [
            'repotext=repotext.__main__:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)