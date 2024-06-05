import argparse
import yaml

# Code will only work if called directly, so far it is only being developed as a terminal application

def add_task(title, desc=str()):

    entry = {title : desc}

    with open('test.yml', 'r+') as yml_file:
        buffer = yaml.safe_load(yml_file)

        #print(f'Current Buffer is:\n{buffer}, Buffer type is: {type(buffer)}')
        #print(f'Current entry is:\n{entry}, Entry type is: {type(entry)}')

        if title in buffer:
            print('Entry already found in journal, aborting')
        else:
            yaml.dump(entry, yml_file)
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
            print(buffer)
            yml_file.seek(0)
            yaml.dump(buffer, yml_file)
            yml_file.truncate()
            pass
        else:
            print(f'\"{title}\" doesn\'t exists in file')
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            prog="task",
            description="It was supposed to be an todo app, but it's functionality is pretty amorphic",
            epilog="not here!"
            )
    parser.add_argument("action", action='store', metavar='add, done, remove or print', help='Execute action upon the entry', choices=['add', 'done', 'remove', 'print'])
    parser.add_argument("entry_name", action='store', metavar='title', help='Specify the title of the entry to execute action, use keyword \'all\' to use entire journal', nargs='*')

    args = parser.parse_args()
    print(args)         #Debugging

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
    else:
        remove_task(title)
