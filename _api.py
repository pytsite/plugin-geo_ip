"""PytSite Geo IP API Functions
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

import requests as _requests
import re as _re
from pytsite import cache as _cache
from . import _error, _model

_private_ip_re = _re.compile('(127\.|10\.|172\.(16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31|32)|192\.168\.)')
_cache_pool = _cache.create_pool('geo_ip')

# external_api_field: our_field
_field_mapping = {
    'as': 'asn',
    'city': 'city',
    'country': 'country',
    'countryCode': 'country_code',
    'isp': 'isp',
    'lat': 'latitude',
    'lon': 'longitude',
    'org': 'organization',
    'region': 'region',
    'regionName': 'region_name',
    'timezone': 'timezone',
}


def resolve(ip: str) -> _model.GeoIP:
    """Get data about an IP address
    """
    try:
        return _model.GeoIP(_cache_pool.get(ip))

    except _cache.error.KeyNotExist:
        r = {}

        if ip == '0.0.0.0' or _private_ip_re.match(ip):
            return _model.GeoIP(r)

        resp = _requests.get('http://ip-api.com/json/{}'.format(ip))

        if resp.status_code != 200:
            raise _error.ResolveError(resp.text)

        for ext_api_f, val in resp.json().items():
            if ext_api_f in _field_mapping:
                r[_field_mapping[ext_api_f]] = val

        return _model.GeoIP(_cache_pool.put(ip, r))
