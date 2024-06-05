import argparse
import yaml

# Code will only work if called directly, so far it is only being developed as a terminal application

def add_task(title, desc=str()):

    print(journal)      #Debugging
    print(args)         #Debugging

    #Test write to file
    with open('output.yml', 'a') as output_file:
        yaml.dump({'title': title, 'desc':desc}, output_file) 
    #Remember to remove that, output must be the same as input (obviously)

    pass

def print_task(title):
    pass

def remove_task(title):
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

    #It reccomends using with open as to automatically close the file when it is not needed any longer, which ... might be good??
    #That will be the implementation for now, I shall observe it's behaviour closely
    
    with open('test.yml') as file_stream:
        journal = yaml.safe_load(file_stream) #In the next phase, this section will need an update for safe_load_all


    print(journal)      #Debugging
    print(args)         #Debugging



    action = args.action
    title = ' '.join(args.entry_name)

    if action == 'add':        #Being debugged
        desc = input(f'Define a description for {title}:\n')        #Change to l8 allow the user to use text editors!
        add_task(title, desc)
    elif action == 'print':
        print_task(title)
    else:
        remove_task(title)
