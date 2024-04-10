from flask import Flask,render_template,request,json
from cipher.caesar import Caesar_Cipher
from cipher.vigenere import VigenereCipher
from cipher.playfair import PlayFairCipher
from cipher.railfence import RailFenceCipher
from cipher.transpostion import TranspositionCipher

app = Flask(__name__)

#roter routes for home page
@app.route("/")
def home():
    return render_template('index.html')

#router routes for caser cypher
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/transposition")
def transpostion():
    return render_template('/transpostion.html')

@app.route("/playfair")
def playfair():
    return render_template('/playfair.html')

#CAESAR 
@app.route("/caesar/encrypt",methods=['POST'])
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
        <button><a href="/caesar" style="color: inherit; text-decoration: none;">Back</a></button>
            """
    return response


@app.route("/caesar/decrypt",methods=['POST'])
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
        <button><a href="/caesar" style="color: inherit; text-decoration: none;">Back</a></button>
            """
    return response  


#VIGENERE CIPHER ALGORITHM
@app.route('/vigenere/encrypt',methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    vigenere_cipher = VigenereCipher()
    encrypted_text = vigenere_cipher.vigenere_encrypt(text,key)
    response = f"""
        <h1>ĐÃ MÃ HÓA THÀNH CÔNG!</h1>
        <p><strong>Text:</strong> {text}</p>
        <p><strong>Key:</strong> {key}</p>
        <p><strong>Decrypted Text:</strong> {encrypted_text}</p>
        <button><a href="/vigenere" style="color: inherit; text-decoration: none;">Back</a></button>
            """
    return response 

@app.route('/vigenere/decrypt',methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    vigenere_cipher = VigenereCipher()
    decrypted_text = vigenere_cipher.vigenere_decrypt(text,key)
    response = f"""
        <h1>ĐÃ GIẢI MÃ THÀNH CÔNG!</h1>
        <p><strong>Text:</strong> {text}</p>
        <p><strong>Key:</strong> {key}</p>
        <p><strong>Decrypted Text:</strong> {decrypted_text}</p>
        <button><a href="/vigenere" style="color: inherit; text-decoration: none;">Back</a></button>
            """
    return response 

#RAILFENCE

@app.route("/railfence/encrypt",methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    railfence_cipher = RailFenceCipher()
    encrypted_text = railfence_cipher.rail_fence_encrypt(text, key)
    response = f"""
        <h1>Đã Mã Hóa Thành Công!</h1>
        <p><strong>Text:</strong> {text}</p>
        <p><strong>Key:</strong> {key}</p>
        <p><strong>Encrypted Text:</strong> {encrypted_text}</p>
        <button><a href="/railfence" style="color: inherit; text-decoration: none;">Back</a></button>
        
            """
    return response


@app.route("/railfence/decrypt",methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    railfence_cipher = RailFenceCipher()
    decrypted_text = railfence_cipher.rail_fence_decrypt(text, key)
    response = f"""
        <h1>ĐÃ GIẢI MÃ THÀNH CÔNG!</h1>
        <p><strong>Text:</strong> {text}</p>
        <p><strong>Key:</strong> {key}</p>
        <p><strong>Decrypted Text:</strong> {decrypted_text}</p>
        <button><a href="/railfence" style="color: inherit; text-decoration: none;">Back</a></button>
            """
    return response  


#Transpostion

@app.route("/transpostion/encrypt",methods=['POST'])
def transpostion_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    transpostion_cipher = TranspositionCipher()
    encrypted_text = transpostion_cipher.encrypt(text, key)
    response = f"""
        <h1>Đã Mã Hóa Thành Công!</h1>
        <p><strong>Text:</strong> {text}</p>
        <p><strong>Key:</strong> {key}</p>
        <p><strong>Encrypted Text:</strong> {encrypted_text}</p>
        <button><a href="/transpostion" style="color: inherit; text-decoration: none;">Back</a></button>
            """
    return response


@app.route("/transpostion/decrypt",methods=['POST'])
def transpostion_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    transpostion_cipher = TranspositionCipher()
    decrypted_text = transpostion_cipher.decrypt(text, key)
    response = f"""
        <h1>ĐÃ GIẢI MÃ THÀNH CÔNG!</h1>
        <p><strong>Text:</strong> {text}</p>
        <p><strong>Key:</strong> {key}</p>
        <p><strong>Decrypted Text:</strong> {decrypted_text}</p>
        <button><a href="/transpostion" style="color: inherit; text-decoration: none;">Back</a></button>
            """
    return response  



#Playfair

@app.route('/playfair/creatematrix',methods=['POST'])
def playfair_creatematrix():
    key = request.form['inputKeyMatrix']
    playfair_cipher = PlayFairCipher()
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    response = f"""
        <h1>ĐÃ TẠO THÀNH CÔNG MA TRẬN!</h1>
        <p><strong>Key:</strong> {key}</p>
        <p><strong>Matrix :</strong> {playfair_matrix}</p>
        <button><a href="/playfair" style="color: inherit; text-decoration: none;">Back</a></button>
            """
    return response 

@app.route('/playfair/encrypt',methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    playfair_cipher = PlayFairCipher()
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(text,playfair_matrix)
    response = f"""
        <h1>ĐÃ MÃ HÓA THÀNH CÔNG!</h1>
        <p><strong>Text:</strong> {text}</p>
        <p><strong>Key:</strong> {key}</p>
        <p><strong>Decrypted Text:</strong> {encrypted_text}</p>
        <button><a href="/playfair" style="color: inherit; text-decoration: none;">Back</a></button>
            """
    return response 

@app.route('/playfair/decrypt',methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    playfair_cipher = PlayFairCipher()
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(text,playfair_matrix)
    response = f"""
        <h1>ĐÃ GIẢI MÃ THÀNH CÔNG!</h1>
        <p><strong>Text:</strong> {text}</p>
        <p><strong>Key:</strong> {key}</p>
        <p><strong>Decrypted Text:</strong> {decrypted_text}</p>
        <button><a href="/playfair" style="color: inherit; text-decoration: none;">Back</a></button>
            """
    return response 


#main function
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5050,debug=True)
    