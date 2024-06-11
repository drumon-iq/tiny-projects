#!../bin/python3
import argparse
import yaml

# Code will only work if called directly, so far it is only being developed as a terminal application

def add_task(title, desc, category=''):

    with open('test.yml', 'r+') as yaml_file:
        buffer = yaml.safe_load(yaml_file)

        #print(f'Current Buffer is:\n{buffer}, Buffer type is: {type(buffer)}') #Debugging
        #print(f'Current entry is:\n{entry}, Entry type is: {type(entry)}') #Debugging

        if category == '':
            if title in buffer:
                print(f'{title} already in journal')
                return
            entry = {title : desc}
        else:
            #If the title is in the category it will also overwrite, so none of that
            entry = {category: {title : desc}}
                #If the category already exists, it must be manually merged before the dict merging or it wil  overwrite data
            if category not in buffer: 
                pass
            elif type(buffer[category]) != type(dict()) :
                print(f'{category} already found in the journal as an entry, aborting')
                return
            else:
                if title not in buffer[category]:
                    entry[category].update(buffer[category])
                else:
                    print('Entry already found in this category, aborting')
                    return

        buffer.update(entry)
        yaml_file.seek(0)
        yaml_file.truncate()
        yaml.dump(buffer, yaml_file)
        print('Jounal updated')

def print_task(title, category=''):

    with open('test.yml', 'r') as yaml_file:
        buffer = yaml.safe_load(yaml_file)

        if category != '':
            if category in buffer:
                if title in buffer[category]:
                    print(buffer[category][title])
                else:
                    print(f'\"{title}\" doesn\'t exists in {category}')
            else:
                print(f'{category} doesn\'t exists')
        else:
            if title in buffer:
                print(buffer[title])
            else:
                print(f'\"{title}\" doesn\'t exists in journal')

    pass

def remove_task(title, category=''):
    
    with open('test.yml', 'r+') as yaml_file:
        buffer = yaml.safe_load(yaml_file)

        if category != '':
            if category in buffer:
                if title in buffer[category]:
                    del(buffer[category][title])
                    #print(buffer)  #Debugging
                    yaml_file.seek(0)
                    yaml_file.truncate()
                    yaml.dump(buffer, yaml_file)
                    print(f'{title} removed from {category}')
                else:
                    print(f'\"{title}\" doesn\'t exists in {category}')
            else:
                print(f'\"{category}\" doesn\'t exists in file')
        else:
            if title in buffer:
                del(buffer[title])
                #print(buffer)  #Debugging
    
                yaml_file.seek(0)
                yaml_file.truncate()
                yaml.dump(buffer, yaml_file)
    
                print(f'{title} removed from journal')
            else:
                print(f'\"{title}\" doesn\'t exists in buffer')

def list_task():

    with open("test.yml", "r") as yaml_file:
        buffer = yaml.safe_load(yaml_file)

        for title in buffer:
            print(title)

            #Now lists the category 2! yieppeeee
            if type(buffer[title]) == type(dict()):
                for categ_title in buffer[title]:
                    print(f' -{categ_title}')
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            prog="task",
            description="It was supposed to be an todo app, but it's functionality is pretty amorphic",
            epilog="not here!"
            )
    parser.add_argument("action", action='store', metavar='add, done, remove or print', help='Execute action upon the entry', choices=['add', 'done', 'remove', 'print', 'list'])
    parser.add_argument("entry_name", action='store', metavar='task title', help='Specify the title of the entry to execute action, use keyword \'all\' to use entire journal', nargs='*')
    parser.add_argument('-c', action='store', help='Specify a category for entry', default='', dest='category')
    #Funções para colocar depois, 
    #--overwrite para add executa um overwrite
    #all para remove, print, executa tal ação com todas as entradas do arquivo
    #-f muda o arquivo sendo alterado
    
    args = parser.parse_args()
    #print(args)         #Debugging
    
    action = args.action
    title = ' '.join(args.entry_name)
    category = args.category

    if action == 'add':
        desc = input(f'Define a description for {title}:\n')        #Change to l8 allow the user to use text editors!
        add_task(title, desc, category)
    elif action == 'print':
        print_task(title, category)
    elif action == 'list':
        list_task()
    else:
        remove_task(title, category)
