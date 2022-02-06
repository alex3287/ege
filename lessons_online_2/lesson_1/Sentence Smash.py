def smash(words):
    result = ''
    for i in words:
        result += (i + ' ')
    return result[:-1]
    # return result.strip()


def smash2(words):
    return ''.join(words)


# A =["hello", "world"] # "hello world")
A = ["hello", "amazing", "world"] # "hello amazing world")
#         test.assert_equals(smash(["this", "is", "a", "really", "long", "sentence"]), "this is a really long sentence")

print(smash2(A))