import setuptools

setuptools.setup(
    name="tasko", 
    version="0.0.1",
    author="warriorofwire",
    description="Tasko package",
    packages=setuptools.find_packages(include=['tasko']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
