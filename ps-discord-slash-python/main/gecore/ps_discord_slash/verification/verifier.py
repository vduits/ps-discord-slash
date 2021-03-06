from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError

public_key = 'f99d67bdd1c633fd8b42ebfeb3da667b16c29710d570938d87a2c8eb91bd6c47'


def verify_key(headers, raw_body: str) -> bool:
    signature = headers['x-signature-ed25519']
    timestamp = headers['x-signature-timestamp']

    try:
        vk = VerifyKey(bytes.fromhex(public_key))
        vk.verify(f'{timestamp}{raw_body}'.encode(), bytes.fromhex(signature))
        return True
    except BadSignatureError as ex:
        print(ex)
        pass
    return False
