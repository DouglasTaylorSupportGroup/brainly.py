import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="brainly",
    version="0.1.0",
    author="jckli",
    description="A parsing library for brainly.com written in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DouglasTaylorSupportGroup/brainly.py",
    packages=setuptools.find_packages(),
    install_requires=["requests", "beautifulsoup4"],
)