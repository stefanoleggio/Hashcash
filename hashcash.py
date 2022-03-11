import hashlib
import time

"""
    Easy Proof Of Work system for validanting messages (Hashcash).
    The sender must show that he was able to find an hash of the message and a nonce (random number) that have the first
    zero_digits to zero.
    To check the validity of the message the receiver has to compute the hash of the payload and check that the first zero_digits are zeros.
"""


# Set the difficoulty
zero_digits = 6

#Message that we want to send
message = 'Hello World'

print("\nMessage: " + message)

nonce = 0
zero_val = '0' * zero_digits

print("Computing the nonce...")

time_start = time.time()

while(True):
    payload = message + str(nonce)
    hashed_string = hashlib.sha256(payload.encode('utf-8')).hexdigest()
    if(hashed_string[:zero_digits] == zero_val):
        break
    nonce += 1

print("Total time: " + str(round(time.time() - time_start,2)))
print("Nonce founded: " + str(nonce))
print("Resulting payload: " + payload)
print("\nSending to the receiver...\n")

hashed_payload = hashlib.sha256(payload.encode('utf-8')).hexdigest()
if(hashed_payload[:zero_digits] == zero_val):
    print("The message is valid!")
    print("Message: " + payload[:(len(payload)-zero_digits-1)])