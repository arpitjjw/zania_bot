import os
import logging

from flask import Flask, jsonify
from src.bot_api import bot_api_bp

from src.document_processor import DocumentProcessor
from src.question_answer import QuestionAnswerer
from src.slack_poster import SlackPoster

app = Flask(__name__)

with app.app_context():
    slack_token = os.environ["SLACK_TOKEN"]
    channel_id = os.environ["SLACK_CHANNEL_ID"]
    openai_api_key = os.environ["OPENAI_API_KEY"]
    pdf_file_path = os.environ["PDF_FILE_PATH"]
    model_name = os.environ["OPENAI_MODEL_NAME"]
    
    app.processor = DocumentProcessor(pdf_file_path)
    app.answerer = QuestionAnswerer(openai_api_key, model_name)
    app.poster = SlackPoster(slack_token, channel_id)
    
@app.route(os.environ.get('API_PREFIX', "") + '/health', methods=['GET'])
def health_check():
    return jsonify({"state": "OK"}), 200

app.register_blueprint(bot_api_bp)

if __name__ == "__main__":
    app.run()