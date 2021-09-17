command = ""
started = False
while command != "quit":
    command = input("> ")
    if command == "start":
        if started:
            print("Car already started")
        else:
            started = True
            print("Car started.....")
    elif command == "stop":
        if not started:
            print("Car already stopped")
        else:
            started = False
            print("Car stopped.....")
    elif command == "help":
        print("""
        start - Car started
        stop - Car stopped
        command - exit
        """)
    elif command == "quit" or command == "exit":
        print("Car engine damaged.....")
        break
    else:
        print("i dont understand")
