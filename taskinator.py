#!../bin/python3
import argparse
import yaml

# Code will only work if called directly, so far it is only being developed as a terminal application

def add_task(title, desc, category=str()):

    entry = {title : desc}

    with open('test.yml', 'r+') as yml_file:
        buffer_list = yaml.safe_load_all(yml_file)

        #print(f'Current Buffer is:\n{buffer}, Buffer type is: {type(buffer)}') #Debugging
        #print(f'Current entry is:\n{entry}, Entry type is: {type(entry)}') #Debugging

        if title in buffer:
            print('Entry already found in journal, aborting')
        else:
            buffer.update(entry)

            #First, resets the entire file ... maybe a bad idea for larger files?
            yml_file.seek(0)
            yml_file.truncate()
            yaml.dump(buffer, yml_file)
            print('Jounal updated')
    pass

def print_task(title):

    with open('test.yml', 'r') as yml_file:
        buffer = yaml.safe_load(yml_file)
        if title in buffer:
            print(buffer[title])
        else:
            print(f'\"{title}\" doesn\'t exists in file')
    pass

def remove_task(title):
    
    with open('test.yml', 'r+') as yml_file:
        buffer = yaml.safe_load(yml_file)
        if title in buffer:
            del(buffer[title])
            #print(buffer)  #Debugging
            yml_file.seek(0)
            yml_file.truncate()
            yaml.dump(buffer, yml_file)
            print(f'{title} removed from journal')
            pass
        else:
            print(f'\"{title}\" doesn\'t exists in file')
    pass

def list_task():

    with open("test.yml", "r") as yml_file:
        buffer_list = yaml.safe_load_all(yml_file)

        buffer = buffer_list[0]
        for title in buffer:
            print(title)

        #for buffer in buffer_list:
        #    for title in buffer:
        #        print(title)
        #    pass
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            prog="task",
            description="It was supposed to be an todo app, but it's functionality is pretty amorphic",
            epilog="not here!"
            )
    parser.add_argument("action", action='store', metavar='add, done, remove or print', help='Execute action upon the entry', choices=['add', 'done', 'remove', 'print', 'list'])
    parser.add_argument("entry_name", action='store', metavar='task title', help='Specify the title of the entry to execute action, use keyword \'all\' to use entire journal', nargs='*')

    args = parser.parse_args()
    #print(args)         #Debugging

    #It reccomends using with open as to automatically close the file when it is not needed any longer, which ... might be good??
    #That will be the implementation for now, I shall observe it's behaviour closely
    
    action = args.action
    title = ' '.join(args.entry_name)

    #Add appends new entry to the end of the journal
    #But, due to the way the yml works it can't have two or more keys with the same name
    #i.e : the new structure means we now must use title:description straightforward
    #And also a check must be made before every add action, to stop the user from adding a entry
    #which already exists, maybe creating a flag l8 on to allow substitution

    #There are 2 methods now
    #either 
    #a: the file gets loaded ONCE in the entire program, right at the beginning, as r+, and the add action
    #rewrites everything
    #b: the file gets loaded in each method, the code would be safer and easier, but its ugly

    if action == 'add':        #Being debugged
        desc = input(f'Define a description for {title}:\n')        #Change to l8 allow the user to use text editors!
        add_task(title, desc)
    elif action == 'print':
        print_task(title)
    elif action == 'list':
        list_task()
    else:
        remove_task(title)
