import random
pw="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
want=int(input('Mau berapa huruf password?'))



string=""
for i in range(want):
    string += random.choice(pw)
print(string)
