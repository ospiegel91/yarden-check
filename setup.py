import setuptools
import time
from pkg_resources import parse_requirements

with open("requirements.txt") as f:
    requirements = [str(r) for r in parse_requirements(f)]


setuptools.setup(
    name="multichecksum",
    version="0.0.1",
    author="Oren Spiegel",
    author_email="ospiegel51191@gmail.com",
    description="test",
    long_description=time.ctime(),
    long_description_content_type="text/markdown",
    packages=['multichecksum'],
    package_dir={'multichecksum': 'src'},

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={
        "multichecksum": [
            "*.py"
        ],
    },
    scripts=[],

    install_requires=requirements,

)
