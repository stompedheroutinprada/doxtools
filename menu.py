from plugins.autodox import doxer
from plugins.clear import screen
from plugins.camhack import cameraselector
from plugins.mullvadbypass import bypass
username = ""

def menu():
    with open("gui/menu", "r", encoding="utf-8") as homesection:
        home_menu = homesection.read()
    print(f'''
{home_menu}
          ''')
    while True:
        options = input(f"root@{username}:")
        if options == ".autodox":
            screen.cls()
            doxer.doxquestions()
        if options == ".camhack":
            screen.cls()
            camhack()
            break
        if options == ".mullvadbypass":
            screen.cls()
            realmullvadbypass()
            break
        else:
            screen.cls()
            print(f'''{home_menu}''')
            print("Enter an actual option.")
    

def realmullvadbypass():
    with open("gui/mullvadmenu", "r", encoding="utf-8") as mullvadsection:
        mull_menu = mullvadsection.read()
        print(f'''       
{mull_menu}
              ''')
        while True:
            options2 = input(f"root@{username}:")
            if options2.startswith(".bypass"):
                screen.cls()
                print(f'''{mull_menu}''')
                print(f"Their IP has been bypassed ☠️")
                bypass.realbypass()
            if options2 == ".back":
                screen.cls()
                menu()
                break
            if options2 == "":
                screen.cls()
                print(f'''{mull_menu}''')

def camhack():
     with open("gui/cameramenu", "r", encoding="utf-8") as camsection:
        cam_menu = camsection.read()
        print(f'''
{cam_menu}
''')
        while True:
            options1 = input(f"root@{username}:")
            if options1 in cameraselector.cameras:
                cameraselector.cameraviewer(options1)
                screen.cls()
                print(f'''{cam_menu}''')
                
            if options1 == ".back":
                menu()
                break

            if options1 not in cameraselector.cameras:
                screen.cls()
                print(f'''{cam_menu}''')
                print("This camera was not available. (If you would like to go back, type in .back)")
            
             


            


screen.cls()
username = input("Enter a username:")
screen.cls()
menu()

