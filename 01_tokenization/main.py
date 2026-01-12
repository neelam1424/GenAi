import tiktoken


enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There! My name is Neelam More"

tokens= enc.encode(text)

#Tokens [25216, 3274, 0, 3673, 1308, 382, 4475, 296, 313, 4633]
print("Tokens", tokens)


decode = enc.decode([25216, 3274, 0, 3673, 1308, 382, 4475, 296, 313, 4633])

print("Decoded",decode)
#Decoded Hey There! My name is Neelam More