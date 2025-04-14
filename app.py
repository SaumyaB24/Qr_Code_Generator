from flask import Flask, render_template, request, send_file
import qrcode
from PIL import Image
import io

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        foreground_color = request.form["foreground_color"]
        background_color = request.form["background_color"]
        
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
        qr.add_data(url)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color=foreground_color, back_color=background_color)
        
        # Save the generated QR code image in memory
        img_io = io.BytesIO()
        img.save(img_io, "PNG")
        img_io.seek(0)

        return send_file(img_io, mimetype="image/png", as_attachment=True, download_name="generated_qr.png")
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
