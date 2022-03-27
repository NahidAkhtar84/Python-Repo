from fileinput import filename


def run_command(command: str) -> None:
    match command.split():
        case ["load", filename]:
            print(f"Loading the file name, {filename}")
        case ["reset", filename]:
            print(f"Resetting the file name, {filename}")
        case ["exit" | "quit" | "bye", *rest]:
            if "-f" in rest:
                print("Clearing the code base and quiting...")
            else:
                print("Quiting the program...")
            quit()
        case _:
            print("Unknown command!")


def main()-> None:
    while True:
        command = input("$ ")
        run_command(command)

if __name__ == "__main__":
    main()
