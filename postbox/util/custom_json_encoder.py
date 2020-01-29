from decimal import Decimal
from datetime import datetime, time, date

from flask import json


class CustomJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)

        if isinstance(obj, (datetime, time, date)):
            return obj.isoformat()

        return super(CustomJsonEncoder, self).default(obj)
