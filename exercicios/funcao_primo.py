

# def eh_primo(numero):
#     divisores = 0
#     for i in range(1, numero + 1):
#         if numero % i == 0:
#             divisores += 1
#     return divisores == 2

# print(eh_primo(423239847294724))


def eh_primo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

print(eh_primo(423239847294724))
