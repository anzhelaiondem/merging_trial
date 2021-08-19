file_name = "database.db"


# print(file_name)


def is_file(a):
    if a > 10:
        print("File Exists")
        return True
    else:
        print("file doesn't exist")
        return False


def is_table(b):
    if b > 10:
        print("Table Exists")
        return True
    else:
        print("Table doesn't exist")
        return False


a = is_file(0)
b = is_table(0)

if a and b:
    print("Both file and table")
else:
    print("File and/or table doesn't exist")
