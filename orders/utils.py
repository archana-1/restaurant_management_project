import secrets
from .models import Coupon
import string

def generate_coupon_code(len = 10):
    # generates alpha numeric code of len 10
    code = ""
    characters = string.ascii_uppercase+ string.digits
    while True:
        for i in range(len):
            code += secrets.choice(characters)
        if not Coupon.objects.filter(code=code).exists():

            return code

generate_coupon_code()