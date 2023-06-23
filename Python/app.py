from flask import Flask
import logging
from logstash_async.handler import AsynchronousLogstashHandler

app = Flask(__name__)

logger=logging.getLogger(f"app_logger")
logger.setLevel(logging.INFO)
logstash_formatter=logging.Formatter(fmt="%(name)s::%(levelname)s::%(message)s")
logstash_handler=AsynchronousLogstashHandler('0.0.0.0', 5000, database_path=None)
logstash_handler.setFormatter(logstash_formatter)
logger.addHandler(logstash_handler)


@app.route("/hello/<name>")
def say_hello(name):
  if len(name) <= 1:
    logger.warning(f"Too short name!")
    return "<h2>Your name is too short!<h2>"
  logger.info(f"Hello {name}")
  return f"<h2>Hello {name}!<h2>"

@app.route("/")
def app_info():
  logger.info("App running!")
  return f"<h1>App is running!<h1>"


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=5001)