from setuptools import setup, find_packages
from plunder.__version__ import __version__


setup(
    name="plunder",
    author="James Campbell",
    author_email="james@jamescampbell.us",
    version=__version__,
    license="MIT",
    description="My crime is that of curiosity.  My crime is that of judging people by what they say and think, not what they look like. My crime is that of outsmarting you, something that you will never forgive me for.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=["plunder"],
    py_modules=["plunder"],
    keywords=["pirates", "gold", "search-tools", "list-maker", "web-scraping"],
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=["beautifulsoup4", "google"],
    entry_points={"console_scripts": ["plunder = plunder.plunder:main"]},
    url="https://github.com/jamesacampbell/plunder",
    download_url="https://github.com/jamesacampbell/plunder/archive/{}.tar.gz".format(
        __version__
    ),
)
