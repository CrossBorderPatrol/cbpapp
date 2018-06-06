import json
import logging
import urllib
from operator import itemgetter

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

import requests

logger = logging.getLogger(__name__)

class HashedNameServiceClient(object):
    def __init__(self):
        super(HashedNameServiceClient, self).__init__()

    def name_to_hash(self, name):
        return requests.get(f"https://cbp-id-provider.herokuapp.com/name2hash/{urllib.parse.quote(name)}").text

    def hash_to_name(arg, hash):
        return urllib.parse.unquote(requests.get(f"https://cbp-id-provider.herokuapp.com/hash2name/{hash}").text)

    def hash_to_info(arg, hash):
        return urllib.parse.unquote(requests.get(f"https://cbp-id-provider.herokuapp.com/hash2info/{hash}").text)


class N1AnalyticsClient(object):
    def __init__(self):
        super(N1AnalyticsClient, self).__init__()

    def get_bank_runs(self, hash, threshold=10):
        url = "https://cbp-engine.herokuapp.com/v1/graphs/bank-200/runs"
        payload = {
          "typ": "http://schema.n1analytics.com/envelope/1",
          "pyl": {
            "@context": "https://schema.n1analytics.com/aml/1/investigationRequest",
            "targetID": hash, # 4fd7584814066639ceaaaeacfc836abe06e806bb6238489e86846600ba9b0ce0
            "threshold": threshold,
          }
        }

        logger.error('hash: ' + hash)
        logger.error('url: ' + url)
        logger.error('payload: ' + json.dumps(payload))

        try:
            logger.error('Sending POST ...')
            response = requests.post(url, json=payload)
            logger.error('POST response: ' + json.dumps(response.json()))

            url = response.json()['@id']
            response = requests.get(url)

            while response.json()["info"]["status"] == "RUNNING":
                logger.error('waiting...')
                logger.debug(response.json()["info"]["status"])
                response = requests.get(url)

            logger.error('GET response: ' + json.dumps(response.json()))

            j = response.json()

            activities = j['res']['receivers']['activities']
            newlist = sorted(activities, key=itemgetter('c'), reverse=True) 

            logger.error(type(newlist))
            logger.error(json.dumps(newlist))

            j['res']['receivers']['activities'] = newlist

            return j

        except Exception as e:
            logger.error(e)
            logger.error('Something went wrong, using fake data ...')

            with open('core/fake.json', 'rb') as f:
                data = json.loads(f.read())

            return data

        return response.json()


# Create your views here.
def index(request):
    client = N1AnalyticsClient()
    return client.get_bank_runs()
