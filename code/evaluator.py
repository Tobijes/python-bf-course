from typing import Callable
import math
import base64
MESSAGE = "Jeg håber I hyggede og lærte noget!"
MESSAGE = MESSAGE.encode("utf-8")
KEY = base64.b64encode(MESSAGE)
KEY = KEY.decode("utf-8")
single_key_len = len(KEY) // 5

def pjudge(*s):
    print("DOMMER:", *s)

def evaluate(output, result, key):
    if output == result:
        print("-----------------")
        pjudge("I gjorde det! Perfekt! Her er en bid af nøglen I skal bruge:")
        pjudge(key)
        print("-----------------")
        return True
    else:
        pjudge(f"Resultatet: {output} var desværre ikke rigtig. Vi forventede {result}")
        return False

def evaluate_challenge_one(function: Callable):
    key = KEY[0:single_key_len]
    output = function(1,2)
    if evaluate(output, 7, key):
        return key
    

def evaluate_challenge_two(function: Callable):
    key = KEY[single_key_len:single_key_len*2]
    output = round(function(75, 1.80), 1)
    if evaluate(output, 23.1, key):
        return key

def evaluate_challenge_three(function: Callable):
    key = KEY[single_key_len*2:single_key_len*3]
    output = function("Wim")
    if evaluate(output, "Wim, du skal tage en bong!", key):
        return key

def evaluate_challenge_four(function: Callable):
    key = KEY[single_key_len*3:single_key_len*4]
    output = (function(144), function(319))
    if evaluate(output, ("Lige", "Ulige"), key):
        return key


def evaluate_challenge_five(function: Callable):
    key = KEY[single_key_len*4:len(KEY)]
    output = function("BF er fucking nice!", 10)
    if evaluate(output, None, key):
        return key

def key_check(s):
    base64_bytes = s.encode("utf-8")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("utf-8")
    return sample_string