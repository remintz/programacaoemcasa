gatos = ['Coco', 'Princess', 'Samantha', 'Sheba', 'Abby', 'Gizmo', 'Lilly', 'Sammy', 'Pumpkin', 'Cali', 'Rascal', 'Toby', 'Luna', 'Boo', 'Mittens', 'Buddy', 'Pepper', 'Maggie', 'Daisy', 'Spooky', 'Samantha', 'Boo', 'Kiki', 'Mia', 'Boo', 'Dusty', 'Boo', 'Buster', 'Luna', 'Buster', 'Sheba', 'Angel', 'Pumpkin', 'Baby', 'Garfield', 'Maggie', 'Annie', 'Tinkerbell', 'Missy', 'Scooter', 'Buster', 'Toby', 'Muffin', 'Bailey', 'Tigger', 'Oscar', 'Lucy', 'Shadow', 'Chloe', 'Lilly', 'Chester', 'Midnight', 'Max', 'Trouble', 'Whiskers', 'Jasper', 'Mimi', 'Charlie', 'Precious', 'Bandit', 'Boots', 'Dusty', 'Snuggles', 'Zoe', 'Scooter', 'Mimi', 'Peanut', 'Mimi', 'Jasper', 'Felix', 'Oreo', 'Cuddles', 'Kitty', 'Tigger', 'Oscar', 'Sadie', 'Bubba', 'Smokey', 'Cookie', 'Snuggles', 'Whiskers', 'Misty', 'Sheba', 'Missy', 'Bear', 'Coco', 'Max', 'Cuddles', 'Loki', 'Baby', 'Toby', 'Casper', 'Oliver', 'Sugar', 'Pepper', 'Chloe', 'Buster', 'Milo', 'Kiki', 'Mia']

OPCAO = 2

if OPCAO == 1:
    print('opção 1, super simples mas repete a mensagem')
    for i in range(len(gatos)):
        for j in range(i+1, len(gatos)):
            if gatos[i] == gatos[j]:
                print('o nome %s está repetido' % gatos[i])

if OPCAO == 2:
    print('opção 2 - não repete a mensagem')
    repetidos = []  # armazena os nomes repetidos já informados
    for i in range(len(gatos)):
        for j in range(i+1, len(gatos)):
            if gatos[i] == gatos[j]:
                # encontrou nomes iguais
                if not gatos[i] in repetidos:
                    # ainda não informou este
                    print('o nome %s está repetido' % gatos[i])
                    repetidos.append(gatos[i])
                
