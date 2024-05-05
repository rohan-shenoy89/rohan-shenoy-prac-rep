#Exercise 1: Reverse each word of a string

#option 1
def reverse(str):
    result = str[::-1]
    return result


value = reverse("My Name is Jessa")
print(value)

#option 2

def reverse2(str2):
    words = str2.split(" ")

    for word in words:
        result2 = word[::-1]

        final_rslt = " ".join(result2)
        return final_rslt


str2 = "My Name is Jessa"
print(reverse2(str2))
