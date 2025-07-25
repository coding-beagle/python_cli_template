from setuptools import setup

setup(
    name="Module",
    version="0.1",
    description="A sample Python package",
    author="coding-beagle",
    author_email="nicholasp.teague@gmail.com",
    packages=["Module"],
    install_requires=["Click"],
    entry_points="""
        [console_scripts]
        module=module.__main__:cli
    """,
)
