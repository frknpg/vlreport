import os

from flask import Flask

from flaskr.report.report_controller import ReportController


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    report_handler = ReportController(app)
    report_handler.listen()

    return app