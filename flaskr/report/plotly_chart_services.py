import os
import uuid

import plotly.graph_objects as go


class PlotlyChartService:
    def __init__(self):
        if not os.path.exists("images"):
            os.mkdir("images")
        super().__init__()

    def save_throuhput_chart_image(self, virtual_users_by_interval, requests_by_interval, date_labels):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=date_labels, y=virtual_users_by_interval, fill='tozeroy'))
        fig.add_trace(go.Scatter(x=date_labels, y=requests_by_interval, fill='tonexty'))
        image_name = '{}.png'.format(uuid.uuid4())
        fig.write_image("images/{}".format(image_name))

        return image_name
