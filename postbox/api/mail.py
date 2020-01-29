import logging
import os

from flask import Blueprint, request, render_template
from flask_cors import cross_origin

from postbox.util.mail_util import send_mail
from postbox.util.web_util import request_param

logger = logging.getLogger("mail")

mail_bp = Blueprint('mail_api', __name__)


@mail_bp.route('/mail', methods=['POST'])
@cross_origin()
def send():
    file = request.files['file'] if request.files else None
    _to = request.form.getlist('to')
    _cc = request.form.getlist('cc')
    content_type = request_param('content_type', default='html')
    sender = os.environ.get('SENDER', None)
    from_ = request_param('from', default=sender)

    alias = request_param('alias', default="byunseob")
    to = request_param('to', required=True) if not _to else _to
    cc = request_param('cc') if not _cc else _cc
    subject = request_param('subject', required=True)
    content = request_param('content', required=True)

    send_mail(from_, to, subject, content, content_type, alias, file, cc)

    return 'success'
