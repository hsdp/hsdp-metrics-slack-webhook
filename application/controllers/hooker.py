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
        message = []
        message.append('*Application name:*\n')
        message.append(alert['labels']['application'] + '\n' + '\n')
        message.append('*Status:*\n')
        message.append(alert['status'] + '\n' + '\n')
        message.append('*Message:*\n')
        message.append( alert['annotations']['description'])
        slack_payload = {'text': '\n'.join(message)}
        response = requests.post(slack_webhook, json=slack_payload)
        if not response.ok:
            response.raise_for_status()
    return jsonify({})
