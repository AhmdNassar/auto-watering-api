from flask import Blueprint

blueprint = Blueprint(
    'home_blueprint',
    __name__,
    url_prefix='/dashboard/home/',
    template_folder='templates',
    static_folder='static'
)
