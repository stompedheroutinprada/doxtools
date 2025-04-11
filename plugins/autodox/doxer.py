### autodox
import os
from clear import screen
from plugins.autodox import questions

#this is the ui which contains the dox logo / ascii art
def ui():
    global content
    with open("ui", "r", encoding="utf-8") as file:
        content = file.read()


# this is to ask questions
def doxquestions():
    global doxname
    while True:
        doxname = input("What would you like to name this dox:")
        if doxname == "":
            print("please enter a file name.")
        else:
            questions.questions()
            doxlayout()
            break


# this is the dox layout
def doxlayout(): 
    ui()
    doxcontent = f'''
{content}

{questions.doxquestions}
'''
    folder_path = "results/doxes"
    file_name = f"{doxname}.txt"
    file_path = f"{folder_path}/{file_name}"

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    with open(file_path, "w", encoding="utf-8") as doxresult:
        doxresult.write(doxcontent)

    
