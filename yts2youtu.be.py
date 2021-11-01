from os import system
from time import sleep
import sys
import pyperclip

main_menu = """
  Main Menu
_____________

1) Quick Mode
2) Bulk Mode

Ctrl+C for exit or back
_____________
"""

quick_menu = """
  Quick Mode
_____________
"""

def convert(link):
    link = link.split("/")[-1].split("?")[0]
    return f"https://youtu.be/{link}"

def main():
    try:
        system("clear")
        print(main_menu)
        choice = input("Choice ~> ")

        try:
            choice = int(choice)
        except ValueError:
            choice = 0

        if choice == 1:
            try:
                while True:
                    system("clear")
                    print(quick_menu)
                    link = input("Link: ")
                    pyperclip.copy(convert(link))
                    print("\nConverted link copied to clipboard.")
                    sleep(1)
            except KeyboardInterrupt:
                main()

        elif choice == 2:
            try:
                while True:
                    system("clear")
                    print("Processing input file...")
                    # Goes through each line in input.txt and stores converted links in output array
                    output = list()
                    with open("input.txt", 'r') as file:
                        for line in file:
                            output.append(convert(line) + "\n")
                    # Writes each link in output array to output.txt
                    with open("output.txt", "w") as file:
                        for links in output:
                            file.write(links)
                    print("\nFinished.")
                    sleep(1)
                    raise KeyboardInterrupt
            except KeyboardInterrupt:
                main()

        else:
            print("\nPlease enter a valid choice...")
            sleep(2)
            main()

    except KeyboardInterrupt:
        print("\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
