"""PytSite GeoIP Event Handlers.
"""
from datetime import datetime as _datetime, timedelta as _timedelta
from plugins import odm as _odm

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def cron_weekly():
    """'pytsite.cron.weekly' event handler.
    """
    # Delete expired entities
    f = _odm.find('geo_ip').lte('_created', _datetime.now() - _timedelta(weeks=1))
    for entity in f.get():
        try:
            entity.delete()
        except _odm.error.EntityDeleted:
            # Entity was deleted by another instance
            pass
