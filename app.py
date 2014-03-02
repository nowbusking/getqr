    # -*- coding: utf-8 -*-
from StringIO import StringIO

from flask import abort
from flask import Flask
from flask import request
from flask import send_file

import qrcode
from qrcode.image.pil import PilImage


app = Flask(__name__)


def serve_pil_image(pil_img):
    img_io = StringIO()
    pil_img.save(img_io)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')


@app.route("/")
def get_qrcode():
    try:
        chs = request.args['chs']
        data = request.args['chl']
        width, height = (int(x) for x in chs.split('x'))
    except KeyError:
        abort(400)
    except ValueError:
        try:
            width = height = int(chs)
        except ValueError:
            abort(400)

    eclv = 'L'
    margin = 4
    if 'chld' in request.args:
        chld = request.args['chld'].split('|')
        eclv = chld[0]
        if len(chld) == 2:
            margin = chld[1]

    ec = qrcode.constants.__getattribute__('ERROR_CORRECT_{0}'.format(eclv))
    qr = qrcode.QRCode(
        version=None,
        error_correction=ec,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(image_factory=PilImage)
    img._img.thumbnail((width, height))
    return serve_pil_image(img)


if __name__ == "__main__":
    app.run(debug=True)
