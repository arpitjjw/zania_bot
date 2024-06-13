import os
import json

from flask import Blueprint, request, current_app


bot_api_bp = Blueprint('bot_api_bp', __name__)
bot_api_bp.api_prefix = os.environ.get('API_PREFIX', "")

@bot_api_bp.route(bot_api_bp.api_prefix + "/query", methods=['POST'])
def query():
    inp = {}

    inp["user_questions"] = json.loads(request.form.get("user_questions")) # expected to be a list of strings
    inp["top_k"] = int(request.form.get("top_k", 3)) #top k documents for context
    
                
    questions = inp["user_questions"]
    
  
    
    document_text = current_app.processor.extract_text()
    answers = current_app.answerer.answer_questions(questions, document_text, inp["top_k"])
    current_app.poster.post_answers(answers)
    return answers