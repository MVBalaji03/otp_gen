import random
import string

def generate_otp(length):
    characters = string.ascii_letters + "0123456789"
    otp = ''.join(random.choice(characters)
    for _ in range(length))
    return otp

otp_length = 9
otp = generate_otp(otp_length)
print("OTP is:", otp)