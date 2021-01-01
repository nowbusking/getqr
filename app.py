# -*- coding: utf-8 -*-
try:
    from StringIO import StringIO ## for Python 2
except ImportError:
    from io import StringIO ## for Python 3

from flask import abort
from flask import Flask
from flask import redirect
from flask import request
from flask import send_file
from PIL import Image
import qrcode
from qrcode.image.pil import PilImage
import os

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 60 * 60 * 24 * 7


def serve_pil_image(pil_img):
    img_io = StringIO()
    pil_img.save(img_io, format='png')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')


@app.route('/')
def hello():
    return redirect('http://github.com/spoqa/getqr')


@app.route("/qr", methods=['GET', 'POST'])
def get_qrcode():
    try:
        chs = request.values['chs']
        data = request.values['chl']
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
    if 'chld' in request.values:
        chld = request.values['chld'].split('|')
        eclv = chld[0]
        if len(chld) == 2:
            margin = chld[1]

    ec = qrcode.constants.__getattribute__('ERROR_CORRECT_{0}'.format(eclv))
    qr = qrcode.QRCode(
        version=None,
        error_correction=ec,
        box_size=10,
        border=margin
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_image = qr.make_image(image_factory=PilImage)
    qr_image._img.thumbnail((width, height))
    final = Image.new('RGBA', (width, height), (255, 255, 255, 255))
    final.paste(qr_image._img, ((width - qr_image._img.size[0]) / 2,
                                (height - qr_image._img.size[1]) / 2))
    return serve_pil_image(final)


if __name__ == "__main__":
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 5000))
    debug = bool(os.environ.get('DEBUG', 0))

    app.run(host=host, port=port, debug=debug)

