"""Python setup.py for webling_calendar package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("webling_calendar", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="webling_calendar",
    version=read("webling_calendar", "VERSION"),
    description="Awesome webling_calendar created by dimschlukas",
    url="https://github.com/dimschlukas/webling-calendar/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="dimschlukas",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["webling_calendar = webling_calendar.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
