from checkFor import checkFor

def main():
    data = open(r'name.csv')
    for conversation in data:
        result = checkFor(data,r'regex')
    print("test")



if __name__ == "__main__":
    main()