import secrets
import sys


k1 = secrets.token_bytes(1)


print(k1)
print(bin(int.from_bytes(k1, byteorder=sys.byteorder)))
