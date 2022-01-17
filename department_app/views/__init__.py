"""[summary]"""

from flask import Blueprint
m_bp = Blueprint('m_bp', __name__)

from . import department
from . import employee
from . import position