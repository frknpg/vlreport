import jsonpickle
from flask import Response
from flask import request
from flask_cors import CORS

from flaskr.report.report_file_service import ReportFileService


class ReportController:
    def __init__(self, app):
        self.app = app
        self.report_file_service = ReportFileService()
        super().__init__()

    def listen(self):
        CORS(self.app)

        @self.app.route('/api/ping')
        def ping():
            return 'pong'

        @self.app.route('/api/create-report', methods=['POST'])
        def create_report():
            report_data = request.get_json()
            self.report_file_service.create_file(report_data)
            return Response(jsonpickle.encode(report_data), mimetype='application/json')
