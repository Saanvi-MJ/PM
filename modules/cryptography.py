from cryptography.fernet import Fernet


class Cryptography:

    # * Private Class Variable
    __key = None

    # * Function to Generate Key
    # * No Parameters
    # * No Return Value
    @classmethod
    def generateKey(cls) -> None:
        cls.__key = Fernet.generate_key()

    # * Function to Get Key
    # * No Parameters
    # * Return Value: Unique Key
    @classmethod
    def getKey(cls) -> bytes:
        return cls.__key

    # * Function to Destroy Key
    # * No Parameters
    # * No Return Value
    @classmethod
    def destroyKey(cls) -> None:
        cls.__key = None

    # * Function to Encrypt a String
    # * Parameters: String to be Encrypted, Unique Key
    # * Return Value: Encrypted Byte String
    @classmethod
    def encrypt(cls, string: str, unique_key: bytes) -> bytes:
        string_bytes = bytes(string, 'utf-8')
        return Fernet(unique_key).encrypt(string_bytes)

    # * Function to Encrypt a String
    # * Parameters: Encrypted Byte String, Unique Key
    # * Return Value: Decrypted String
    @classmethod
    def decrypt(cls, string_byte: bytes, unique_key: bytes) -> str:
        string = Fernet(unique_key).decrypt(string_byte).decode()
        return string
