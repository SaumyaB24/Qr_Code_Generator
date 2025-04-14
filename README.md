# 🎯 QR Code Generator 🔗📱

A sleek and simple web app to **generate QR codes** for any URL, with customizable colors and instant download! 💡🎨

🌐 **Live Website**:  
🔗 [https://qr-code-generator-0obi.onrender.com](https://qr-code-generator-0obi.onrender.com)

---

## 🚀 Features
- 🔗 **URL Input** – Type any URL you want to turn into a QR code
- 🎨 **Custom Colors** – Choose foreground and background colors
- 📸 **Preview on the Same Page**
- 📥 **Download QR Code** – Save the image in PNG format
- ♻️ **Reset Button** – Quickly clear and start over

---

## 🛠️ Tech Stack
| Layer     | Technology     |
|-----------|----------------|
| 👩‍💻 Backend  | Flask (Python) |
| 🎨 Frontend | HTML, CSS       |
| 🧱 Libraries | `qrcode`, `Pillow` |
| ☁️ Hosting   | Render        |

---

## 📂 Project Structure
```
Qr_Code_Generator/
├── app.py              # Flask backend
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Frontend interface
└── static/
    └── qrcodes/        # Saved QR code images
```

---

## 💻 Local Setup

1. 🧬 Clone the repository:
   ```bash
   git clone https://github.com/SaumyaB24/Qr_Code_Generator.git
   ```

2. 📂 Move into the directory:
   ```bash
   cd Qr_Code_Generator
   ```

3. 📦 Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. ▶️ Run the app:
   ```bash
   python app.py
   ```

5. 🌍 Visit in your browser:
   ```
   http://127.0.0.1:5000/
   ```

---

## 📦 Requirements

- Python 3.x
- Flask
- qrcode
- Pillow (PIL)

Install them using:

```bash
pip install flask qrcode[pil]
```

---

## 📜 License
📝 This project is licensed under the **MIT License** – feel free to use and modify it.

---

## 🙌 Credits
- 🔥 [Flask](https://flask.palletsprojects.com/) – lightweight web framework
- 📦 [qrcode](https://pypi.org/project/qrcode/) – QR code generation
- 🖼️ [Pillow](https://pillow.readthedocs.io/) – image processing

---

> Made with ❤️ by **Saumya Bhardwaj**
```
