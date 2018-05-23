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
        return requests.get(f"http://35.178.109.215/name2hash/{urllib.parse.quote(name)}").text

    def hash_to_name(arg, hash):
        return urllib.parse.unquote(requests.get(f"http://35.178.109.215/hash2name/{hash}").text)


class N1AnalyticsClient(object):
    def __init__(self):
        super(N1AnalyticsClient, self).__init__()

    def get_bank_runs(self):
        url = "http://dataconnector.n1analytics.com:8000/v1/graphs/bankA-test/runs"
        payload = {
          "typ": "http://schema.n1analytics.com/envelope/1",
          "pyl": {
            "@context": "https://schema.n1analytics.com/aml/1/investigationRequest",
            "targetID": "bfb65c5925abc06df4e88d4e919d91bcf07bed093bad1726be8ef9cd302420d0",
            "threshold": 3
          }
        }

        response = requests.post(url, json=payload)
        while response.json()["info"]["status"] == "RUNNING":
            logger.debug(response.json()["info"]["status"])
            response = requests.post(url, json=payload)

        return JsonResponse(response.json())


# Create your views here.
def index(request):
    client = N1AnalyticsClient()
    return client.get_bank_runs()
