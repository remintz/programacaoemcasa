gatos = ['Coco', 'Princess', 'Samantha', 'Sheba', 'Samantha'] 
# 'Gizmo', 'Lilly', 'Sammy', 'Pumpkin', 'Cali', 'Rascal', 'Toby', 'Luna', 'Boo', 'Mittens', 'Buddy', 'Pepper', 'Maggie', 'Daisy', 'Spooky', 'Samantha', 'Boo', 'Kiki', 'Mia', 'Boo', 'Dusty', 'Boo', 'Buster', 'Luna', 'Buster', 'Sheba', 'Angel', 'Pumpkin', 'Baby', 'Garfield', 'Maggie', 'Annie', 'Tinkerbell', 'Missy', 'Scooter', 'Buster', 'Toby', 'Muffin', 'Bailey', 'Tigger', 'Oscar', 'Lucy', 'Shadow', 'Chloe', 'Lilly', 'Chester', 'Midnight', 'Max', 'Trouble', 'Whiskers', 'Jasper', 'Mimi', 'Charlie', 'Precious', 'Bandit', 'Boots', 'Dusty', 'Snuggles', 'Zoe', 'Scooter', 'Mimi', 'Peanut', 'Mimi', 'Jasper', 'Felix', 'Oreo', 'Cuddles', 'Kitty', 'Tigger', 'Oscar', 'Sadie', 'Bubba', 'Smokey', 'Cookie', 'Snuggles', 'Whiskers', 'Misty', 'Sheba', 'Missy', 'Bear', 'Coco', 'Max', 'Cuddles', 'Loki', 'Baby', 'Toby', 'Casper', 'Oliver', 'Sugar', 'Pepper', 'Chloe', 'Buster', 'Milo', 'Kiki', 'Mia']


for gato_a in gatos:
    contador = 0
    print(f'Vou analisar {gato_a}')
    for gato_b in gatos:
        if gato_a == gato_b:
            contador = contador + 1
    if contador > 1:
        print(f'{gato_a} aparece mais de uma vez')
    else:
        print(f'{gato_a} só aparece uma vez')

