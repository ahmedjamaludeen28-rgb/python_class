import csv

expected = ["name", "age", "email"]
with open ("people.csv", "r") as file:
    a = csv.reader(file)
    h = next(a, None)
    if h is None:
        print("No data in the file")    
    elif [c.lower().strip() for c in h] != expected:
        print("No header found") 

    # h = [column.strip() for column in h]

    # if h == ["name", "age", "email"]:
    #     print("There is a header")
    # else:
    #     print("There is no header")

    # expected = ["name", " age", " email"]

    # if h != expected:
    #     print("There is no header")
    # else:
    #     print("there is header")

    else:
        for r in a:
            if len(r) != 3 or r[0].strip() == "" or r[1].strip() == "" or r[2].strip() == "":
                print("This is a bad line")
                continue
            a,b,c = r
            print(a,b,c)
            