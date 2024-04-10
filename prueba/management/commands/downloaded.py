import requests
from prueba.convert import converter
from django.core.management.base import BaseCommand
from prueba.models import Feature

class Command(BaseCommand):
    help = 'Fetch and store earthquake data'

    
    def handle(self, *args, **kwargs):
        url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson'
        response = requests.get(url)
        data = response.json()

        for feature in data['features']:
            external_id = feature['id']
            properties = feature['properties']
            geometry = feature['geometry']
            
            Feature.objects.update_or_create(
                external_id=external_id,
                defaults={
                    "external_id": external_id,
                    "type": feature["type"],
                    'magnitude': properties.get('mag'),
                    'place': properties.get('place'),
                    'time': converter(properties.get('time')),
                    'external_url': properties.get('url'),
                    'tsunami': properties.get('tsunami', False),
                    'mag_type': properties.get('magType'),
                    'title': properties.get('title'),
                    'longitude': geometry['coordinates'][0],
                    'latitude': geometry['coordinates'][1],
                }
            )
