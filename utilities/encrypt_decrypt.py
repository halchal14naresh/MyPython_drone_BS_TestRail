from cryptography.fernet import Fernet


class EncryptDecrypt:

    def generate_key(self):
        """
        Generates the Symmetric encryption key
        """
        return Fernet.generate_key()

    def encrypt_message(self, message: str):
        """
        Encrypt the given message using Symmetric encryption key.
        Note: Please uncomment print statements to get the value of key and encrypted test
        """
        key = self.generate_key()
        print("key:", key)
        encoded_message = message.encode('utf-8')
        encoded_fernet = Fernet(key)
        encrypted_message = encoded_fernet.encrypt(encoded_message)
        print("encrypted message: ", encrypted_message)

    def decrypt_message(self, encrypt_message: bytes, decrypt_key):
        """
        Encrypt the given encrypted message using Symmetric encryption key
        """
        df = Fernet(decrypt_key)
        decrypted_message = df.decrypt(encrypt_message)
        print(decrypted_message)

        return decrypted_message.decode()


en = EncryptDecrypt()
en.encrypt_message("nku")
