import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
#import logging
#logging.basicConfig(level=logging.DEBUG)


slack_token = os.environ["SLACK_BOT_TOKEN"]
client = WebClient(token=slack_token)
script = (os.popen("sh test.sh").read())

try:
    response = client.chat_postMessage(
        channel="testing",
        text=script

    )
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["error"]

