from caesar_cipher import encrypt, decrypt


def test_encrypt_shift_1():
    actual = encrypt(1, "apple")
    expected = "bqqmf"
    assert actual == expected


def test_encrypt_shift_10():
    actual = encrypt(10, "apple")
    expected = "kzzvo"
    assert actual == expected


def test_encrypt_shift_20():
    actual = encrypt(20, "apple")
    expected = "ujjfy"
    assert actual == expected


def test_uppercase():
    actual = encrypt(10, "BANANA")
    expected = "lkxkxk"
    assert actual == expected


def test_with_whitespace():
    actual = encrypt(1, "apples and bananas")
    expected = "bqqmft boe cbobobt"
    assert actual == expected


def test_with_non_alpha():
    actual = encrypt(1, "Gimme a 1!")
    expected = "hjnnf b 1!"
    assert actual == expected


def test_round_trip():
    original = "gimme a 1!"
    shift = 5
    encrypted = encrypt(shift, original)
    actual = decrypt(shift, encrypted)
    expected = original
    assert actual == expected


# def test_crack_phrase():
#     phrase = "It was the best of times, it was the worst of times."
#     encrypted = encrypt(phrase, 10)
#     actual = crack(encrypted)
#     expected = phrase
#     assert actual == expected


# def test_crack_nonsense():
#     phrase = "Ix fhw txe fofg of ndhrl, it nad tho hndrk of allkd."
#     encrypted = encrypt(phrase, 10)
#     actual = crack(encrypted)
#     expected = ""
#     assert actual == expected