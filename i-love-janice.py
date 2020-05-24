def solution(x):
    normal = [i for i in range(97, 123)]
    reverse = [j for j in range(122, 96, -1)]
    dictionary_of_chars = {normal[n]: reverse[n] for n in range(len(normal))}

    decrypted_string = []

    for c in x:
        if ord(c) in dictionary_of_chars :
            decrypted_string.append(chr(dictionary_of_chars[ord(c)]))
        else:
            decrypted_string.append(c)

    return ''.join(decrypted_string)

print(solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))