#Import the necessary libraries:

import requests
import json

#Set the required parameters, including the payment amount, the Merchant ID, and the terminal ID:

amount = 1000 # The payment amount in Iranian Rials
merchant_id = 'your_merchant_id'
terminal_id = 'your_terminal_id'
callback_url = 'http://your_callback_url'

#Create a dictionary containing the payment details:


payment_data = {
    'terminalId': terminal_id,
    'userName': 'your_username',
    'userPassword': 'your_password',
    'orderId': '123456', # A unique identifier for the payment transaction
    'amount': amount,
    'localDate': '20220224', # The local date in the format of YYYYMMDD
    'localTime': '151920', # The local time in the format of HHMMSS
    'additionalData': '',
    'callBackUrl': callback_url,
    'payerId': '0',
    'payerContact': '09121234567',
    'secureCode': '',
    'signature': ''
}

#Create a function to generate the signature for the payment data:

def generate_signature(terminal_id, merchant_id, order_id, amount, local_date, local_time):
    data = f'{terminal_id};{merchant_id};{order_id};{amount};{local_date};{local_time}'
    signature = hashlib.sha1(data.encode('utf-8')).hexdigest()
    return signature

#Generate the signature using the function created in step 4 and add it to the payment data:

payment_data['signature'] = generate_signature(terminal_id, merchant_id, payment_data['orderId'], amount, payment_data['localDate'], payment_data['localTime'])

#Send a POST request to the ns1 payment gateway with the payment data:

url = 'https://sadad.shaparak.ir/VPG/api/v0/Request/PaymentRequest'
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
response = requests.post(url, data=json.dumps(payment_data), headers=headers)

#Parse the response and extract the payment gateway URL to redirect the user to complete the payment:

response_data = json.loads(response.text)
if response_data['ResCode'] == '0':
    payment_gateway_url = response_data['PaymentGateway']
    # Redirect the user to the payment gateway URL to complete the payment

#Note that you need to replace the values for merchant_id, terminal_id, callback_url, userName, and userPassword with your own credentials. 
#Also, make sure to handle any errors and exceptions that may occur during the payment process.



