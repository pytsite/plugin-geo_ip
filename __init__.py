"""PytSite Geo IP
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import plugman as _plugman

# Public API
if _plugman.is_installed(__name__):
    from . import _error as error
    from ._api import resolve
