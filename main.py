
import json
import base64
import requests

def notify_slack(data, context):
	url = "" # Incoming Webhook URL
	notification_data = base64.b64decode(data['data']).decode('utf-8')
	data_json = json.loads(notification_data)
	cost_amount = data_json['costAmount']
	budget_amount = data_json['budgetAmount']
	currency_code = data_json['currencyCode']
	budget_notification_text = f'現在の利用額をお知らせ\n*予算*\n{budget_amount} {currency_code}\n*利用額*\n{cost_amount} {currency_code}'	
	requests.post(url, data=json.dumps({'text': budget_notification_text}))