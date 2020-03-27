from setuptools import setup

setup(
    name='gpg_viz',
    version='1.0.0',
    description='Visualizing library for GPG web of trust',
    author='Olivier van der Toorn',
    author_email='oliviervdtoorn@gmail.com',
    packages=['gpg_viz'],
    install_requires=['matplotlib', 'networkx', 'pygraphviz'],
)
