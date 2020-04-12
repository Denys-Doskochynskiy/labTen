from src.Stadium import Stadium


def main():
    lvov = Stadium("Lvov", 15750, "Ua", 190.65, 28.65, 1898)
    kharkov = Stadium("Kharkov", 12500, "ua", 10500, 16.05, 1990)
    odessa = Stadium("Odessa", 10000, "Ua", 900.5, 29.75, 2005)
    print(lvov.__str__())
    print(kharkov.__str__())
    print(odessa.__str__())


if __name__ == "__main__":
    main()
