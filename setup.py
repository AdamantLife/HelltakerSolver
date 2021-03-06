import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="HelltakerSolver",
    version="0.0.1",
    author="AdamantLife",
    author_email="",
    description="Helltaker map solver. Currently only features a basic Brute Force algorithm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        "click",
        "helltaker @ git+https://github.com/AdamantLife/Helltaker",
        ],
    entry_points = {
        'console_scripts': [
            "HelltakerSolver=HelltakerSolver.cli:run"
        ]
    }
)