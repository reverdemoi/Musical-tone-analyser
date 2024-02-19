import original as original
from colorama import Fore
from separate import *

def main():
    print(Fore.LIGHTCYAN_EX, "Separating vocals...", Fore.RESET)
    isolatedFilePath = separate("hotandcold.m4a", "songs/test")

    print(isolatedFilePath)
    print("THIS BE ISOLATED")

    print(Fore.LIGHTCYAN_EX, "Analyzing vocals dominant pitches...", Fore.RESET)
    original.main(isolatedFilePath)

if __name__ == "__main__":
    main()