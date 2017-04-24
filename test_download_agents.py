from program.download_agents import *

import urllib.error
import urllib.request

def test_http_return(monkeypatch):
    dictionary = [{
            "age": 84,
            "agreeableness": 0.7413407664115031,
            "conscientiousness": -1.1249747587681012,
            "country_name": "Mexico",
            "country_tld": "mx",
            "date_of_birth": "1933-08-01",
            "extraversion": 0.7658659053502607,
            "id": 4292118096,
            "id_str": "OnS-Uo",
            "income": 16405,
            "internet": 'false',
            "language": "Spanish",
            "latitude": 24.070169151659698,
            "longitude": -100.89312355431782,
            "neuroticism": -0.3989004017999598,
            "openness": 0.7907731119904722,
            "religion": "Roman Catholic",
            "sex": "Female"
          }
        ]
    def mockreturn(request):
        return dictionary
    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    response = urllib.request.urlopen("http://pplapi.com/batch/{}/sample.json".format(1))
    assert response == dictionary