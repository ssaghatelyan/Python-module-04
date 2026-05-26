import sys
import typing

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <file>")
else:
    name = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{name}'")
    try:
        ft: typing.IO[str] = open(name)
        data = ft.read()
        ft.close()
        print("---\n")
        print(f"{data}")
        print("\n---")
        print(f"File '{sys.argv[1]}' closed")
    except FileNotFoundError as e:
        print(f"[STDERR] Error opening file '{name}': {e}", file=sys.stderr)
        print("Data not saved.")
    except PermissionError as e:
        print(f"[STDERR] Error opening file '{name}': {e}", file=sys.stderr)
        print("Data not saved.")
