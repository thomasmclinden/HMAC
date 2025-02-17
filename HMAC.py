import hmac
import hashlib
import base64

# Function to compute HMAC
def compute_hmac(message, secret_key):
    hash_algorithm = hashlib.sha256
    hmac_object = hmac.new(secret_key.encode(), message.encode(), hash_algorithm)
    hmac_digest = hmac_object.digest()
    encoded_hmac = base64.b64encode(hmac_digest).decode()  # Base64 encoding
    return encoded_hmac

# Function to verify the HMAC (on the receiving side)
def verify_hmac(message, received_hmac, secret_key):
    computed_hmac = compute_hmac(message, secret_key)
    if hmac.compare_digest(computed_hmac, received_hmac):
        print("HMAC verified successfully!")
        return True
    else:
        print("HMAC verification failed!")
        return False

#Sending side
def app_send(message, secret_key):
    print("Sending message...")
    # Compute the HMAC for the message
    hmac_value = compute_hmac(message, secret_key)
    payload = {"message": message, "hmac": hmac_value}
    # Simulate sending the payload to appRecv
    return payload

#Receiving side
def app_recv(payload, secret_key):
    print("Receiving message...")
    message = payload.get("message")
    received_hmac = payload.get("hmac")
    # Verify the HMAC
    if verify_hmac(message, received_hmac, secret_key):
        print("Message:", message)
    else:
        print("Message integrity check failed!")

# Example Usage
if __name__ == "__main__":
    secret_key = "mySecretKey"
    message = "Hello, HMAC!"
    # appSend
    payload = app_send(message, secret_key)
    # appRecv
    app_recv(payload, secret_key)