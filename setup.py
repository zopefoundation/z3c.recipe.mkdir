from setuptools import setup, find_packages
import os

version = '0.5.1dev'

with open("README.rst") as f:
    README = f.read()

with open(os.path.join("z3c", "recipe", "mkdir", "README.rst")) as f:
    DETAILED = f.read()

with open("CHANGES.rst") as f:
    CHANGES = f.read()

setup(name='z3c.recipe.mkdir',
      version=version,
      description="Buildout recipe to create directories.",
      long_description=README + "\n\n" + DETAILED + "\n\n" + CHANGES,
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Buildout",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2 :: 2.6",
        "Programming Language :: Python :: 2 :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Zope Public License",
        ],
      keywords='buildout directory folder mkdir',
      author='Uli Fouquet',
      author_email='grok-dev@zope.org',
      url='http://pypi.python.org/pypi/z3c.recipe.mkdir',
      license='ZPL 2.1',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['z3c', 'z3c.recipe' ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zc.buildout >= 1.5',
      ],
      extras_require=dict(
        test = [
            'zope.testing',
            ]
        ),
      entry_points="""
      [zc.buildout]
      default = z3c.recipe.mkdir:Recipe
      """,
      )
