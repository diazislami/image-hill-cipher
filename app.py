# Design is inspired by Clear Code Channel on Youtube (which in Photo Editor part in the video)
# Link Video -> https://youtu.be/mop6g-c5HEY?si=u6JdVndQdj38aSkE

from flask import Flask, render_template, request
import process as prc

app = Flask(__name__)
app.static_folder = "static"

@app.route("/enc", methods=["GET"])
def home():
    return render_template("encryption.html")

@app.route("/dec", methods=["GET"])
def decryption():
    return render_template("decryption.html")

@app.route("/encrypt", methods=["POST"])
def encrypt():
    image = request.files["image"]
    key = request.form["key"]
    key = [int(x) for x in key.split(',')]
    original_image_path = "static/image/" + image.filename
    encryp = prc.hill_cipher_encrypt(original_image_path, key)
    crypted_image_path = "static/image/encrypted_image.png"
    mse, psnr = prc.evaluate(original_image_path, crypted_image_path)
    return render_template("encryption.html", encrypt1=encryp, mse_value1=mse, mse_value3=psnr)

@app.route("/decrypt", methods=["POST"])
def decrypt():
    image = request.files["image"]
    key = request.form["key"]
    key = [int(x) for x in key.split(',')]
    encrypted_image_path = "static/image/" + image.filename
    decryp = prc.hill_cipher_decrypt(encrypted_image_path, key)
    crypted_image_path = "static/image/decrypted_image.png"
    mse, psnr = prc.evaluate(encrypted_image_path, crypted_image_path)
    return render_template("decryption.html", decrypt1=decryp, mse_value2=mse, mse_value3=psnr)

if __name__ == "__main__":
    app.run()
