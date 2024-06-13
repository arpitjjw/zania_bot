import os
import sys
import json

from flask import Blueprint, request, current_app

'''current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, current_dir )

from document_processor import DocumentProcessor
from question_answer import QuestionAnswerer
from slack_poster import SlackPoster'''



bot_api_bp = Blueprint('bot_api_bp', __name__)
bot_api_bp.api_prefix = os.environ.get('API_PREFIX', "")

@bot_api_bp.route(bot_api_bp.api_prefix + "/query", methods=['POST'])
def query():
    inp = {}

    inp["user_questions"] = json.loads(request.form.get("user_questions")) # expected to be a list of strings
    inp["top_k"] = int(request.form.get("top_k", 3)) #top k documents for context
    
    '''slack_token = os.environ["SLACK_TOKEN"]
    channel_id = os.environ["SLACK_CHANNEL_ID"]
    openai_api_key = os.environ["OPENAI_API_KEY"]
    pdf_file_path = os.environ["PDF_FILE_PATH"]
    model_name = os.environ["OPENAI_MODEL_NAME"]'''
    
    '''questions = ["What is the name of the company?",
                "Who is the CEO of the company?",
                "What is their vacation policy?",
                "What is the termination policy?"]'''
                
    questions = inp["user_questions"]
    
    '''processor = DocumentProcessor(pdf_file_path)
    answerer = QuestionAnswerer(openai_api_key, model_name)
    poster = SlackPoster(slack_token, channel_id)'''
    
    document_text = current_app.processor.extract_text()
    answers = current_app.answerer.answer_questions(questions, document_text, inp["top_k"])
    current_app.poster.post_answers(answers)
    return answers