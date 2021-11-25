from utils.class_utils import Encoder, Decoder
from utils.utils import get_sum

print(get_sum(1, 2))

encoder = Encoder()
decoder = Decoder()
print(encoder.encode('abcdef'))
print(decoder.decode('edcba'))
