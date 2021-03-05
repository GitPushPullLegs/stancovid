import json
from json import JSONDecodeError
from urllib.parse import urljoin

import requests


class Client:
    _HOST = r"https://gis2.stancounty.com/arcgis/rest/services/"
    _HEADERS = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

    def __init__(self):
        self.session = requests.session()
        self.session.headers.update(self._HEADERS)

    def get_latest_data(self):
        """Returns the latest COVID data."""
        url = urljoin(self._HOST, r"COVID19_POS_CASE_Layer2/FeatureServer/0/query")
        params = dict(f='json',
                      where='1=1',
                      returnGeometry=False,
                      spatialRel='esriSpatialRelIntersects',
                      outFields="*",
                      orderByFields="id desc",
                      outSR=102100,
                      resultOffset=0,
                      resultRecordCount=1,
                      resultType="Standard")
        response = self.session.get(url, params=params)
        return self._safe_json(response.content)['features'][0]['attributes']

    def get_by_zipcode(self):
        """Returns a list of dicts detailing the COVID data by zip code."""
        url = urljoin(self._HOST, r"Hosted/COVID19_By_ZipCodes/FeatureServer/0/query")
        params = dict(f='json',
                      returnGeometry=False,
                      spatialRel='esriSpatialRelIntersects',
                      geometry=json.dumps(dict(xmin=-13462700.917811539,
                                               ymin=4383204.949985651,
                                               xmax=-13149614.849955473,
                                               ymax=4696291.017841717,
                                               spatialReference=dict(wkid=102100))),
                      geometryType='esriGeometryEnvelope',
                      inSR=102100,
                      outFields="*",
                      outSR=102100,
                      resultType="tile")
        response = self.session.get(url, params=params)
        return [datum['attributes'] for datum in self._safe_json(response.content)['features']]

    def _safe_json(self, data):
        try:
            return json.loads(data)
        except JSONDecodeError:
            return {}
