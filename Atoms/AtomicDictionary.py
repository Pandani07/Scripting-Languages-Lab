def AtomicDictionary():
    elements = {
        "Iron": "Fe",
        "Sulphur": "S",
        "Oxygen": "O",
        "Magnesium": "Mg"
    }
    def add():
        x = str(input("Enter the element name"))
        sy = str(input("Enter the element symbol"))
        elements.update({x: sy})
        print(elements)
    def count():
        number = len(elements.keys())
        print(number)
    def search1():
        search = str(input("Enter the search element"))
        if search in elements.keys():
            print(search, " exists in the dictionary")
        else:
            print(search, " doesn't exist in the dictionary")
    while(True):
        ch = int(input("Enter your choice: 1.Add an element 2.Count number of elements 3.Search for an element 4.Exit"))
        if ch == 1:
            add()
        elif ch == 2:
            count()
        elif ch == 3:
            search1()
        else:
            exit()
