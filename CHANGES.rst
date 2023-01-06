Changes
*******

1.0 (2023-01-06)
================

- Drop support for Python 2.7, 3.4. 3.5, 3.6.

- Add support for Python 3.8, 3.9, 3.10, 3.11.


0.7 (2018-11-16)
================

- Add support for Python 3.4, 3.5, 3.6, 3.7, PyPy and PyPy3.

- Drop support for Python 2.6, 3.2 and 3.3.


0.6 (2013-05-21)
================

- Dropped support for deprecated ``path`` option (use ``paths`` instead).

- Added support for Python 3.2 / 3.3.

- Added ``setup.py docs`` alias:  runs ``setup.py develop`` and then installs
  documentation dependencies.

- Added ``setup.py dev`` alias:  runs ``setup.py develop`` and then installs
  testing dependencies.

- Updated docs and tests.

0.5 (2012-06-26)
==================

- Added support for ``create-intermediate`` option (``yes`` by default).

- Fixed bug: empty directory names were not excluded from ``paths``.

0.4 (2012-06-24)
================

- Added support for ``mode``, ``user``, and ``group`` options.

- Fixed (unnoticed?) bug when using the deprecated ``path`` option. In
  that case the default path (``parts/<sectionname>``) was created
  instead of the given one.

- Shortened main code.

- Updated tests to run with ``zc.buildout`` 1.5, thus requiring at least this
  version.

- Using python's ``doctest`` module instead of depreacted
  ``zope.testing.doctest``.


0.3.1 (2009-08-21)
==================

- Update options ``path`` and ``paths`` to be referencable.

- Output ``created`` message only if a directory was really created
  but display this message also for intermediate directories.

0.3 (2009-08-20)
================

- Renamed ``path`` option to ``paths`` (plural). Please do not use
  ``path`` anymore!

- Created directories are now displayed during buildout runs.

- Changed default behaviour: directories created once will not be
  removed on updates, except you require that explicitly.

- Added new option ``remove-on-update``: if set to ``yes``, ``true``
  or ``on`` the set directories will be removed on updates of
  ``buildout`` configuration.


0.2 (2009-08-19)
================

- Make paths absolute and normalize them before creation.

- Support creation of several paths in a row.

- Added check whether a file exists as part of path and emit error.


0.1 (2009-08-17)
================

- Initial release.
