import requests
from flask import request, jsonify, Blueprint, current_app


webhook_proxy = Blueprint('wehhook_proxy', __name__)


@webhook_proxy.route('/healthcheck')
def healthcheck():
    return jsonify({})


@webhook_proxy.route('/800e8022-9994-497e-a808-0f0043e8c129', methods=['POST'])
def hook_to_hook():
    slack_webhook = current_app.config['SLACK_WEBHOOK']
    for alert in request.json['alerts']:
        message = []
        message.append(' '.join(['alert name:', alert['labels']['alertname']]))
        message.append(' '.join(['service instance name:', alert['labels']['hsdp_instance_name']]))
        message.append(' '.join(['severity:', alert['labels']['severity']]))
        message.append(' '.join(['status:', alert['status']]))
        message.append(' '.join(['description:', alert['annotations']['description']]))
        message.append(' '.join(['summary:', alert['annotations']['summary']]))
        slack_payload = {'text': '\n'.join(message)}
        response = requests.post(slack_webhook, json=slack_payload)
        if not response.ok:
            response.raise_for_status()
    return jsonify({})
