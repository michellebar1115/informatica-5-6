def main():

    tasks = [] #Empty list
    # tasks = [""] 1 Element, so not this one

    while True: # this is the same as: "command != "exit":"
        print(f"Tasks to do: {len(tasks)}")
        command = input("What do you want to do? (add, complete, or exit): ").lower().strip()
        if command == "add":
            new_task = input("Enter new task: ")
            tasks.append(new_task)
        elif command == "complete":
            option = input("Are you completing one or all? ").strip().lower()
            if option == "one":
                completed = input("Enter completed task: ")
                tasks.remove(completed)
            elif option == "all":
                tasks.clear()
            else:
                print("Please choose all or one.")
        elif command == "exit":
            break
        else:
            print("Please choose one of the options")


if __name__ == "__main__":
    main()
