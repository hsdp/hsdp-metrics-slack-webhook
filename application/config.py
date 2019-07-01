import os
import sys
import json


class Config(object):

    DEBUG = True
    VCAP_SERVICES = json.loads(os.getenv('VCAP_SERVICES', '{}'))
    SLACK_WEBHOOK = os.getenv('SLACK_WEBHOOK','')

config = Config()
