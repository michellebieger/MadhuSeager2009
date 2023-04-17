import setuptools
from setuptools import find_packages
from numpy.distutils.core import setup
from numpy.distutils.core import Extension
from numpy.distutils import log
import re, os

packages = find_packages(exclude=('tests', 'doc'))
provides = ['taurex_MadhuSeager2018', ]
requires = []

install_requires = ['taurex']    
entry_points = {'taurex.plugins': 'taurex_MadhuSeager2018 = taurex_MadhuSeager2018'}

 setup(name='taurex_randomtp',
	author="M. F. Bieger",
	author_email="michellebieger@live.com",
        license="BSD",
        description='A replication of the temperature-pressure profile from the publication of Madhusudhan and Seager 2018, arXiv:0910.147v2',
        packages=packages,
        entry_points=entry_points,
        provides=provides,
        requires=requires,
        install_requires=install_requires) 
