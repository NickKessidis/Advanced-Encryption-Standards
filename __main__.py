import random


if __name__ == "__main__":

    number = random.randrange(2**127, (2**128)-1)
    # print(bin(number))
    key = random.randrange(2**127, (2**128)-1)

    print("Result of XOR:" + bin(number ^ key))  # COMMENT: The AddRoundKey step (XOR)

    print("Plain text:" + bin(number))

    # # Creating the State Array

    State = ["0", "0", "0", "0",
             "0", "0", "0", "0",
             "0", "0", "0", "0",
             "0", "0", "0", "0"]

    r = ""
    for i in range(0, 16):
        for j in range(8*i+2, 8*i+10):
            # print(j)
            r = r + bin(number)[j]
        # print(r)
        State[i] = r
        # State[i] = int(r, 2)
        r = ""

    print("State Array:")
    print(State)

    # # Creating the S-Box

    Sbox = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(0, 256):
        Sbox[i] = random.randrange(2**7, (2**8)-1)

    # print(Sbox)

    for i in range(0, 16):
        z = State[i]
        c = ""
        for j in range(0, 4):
            c = c + z[j]
        row = int(c, 2)
        c = ""
        for j in range(4, 8):
            c = c + z[j]
        col = int(c, 2)
        State[i] = Sbox[(col+row) % 16]

    print("State Array after the Substitution process:")
    print(State)


