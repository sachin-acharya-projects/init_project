from colorama import Fore

__all__ = ['Print']

class Print:
    def error(*args):
        print(f"{Fore.LIGHTRED_EX}\033[1m{' '.join(args)}")
    
    def general(*args):
        print(f"{Fore.LIGHTWHITE_EX}\033[1m{' '.join(args)}")

    def progress_st(*args, arrow: str = '> '):
        print(f"{Fore.LIGHTBLUE_EX}\033[1m{arrow}{' '.join(args)}")
        
    def success(*args):
        print(f"{Fore.LIGHTGREEN_EX}\033[1m{' '.join(args)}")
        
    def progress_s(*args, arrow: str = '> '):
        print(f"{Fore.LIGHTCYAN_EX}\033[3m{arrow}{' '.join(args)}")
        
    def code(*args):
        print(f"\033[3M\033[1m{Fore.WHITE}{' '.join(args)}")