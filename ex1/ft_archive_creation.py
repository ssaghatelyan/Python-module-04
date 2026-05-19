import sys
import typing


if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <file>")
else:
    name = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{name}'")
    try:
        ft: typing.IO = open(name)
        data = ft.read()
        ft.close()
        print("---\n")
        print(data)
        print("\n---")
        print(f"File '{sys.argv[1]}' closed")

        lines = data.strip().split("\n")
        new_lines = []
        for line in lines:
            new_lines += [line + "#"]
        new_data = "\n".join(new_lines)
        print("Transform data:\n---\n")
        print(new_data)
        print("---")

        new_file = input("Enter new file name (or empty): ")
        if new_file == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_file}'")
            ft1: typing.IO = open(new_file, "w")
            ft1.write(new_data + "\n")
            ft1.close()
            print(f"Data saved in file '{new_file}'.")

    except (FileNotFoundError, PermissionError) as e:
        print(f"[STDERR] Error opening file '{name}': {e}", file=sys.stderr)
        print("Data not saved.")
    
    finally:
        close()
