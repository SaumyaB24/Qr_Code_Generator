from flask import Flask, render_template, request, url_for
import qrcode
import qrcode.constants
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'

@app.route('/', methods=['GET', 'POST'])
def generate_qr():
    qr_generated = False
    qr_filename = None

    if request.method == 'POST':
        link = request.form.get('link')
        fill_color = request.form.get('fill_color')
        back_color = request.form.get('back_color')

        # Generate QR
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4
        )
        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fill_color, back_color=back_color)

        # Save to static folder
        qr_filename = 'qr_code.png'
        img_path = os.path.join(app.config['UPLOAD_FOLDER'], qr_filename)
        img.save(img_path)
        qr_generated = True

    return render_template('index.html', qr_generated=qr_generated, qr_filename=qr_filename)

if __name__ == '__main__':
    app.run(debug=True)
