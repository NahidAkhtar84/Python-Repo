def run_command(command: str) -> None:
    match command:
        case "quit":
            print("quiting the program.")
            quit()
        case "reset":
            print("reseting the system...")
        case other:
            print(f"The command: {other!r} is not supported.")


def main()-> None:
    while True:
        command = input("$ ")
        run_command(command)

if __name__ == "__main__":
    main()
