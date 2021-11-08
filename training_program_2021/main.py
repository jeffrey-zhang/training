from utils.utils import get_sum
from utils.class_utils import *

print(get_sum(1, 2))

encoder = Encoder()
decoder = Decoder()
print(encoder.encode('abcdef'))
print(decoder.decode('edcba'))