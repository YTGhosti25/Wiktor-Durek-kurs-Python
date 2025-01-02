from tkinter import *
import json

with open('to do list\data.json','r') as file:
    zadania = json.load(file)
    file.close

def save_list_to_json ():
    with open("to do list\data.json", "w") as outfile:
        json.dump(zadania, outfile)
        outfile.close

def modify_title (title): 
    """if title is already in zadania, add number to it"""
    i=2
    if title in zadania:
        title = title +" (" + str(i) + ")"
    else:
        return title
    
    while True:
        i+=1 
        if title in zadania:
            x=title.rfind(" (")
            new_title = title[:x] +" (" + str(i) + ")"

            title=new_title
        else:
            return title

def add_new_task_to_memory (title, description, date_of_realization):
    
    title = modify_title(title)

    task = {
        "title": title,
        "description": description,
        "date_of_realization": date_of_realization,
        "status": "uncompleted"
    }

    zadania[title] = (task)

def task_completed (title):
    zadania[title]["status"] = "completed"

def delete_task (title):
    del zadania[title]

def print_all_tasks ():
    for i in zadania:
        print(f"tytuł: {zadania[i]["title"]},\nopis: {zadania[i]["description"]},\ndata realizacji: {zadania[i]["date_of_realization"]},\nstatus: {zadania[i]["status"]}\n")

# add_new_task("siema","jak tam","2024-10-01")
# add_new_task("siema","jAak tam","20A24-10-01")
# add_new_task("siema","jAaaaaaaak tam","20A24-10-01")
# add_new_task("siema","jAak tam","20A24-10-01aaaa")
# task_completed("siema")
# delete_task("siema (2)")
# add_new_task("siema","jAak tammaksfmoofka","20A24-10-01")
#print_all_tasks()



# task_completed("siema")
# print(zadania)
# print(zadania["siema"])
# delete_task(0)
# print(zadania[0])

# menu = Tk()
# w = Label(menu, text='GeeksForGeeks.org!')
# w.pack()



menu = Tk()
menu.title("To-do list")
menu.geometry("850x250")  


scrollbar = Scrollbar(menu)
# scrollbar.grid(row=0,column=2) 
listbox = Listbox(menu, height = 10, 
                  width = 15, 
                  bg = "white",
                  activestyle = 'dotbox', 
                  font = "Helvetica",
                  fg = "black",
                  yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview) 

 
label = Label(menu, text = "Nazwy zadań",bg='white',width=19) 
task_info = Label(menu,text="Hello world",bg='lightgray', width=100)

def add_new_task():
    #new entry box for user input
    #get: tytuł, opis, datę(spinbox)
    #wpisz to do pamięci
    pass

def change_state():
    index = int(listbox.curselection()[0])
    title = listbox.get(index)
    print(title)

def on_select(event):
    w = event.widget
    index = int(w.curselection()[0])
    title = w.get(index)
    #wyświetl po prawej tytuł opis datę i status
    #dwa przyciski, jeden do zmienienia statusu na wykonane a drugi do usunięcia
    #print(f'You selected item {index}: "{value}"')
    task_info.config(text=str(zadania[title]))
    change_state_button.config(command=change_state)
    #delete_task_button.config(command=delete_task(title))

new_task_button = Button(menu, text='new task', width=18, command=add_new_task())
change_state_button = Button(menu, text='change state', width=18, command=None)
delete_task_button = Button(menu, text='delete task', width=18, command=None)



listbox.insert(1, "siema")
listbox.insert(2, "siema (2)")
listbox.insert(3, "siema (3)")
listbox.insert(4, "siema (4)")



label.grid(row=0,column=0)
listbox.grid(row=1, rowspan=10,column=0)
task_info.grid(row=0,column=1,columnspan=10)
new_task_button.grid(row=11,column=0)
change_state_button.grid(row=11,column=1)
delete_task_button.grid(row=11,column=2)

listbox.bind('<<ListboxSelect>>', on_select)


menu.mainloop()