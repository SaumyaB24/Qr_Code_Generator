from flask import Flask, render_template, request, send_file, redirect, url_for, flash
import qrcode
import qrcode.constants
from PIL import Image
import io
import os

app = Flask(__name__)
app.secret_key = 'secret123'  # Required for flash messages

# Route
@app.route("/", methods=["GET", "POST"])
def index():
    qr_data = None
    if request.method == "POST":
        try:
            url = request.form["url"]
            foreground_color = request.form["foreground_color"]
            background_color = request.form["background_color"]

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4
            )
            qr.add_data(url)
            qr.make(fit=True)

            img = qr.make_image(fill_color=foreground_color, back_color=background_color)
            img_io = io.BytesIO()
            img.save(img_io, "PNG")
            img_io.seek(0)

            qr_data = img_io.getvalue().hex()
            return render_template("index.html", qr_data=qr_data)

        except Exception as e:
            flash(f"Error: {str(e)}")
            return redirect(url_for("index"))

    return render_template("index.html", qr_data=qr_data)

@app.route("/download", methods=["POST"])
def download():
    url = request.form["url"]
    foreground_color = request.form["foreground_color"]
    background_color = request.form["background_color"]

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color=foreground_color, back_color=background_color)
    img_io = io.BytesIO()
    img.save(img_io, "PNG")
    img_io.seek(0)
    return send_file(img_io, mimetype="image/png", as_attachment=True, download_name="generated_qr.png")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
