import os
import slack_sdk

class SlackPoster:
    def __init__(self, slack_token, channel_id):
        self.client = slack_sdk.WebClient(token=slack_token)
        self.channel_id = channel_id

    def post_answers(self, answers):
        print(answers)
        for question, answer in answers.items():
            message = f"*{question}*\n-{answer}\n"
            self.client.chat_postMessage(channel=self.channel_id, text=message)