import eventlet
eventlet.monkey_patch()
from src.init import initialize_kevin
initialize_kevin()


from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from src.socket_instance import socketio, emit_agent
import os
import logging
from threading import Thread
import tiktoken

from src.apis import project_bp
from src.config import Config
from src.logger import Logger, route_logger
from src.project import ProjectManager
from src.state import AgentState
from src.agents import Agent
from src.llm import LLM

app = Flask(__name__)
CORS(app)
app.register_blueprint(project_bp)
socketio.init_app(app)


log = logging.getLogger("werkzeug")
log.disabled = True


TIKTOKEN_ENC = tiktoken.get_encoding("cl100k_base")

os.environ["TOKENIZERS_PARALLELISM"] = "false"

manager = ProjectManager()
AgentState = AgentState()
config = Config()
logger = Logger()

@socketio.on('socket_connect')
def test_connect(data):
    print("Socket connected :: ", data)
    emit_agent("socket_response", {"data": "Server Connected"})

@app.route("/api/data", methods=["GET"])
@route_logger(logger)
def data():
    project = manager.get_project_list()
    models = LLM().list_models()
    search_engines = ["Bing", "Google", "DuckDuckGo"]
    return jsonify({"projects": project, "models": models, "search_engines": search_engines})