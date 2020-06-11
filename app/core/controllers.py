from flask import Blueprint, render_template, request

import core.service as core_service

routes = Blueprint('core', __name__)


@routes.route('/')
def index():
    counter = None
    counter_name = request.args.get('counter_name', None)

    if counter_name:
        counter_name = str(counter_name)
        counter = core_service.get_or_create_counter(counter_name)
        counter = core_service.increment_counter(counter)

    return render_template('index.html', counter=counter)
