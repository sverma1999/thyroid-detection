from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """Reads requirements.txt file and returns a list of required packages"""
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [r.replace("\n", "") for r in requirements]

        # Remove -e . from requirements
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name="thyroid-detection",
    version="0.0.1",
    author="Shubham",
    author_email="vshubhamkam05@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
