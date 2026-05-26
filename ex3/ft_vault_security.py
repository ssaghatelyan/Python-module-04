def secure_archive(
        filename: str, action: str = "read", content: str = ""
                   ) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(filename, "r") as file:
                data = file.read()
            return (True, data)
        elif action == "write":
            with open(filename, "w") as file:
                file.write(content)
            return (True, "Content successfully written to file")
        else:
            return (False, "Invalid action")
    except Exception as e:
        return (False, e.args[0])


print("=== Cyber Archives Security ===")
print("Using 'secure_archive' to read from a nonexistent file:")
print(secure_archive("/not/existing/file", "read"))
print("Using 'secure_archive' to read from a regular file:")
result = secure_archive("archive.txt")
print(result)
if result[0]:
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("backup.txt", "write", result[1]))
