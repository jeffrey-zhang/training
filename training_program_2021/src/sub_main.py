import sys

sys.path.append("..")

from utils.class_utils import *

encoder = Encoder()
decoder = Decoder()

print(encoder.encode("Hello World"))
print(decoder.decode(encoder.encode("Hello World")))
