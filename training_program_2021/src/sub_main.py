from training_program_2021.utils.class_utils import Encoder, Decoder

encoder = Encoder()
decoder = Decoder()

print(encoder.encode("Hello World"))
print(decoder.decode(encoder.encode("Hello World")))
