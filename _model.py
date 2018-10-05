"""PytSite GeoIP plugin Data Models
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class GeoIP:
    def __init__(self, data: dict):
        self._asn = data.get('asn')
        self._city = data.get('city')
        self._country = data.get('country')
        self._country_code = data.get('country_code')
        self._isp = data.get('isp')
        self._latitude = data.get('latitude', 0.0)
        self._longitude = data.get('longitude', 0.0)
        self._organization = data.get('organization')
        self._region = data.get('region')
        self._region_name = data.get('region_name')
        self._timezone = data.get('timezone', 'UTC')

    @property
    def asn(self) -> str:
        return self._asn

    @property
    def city(self) -> str:
        return self._city

    @property
    def country(self) -> str:
        return self._country

    @property
    def country_code(self) -> str:
        return self._country_code

    @property
    def isp(self) -> str:
        return self._isp

    @property
    def latitude(self) -> float:
        return self._latitude

    @property
    def longitude(self) -> float:
        return self._longitude

    @property
    def organization(self) -> str:
        return self._organization

    @property
    def region(self) -> str:
        return self._region

    @property
    def region_name(self) -> str:
        return self._region_name

    @property
    def timezone(self) -> str:
        return self._timezone
