from urllib import parse

import requests

from .base import BaseCrawler


class FareEstimate(BaseCrawler):

    def get_ref_address(self, address):
        url = 'https://www.uber.com/api/autocomplete-address?latitude=-15.774128271247498&longitude=-47.74372673034998&\
query=' + parse.quote(address)
        response = requests.get(url, headers=self.headers())

        options = []
        if response.status_code == 200:
            json = response.json()
            if json:
                if len(json) == 1:
                    item = json[0]
                    options = [{'title': item['title'], 'reference': item['reference']}]
                else:
                    options = [{'title': item['title'], 'reference': item['reference']} for item in json]

        return options

    def get_prices(self, pickup, destination):
        pickupRef = pickup['reference']
        destinationRef = destination['reference']

        url = f'https://www.uber.com/api/fare-estimate?pickupRef={pickupRef}&pickupRefType=&pickupLat=&pickupLng=\
&destinationRef={destinationRef}&destinationRefType=google_places'

        response = requests.get(url, headers=self.headers())

        values = []
        if response.status_code == 200:
            json = response.json()
            for price in json['prices']:
                vehicle = price['vehicleViewDisplayName']
                value = price['fareString']
                base = price['fare']['base']
                cancellation = price['fare']['cancellation']

                value = value.split('-')
                min_value = f'{value[0]}.00'
                max_value = f'{value[0][0:2]}{value[1]}.00'
                values.append({
                    'vehicle': vehicle,
                    'value': [min_value, max_value],
                    'base': base,
                    'cancellation': cancellation
                })

        return values
