import requests
from flask import request, jsonify, Blueprint, current_app


webhook_proxy = Blueprint('wehhook_proxy', __name__)


@webhook_proxy.route('/healthcheck')
def healthcheck():
    return jsonify({})


@webhook_proxy.route('/aa14d002-cfc2-4a83-8ea4-25d8a7be2a8e', methods=['POST'])
def hook_to_hook():
    slack_webhook = current_app.config['SLACK_WEBHOOK']
    for alert in request.json['alerts']:
        message = []
        message.append(' '.join(['*Alert name:*', alert['labels']['alertname']]))
        message.append(' '.join(['*Service instance name:*', alert['labels']['application']]))
        message.append(' '.join(['*Severity:*', alert['labels']['severity']]))
        message.append(' '.join(['*Status:*', alert['status']]))
        message.append(' '.join(['*Description:*', alert['annotations']['description']]))
        message.append(' '.join(['*Summary:*', alert['annotations']['summary']]))
        slack_payload = {'text': '\n'.join(message)}
        response = requests.post(slack_webhook, json=slack_payload)
        if not response.ok:
            response.raise_for_status()
    return jsonify({})
