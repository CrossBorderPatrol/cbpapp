import json
import logging
import urllib

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

import requests


logger = logging.getLogger(__name__)


class HashedNameServiceClient(object):
    def __init__(self):
        super(HashedNameServiceClient, self).__init__()

    def name_to_hash(self, name):
        return requests.get(f"http://35.178.109.215:5000/name2hash/{urllib.parse.quote(name)}").text

    def hash_to_name(arg, hash):
        return urllib.parse.unquote(requests.get(f"http://35.178.109.215:5000/hash2name/{hash}").text)

    def hash_to_info(arg, hash):
        return urllib.parse.unquote(requests.get(f"http://35.178.109.215:5000/hash2info/{hash}").text)


class N1AnalyticsClient(object):
    def __init__(self):
        super(N1AnalyticsClient, self).__init__()

    def get_bank_runs(self, hash):
        url = "http://35.178.21.231/v1/graphs/bank-200/runs"
        payload = {
          "typ": "http://schema.n1analytics.com/envelope/1",
          "pyl": {
            "@context": "https://schema.n1analytics.com/aml/1/investigationRequest",
            #"targetID": "4fd7584814066639ceaaaeacfc836abe06e806bb6238489e86846600ba9b0ce0",
            "targetID": hash,
            "threshold": 3
          }
        }

        try:
            #raise Exception()

            response = requests.post(url, json=payload)
            url = response.json()['@id']

            response = requests.get(url)

            while response.json()["info"]["status"] == "RUNNING":
                logger.debug(response.json()["info"]["status"])
                response = requests.get(url)
        except:
            with open('core/fake.json', 'rb') as f:
                data = json.loads(f.read())

            return data

        return response.json()


# Create your views here.
def index(request):
    client = N1AnalyticsClient()
    return client.get_bank_runs()
