#!../bin/python3
import argparse
import yaml

# Code will only work if called directly, so far it is only being developed as a terminal application

def add_task(title, desc, buffer, category=None):


    #print(f'Current Buffer is:\n{buffer}, Buffer type is: {type(buffer)}') #Debugging
    #print(f'Current entry is:\n{entry}, Entry type is: {type(entry)}') #Debugging

    if category == None:
        if title in buffer:
            print(f'{title} already in journal')
            return 1
        entry = {title : desc}
    elif category not in buffer: 
        entry = {category: {title : desc}}

    elif type(buffer[category]) != type(dict()) :
        print(f'{category} already found in the journal as an entry, aborting')
        return 1

    elif title not in buffer[category]:
        entry = {category: {title : desc}}
        entry[category].update(buffer[category])

    else:
        print('Entry already found in this category, aborting')
        return 1

    buffer.update(entry)
    return buffer
    print('Jounal updated')

def print_task(title, buffer, category=None, all=False):

    if category is None:
        pass
    elif category in buffer:
        buffer = buffer[category]
    else:
        print(f'{category} doesn\'t exists in file, returning failure')
        return 1

    if all is False:
        if title not in buffer:
            print(f'\"{title}\" doesn\'t exists in journal, returning failure')
            return 1
        elif type(buffer[title]) == type(dict()):
            buffer = buffer[title]
            for entry in buffer:
                if type(buffer[entry]) == type(dict()):
                    print(f'\\{entry}[{len(buffer[entry])}]\n')
                    for parallax_entry in buffer[entry]:
                        print(f'\t\\{parallax_entry}\n\t->{buffer[entry][parallax_entry]}\n')
                else:
                    print(f'\\{entry}\n->{buffer[entry]}\n')
            return 0

        print(buffer[title])
    else:
        for entry in buffer:
            if type(buffer[entry]) == type(dict()):
                print(f'\\{entry}[{len(buffer[entry])}]\n')
                for parallax_entry in buffer[entry]:
                    print(f'\t\\{parallax_entry}\n\t->{buffer[entry][parallax_entry]}\n')
            else:
                print(f'\\{entry}\n->{buffer[entry]}\n')

def remove_task(title, buffer, category=None, all=False):
    if category == None:
        if title in buffer:
            del(buffer[title])
            print(f'{title} removed from journal')
        else:
            print(f'\"{title}\" doesn\'t exists in the journal, aborting')
            return 1

    elif category not in buffer:
        print(f'\"{category}\" doesn\'t exists in journal, aborting')
        return 1

    elif title in buffer[category]:
        del(buffer[category][title])
        print(f'{title} removed from {category}')

    else:
        print(f'\"{title}\" doesn\'t exists in {category}, aborting')
        return 1

    return buffer

def list_task(buffer, category=None, all=False):
    if category is None:
        pass
    elif category in buffer:
        buffer = buffer[category]
    else:
        print(f'{category} doesn\'t exists in file, returning')
        return 1

    for entry in buffer:
        #Now lists the category 2! yieppeeee
        if type(buffer[entry]) == type(dict()):
            print(f'{entry} [{len(buffer[entry])}]')
            if all is True:
                for categ_entry in buffer[entry]:
                    print(f' -{categ_entry}')
        #Normal printing lol
        else:
            print(entry)

def read_file():
    with open(file_name, "r") as yaml_file:
        buffer = yaml.safe_load(yaml_file)
        #buffer type is always dictionary
        return buffer

def write_file(buffer):
    with open(file_name, "w") as yaml_file:
        yaml.dump(buffer, yaml_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            prog="task",
            description="It was supposed to be an todo app, but it's functionality is pretty amorphic",
            epilog="not here!"
            )

    parser.add_argument("action", 
                        action='store', 
                        metavar='add, done, remove or print', 
                        help='Execute action upon the entry', 
                        choices=['add', 'done', 'remove', 'print', 'list'])
    parser.add_argument("entry_name",
                        action='store',
                        metavar='task title',
                        help='Specify the title of the entry to execute action, use keyword \'all\' to use entire journal',
                        nargs='*')
    parser.add_argument('-c',
                        action='store',
                        help='Specify a category for entry',
                        default=None, dest='category')

    global file_name 
    file_name = "test.yml"
    
    args = parser.parse_args()
    
    action = args.action
    title = ' '.join(args.entry_name)
    category = args.category

    all = False 

    if title == 'all':
        all = True
        title = None

    if action == 'add':
        desc = input(f'Define a description for {title}:\n')        #Change to l8 allow the user to use text editors!
        old_journal = read_file()
        new_journal = add_task(title, desc, old_journal, category) 
        write_file(new_journal)

    elif action == 'print':
        old_journal = read_file()
        print_task(title, old_journal, category, all)

    elif action == 'list':
        old_journal = read_file()
        list_task(old_journal, category, all)

    else:
        old_journal = read_file()
        new_jornal = remove_task(title, old_journal, category, all) 
        write_file(new_journal)
