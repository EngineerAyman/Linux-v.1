'''
*********************************************
 * Author:          AYMAN HARRAZ
 * Creation Data:   3 MAY, 2023
 * Version:         v1.0
 ********************************************
Assignment 1:
This program for Auto Post using python code to SLAC
'''

import requests
import json

def send_slack_message(payload, webhook):
    """Send a Slack message to a channel via a webhook. 
    
    Args:
        payload (dict): Dictionary containing Slack message, i.e. {"text": "This is a test"}
        webhook (str): Full Slack webhook URL for your chosen channel. 
    
    Returns:
        HTTP response code, i.e. <Response [503]>
    """

    return requests.post(webhook, json.dumps(payload))

webhook = "https://hooks.slack.com/services/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"
payload = {"text": "Hello, This is Ayman"}
send_slack_message(payload,webhook)


