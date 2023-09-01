import os
import subprocess
import time
import itertools
import ctypes

def set_window_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

def set_console_size(width, height):
    os.system(f'mode con: cols={width} lines={height}')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    set_console_size(85, 25)

def display_loading_animation():
    animation = itertools.cycle(['|', '/', '—', '\\'])
    start_time = time.time()
    while time.time() - start_time < 3:
        print(f'\rStarting {next(animation)}', end='', flush=True)
        time.sleep(0.1)
    print('\r', end='', flush=True)

clear_screen()
display_loading_animation()
def banner():
    banner_text = f"""
                   ╔════════════════════════════════════════╗
                   ║   ███████╗██╗   ██╗███████╗ ██████╗    ║      
                   ║   ██╔════╝██║   ██║██╔════╝██╔═══██╗   ║ 
                   ║   ███████╗██║   ██║█████╗  ██║   ██║   ║
                   ║   ╚════██║██║   ██║██╔══╝  ██║   ██║   ║
                   ║   ███████║╚██████╔╝██║     ╚██████╔╝   ║
                   ║   ╚══════╝ ╚═════╝ ╚═╝      ╚═════╝    ║
                   ╚════════════════════════════════════════╝                                                                              
               ╔═════════════════════════════════════════════════╗
               ║ Yes you re-install it each time so deal with it ║
               ╚═════════════════════════════════════════════════╝    
                         ╔══════════════════════════╗       
                         ║ --=[ '1' to Install ]=-- ║
                         ║╔════════════════════════╗║       
                         ║║        [ SUFO ]        ║║
                         ║╚════════════════════════╝║
                         ╚══════════════════════════╝
    """
    return banner_text

def display_page_one():
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    choice = input(">>  ")

    if choice == '1':
        os.system('git clone https://github.com/sherlock-project/sherlock.git')
        os.chdir('sherlock')
        os.system('pip install -r requirements.txt')

def display_page_two():
    clear_screen()
    print("[ENTER]")
    print("[THY]")
    print("[NAME]")
    print(" ")
    name = input(">>  ")
    browse_option = input("Open ALL links in default browser? (y/n): ")

    if browse_option.lower() == 'y':
        command = f'python sherlock "{name}" --timeout 60 --print-found --nsfw --browse'
    else:
        command = f'python sherlock "{name}" --timeout 60 --print-found --nsfw'
    
    subprocess.call(command, shell=True)

if __name__ == "__main__":
    set_console_size(85, 25)
    set_window_title("SUFO")
    clear_screen()
    print(banner())
    
    while True:
        display_page_one()
        display_page_two()
        print(" ")
        print(" ")
        choice = input("['2' Another search]: ")
        display_page_two()
