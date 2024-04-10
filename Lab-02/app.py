from flask import Flask,render_template,request,json
from  cipher.caesar import Caesar_Cipher

app = Flask(__name__)

#roter routes for home page
@app.route("/")
def home():
    return render_template('index.html')

#router routes for caser cypher
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt",methods=['POST'])
def caesar_encrypt():
    
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    caesar_cipher = Caesar_Cipher()
    encrypted_text = caesar_cipher.encrypt_text(text, key)
    response = f"""
        <h1>Đã Mã Hóa Thành Công!</h1>
        <p><strong>Text:</strong> {text}</p>
        <p><strong>Key:</strong> {key}</p>
        <p><strong>Encrypted Text:</strong> {encrypted_text}</p>
            """

    return response


@app.route("/decrypt",methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    caesar_cipher = Caesar_Cipher()
    decrypted_text = caesar_cipher.decrypt_text(text, key)
    response = f"""
        <h1>ĐÃ GIẢI MÃ THÀNH CÔNG!</h1>
        <p><strong>Text:</strong> {text}</p>
        <p><strong>Key:</strong> {key}</p>
        <p><strong>Decrypted Text:</strong> {decrypted_text}</p>
            """

    return response  


#main function
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5050,debug=True)
    