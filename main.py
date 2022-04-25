from inquirer.themes import GreenPassion
import os, signal, random, shutil, chalk, inquirer
from os import killpg, name,system
from pynput import keyboard

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


#Si le système est windows
if name == 'nt':
    clear()
    questions = [
        inquirer.Confirm('continue',
                    message="Incompatible avec Windows, voulez vous continuer ? // Incompatible with Windows, do you want to continue ?",)
    ]

    win = inquirer.prompt(questions, theme=GreenPassion())


    if win['continue'] == True:
        clear()
        pass
    else:
        clear()
        exit()


# Nombre de colonnes et rangées dans le terminal
columns, rows = shutil.get_terminal_size()

clear()
def home():
    questions = [
        inquirer.List(
            "start",
            message="RANDOM COLOR CLI",
            choices=["Mode Normal", "Couleurs Sombres", "Couleurs Claires", "HEX to RGB", "RGB to HEX", "Sortir"],
    ),
]

    answer = inquirer.prompt(questions, theme=GreenPassion())


    if answer['start'] == 'Mode Normal':
        def colornew():
            def get_color_escape(r, g, b, background=True):
                return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)


            #Afficher la couleur de fond
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            for i in range(columns):
                print(get_color_escape(r, g, b))
        
            if r + g + b >= 364:
                print(chalk.bold(chalk.black('\t\tHEX : #{:02x}{:02x}{:02x}'.format(r, g, b) + '\t\t\t' + 'RGB : ({}, {}, {})'.format(r, g, b))))
            else:
                print(chalk.bold(chalk.white('\t\tHEX : #{:02x}{:02x}{:02x}'.format(r, g, b) + '\t\t\t' + 'RGB : ({}, {}, {})'.format(r, g, b))))
        colornew()

        print(chalk.yellow("\n\n Pour une nouvelle couleur, appuyez sur la touche 'Espace' Pour revenir au menu principal, appuyez sur la touche 'ESC'\n"))
        def on_press(key):
            if key == keyboard.Key.space:
                #Afficher une nouvelle couleur
                colornew()

            elif key == keyboard.Key.esc:
                clear()
                return home()
            try:
                k = key.char
            except:
                k = key.name  
        listener = keyboard.Listener(on_press=on_press)
        listener.start() 
        listener.join() 


    if answer['start'] == 'Couleurs Sombres':
        def darknew():
            def get_color_escape(r, g, b, background=True):
                return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)

            #Afficher la couleur de fond
            r = random.randint(0, 127)
            g = random.randint(0, 127)
            b = random.randint(0, 127)
            for i in range(columns):
                print(get_color_escape(r, g, b))

            print(chalk.bold(chalk.white('\t\tHEX : #{:02x}{:02x}{:02x}'.format(r, g, b) + '\t\t\t' + 'RGB : ({}, {}, {})'.format(r, g, b))))
        darknew()

        print(chalk.yellow("\n\n Pour une nouvelle couleur, appuyez sur la touche 'Espace' Pour revenir au menu principal, appuyez sur la touche 'ESC'\n"))
        def on_press(key):
            if key == keyboard.Key.space:
                #Afficher une nouvelle couleur
                darknew()

            elif key == keyboard.Key.esc:
                clear()
                return home()
            try:
                k = key.char
            except:
                k = key.name  
        listener = keyboard.Listener(on_press=on_press)
        listener.start() 
        listener.join() 


    if answer['start'] == 'Couleurs Claires':
        def newlight():
            def get_color_escape(r, g, b, background=True):
                return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)

            #Afficher la couleur de fond
            r = random.randint(128, 255)
            g = random.randint(128, 255)
            b = random.randint(128, 255)
            for i in range(columns):
                print(get_color_escape(r, g, b))

            print(chalk.bold(chalk.black('\t\tHEX : #{:02x}{:02x}{:02x}'.format(r, g, b) + '\t\t\t' + 'RGB : ({}, {}, {})'.format(r, g, b))))
        
        newlight()
        print(chalk.yellow("\n\n Pour une nouvelle couleur, appuyez sur la touche 'Espace' Pour revenir au menu principal, appuyez sur la touche 'ESC'\n"))

        def on_press(key):
            if key == keyboard.Key.space:
                #Afficher une nouvelle couleur
                newlight()

            elif key == keyboard.Key.esc:
                clear()
                return home()
            try:
                k = key.char
            except:
                k = key.name  
        listener = keyboard.Listener(on_press=on_press)
        listener.start() 
        listener.join() 

    if answer['start'] == 'HEX to RGB':
        def hex_to_rgb():
            clear()
            hex = input('Entrez le code HEX : ')
            hex = hex.replace('0x', '#')
            if not '#' in hex:
                hex = f'#{hex}'
            
            if len(hex) != 7:
                print(chalk.red('Valeur HEX incorrecte. Veuillez entrer un code HEX valide'))
                home()

            #Convertir le code HEX en code RGB
            try:
                r = int(hex[1:3], 16)
                g = int(hex[3:5], 16)
                b = int(hex[5:7], 16)
            except:
                print(chalk.red('Valeur HEX incorrecte. Veuillez entrer un code HEX valide'))
                home()

            #Mettre un aperçu de la couleur à côté du texte
            def get_color_escape(r, g, b, background=False):
                return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)
            print('\t\t RGB : ({}, {}, {})'.format(r, g, b) + '\t Aperçu : ' +get_color_escape(r, g, b)+ '■')
        hex_to_rgb()
        print(chalk.yellow("\n\nPour une nouvelle conversion, écrivez le code HEX à convertir puis appuyez sur 'Entrée' Pour revenir au menu principal, appuyez sur la touche 'ESC'\n"))

        def on_press(key):
            if key == keyboard.Key.enter:
                #Afficher une nouvelle couleur
                hex_to_rgb()

            elif key == keyboard.Key.esc:
                clear()
                return home()
            try:
                k = key.char
            except:
                k = key.name  
        listener = keyboard.Listener(on_press=on_press)
        listener.start() 
        listener.join() 


    if answer['start'] == 'RGB to HEX':
        def rgb_to_hex():
            clear()
            r = input(chalk.red('Red : '))
            g = input(chalk.green('Green : '))
            b = input(chalk.blue('Blue : '))
            # Si la valeur rgb est incorrecte
            if not r.isdigit() or not g.isdigit() or not b.isdigit():
                print(chalk.red('Valeur RGB incorrecte Veuillez entrer un code RGB valide'))
                return home()
            r.replace(' ', '')
            g.replace(' ', '')
            b.replace(' ', '')

            r = int(r)
            g = int(g)
            b = int(b)

            if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
                print(chalk.red('Valeur RGB incorrecte Veuillez entrer un code RGB valide'))
                return home()

            #Mettre un aperçu de la couleur à côté du texte
            def get_color_escape(r, g, b, background=False):
                return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)
            print('\t\tHEX : #{:02x}{:02x}{:02x}'.format(r, g, b) + '\t Aperçu : ' +get_color_escape(r, g, b)+ '■')
        rgb_to_hex()
        print(chalk.yellow("\n\nPour une nouvelle conversion, Appuyez sur 'Entrer'. Pour revenir au menu principal, appuyez sur la touche 'ESC'\n"))

        def on_press(key):
            if key == keyboard.Key.enter:
                #Afficher une nouvelle couleur
                input()
                rgb_to_hex()

            elif key == keyboard.Key.esc:
                clear()
                return home()
            try:
                k = key.char
            except:
                k = key.name  
        listener = keyboard.Listener(on_press=on_press)
        listener.start() 
        listener.join() 

    if answer['start'] == 'Sortir':
        clear()
        killpg(os.getpgid(os.getpid()), signal.SIGTERM)

home()
