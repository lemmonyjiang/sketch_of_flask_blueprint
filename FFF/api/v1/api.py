from flask import Blueprint

bp = Blueprint('api', __name__)


@bp.route('/')
def index():
    return 'FFF v1'
