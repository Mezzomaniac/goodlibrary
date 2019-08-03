from flask import Flask
from goodlibrary.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from goodlibrary import routes
