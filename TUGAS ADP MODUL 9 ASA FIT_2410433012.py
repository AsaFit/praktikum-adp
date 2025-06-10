import time
import os
from termcolor import colored, cprint

os.system('cls')

cprint("     " + colored(" ^^^", "red"))
time.sleep(1)
cprint("     " + colored(" ||| ","yellow"))
time.sleep(1)
cprint("      " + colored("   ","white", "on_red"))
time.sleep(1)
cprint("     " + colored("     ","white", "on_yellow"))
time.sleep(1)
cprint("   " + colored("         ","white", "on_green"))
time.sleep(1)
cprint("  " + colored("           ","white", "on_blue"))
time.sleep(2)
cprint(colored("\n---Selamat Ulang Tahun!---", "white"))

time.sleep(10)