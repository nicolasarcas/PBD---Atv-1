a = float(input())
b = float(input())
media = (a+b)/2

print(f'Nota 1: {a}\nNota 2: {b}\nMedia: {media}')

if media <= 4:
    print("E\nReprovado")
elif media <=6:
    print("D\nReprovado")
elif media <= 7.5:
    print("C\nAprovado")
elif media <= 9:
    print("B\nAprovado")
else:
    print("A\nAprovado")