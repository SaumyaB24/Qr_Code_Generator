from flask import Flask, render_template, request, send_file, url_for
import qrcode
import os
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join('static', 'qrcodes')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_filename = None
    if request.method == 'POST':
        url = request.form.get('url')
        fill_color = request.form.get('fill_color') or 'black'
        back_color = request.form.get('back_color') or 'white'

        if url:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr.add_data(url)
            qr.make(fit=True)

            img = qr.make_image(fill_color=fill_color, back_color=back_color)
            qr_filename = f"qr_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
            img_path = os.path.join(UPLOAD_FOLDER, qr_filename)
            img.save(img_path)

    return render_template('index.html', qr_filename=qr_filename)

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join(UPLOAD_FOLDER, filename), as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
