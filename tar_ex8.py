import os
def soldier(pathh, fil, form):
    with open(fil) as f:
        files_lst = f.read().split("\n")
    count = 1
    os.chdir(pathh)
    files = os.listdir(pathh)

    for file in files:
        if file not in files_lst:
            os.rename(file, file.capitalize())
        if os.path.splitext(file)[1] == form:
            os.rename(file, f"{count}.{form}")
            count = count + 1


if __name__ == '__main__':
    pathe = input("Enter path")
    # forms  = input("Enter format")
    soldier(pathe, "detail.txt", ".png")
