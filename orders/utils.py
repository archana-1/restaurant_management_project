import secrets
from .models import Coupon
import strings

def generate_coupon_code(len = ):
    # generates coupon code(alpha num) of len 10
    code = ""
    characters = string.ascii_uppercase+string.digits
    while True:
        for i in range(len):
            code += secrets.choice(characters)
        # check code is unique and not alloted already
        if not Coupon.objects.filter(code = code).exists():
            return code
