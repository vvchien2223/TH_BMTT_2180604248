class TranspositionCipher:
    def __init__(self):
        pass 
    def encrypt(self,text,key):
        encrypted_text = ''
        for col in range (key):
            pointer = col
        while pointer < len(text):
            