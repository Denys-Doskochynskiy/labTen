from src.Stadium import Stadium


def main():
    lvov = Stadium("Lvov", 15750, "Ua", 190.65, 28.65, 1898)
    kharkov = Stadium("Kharkov", 12500, "ua")
    odessa = Stadium()
    stadium = [lvov, kharkov, odessa]
    [print(count_of_object) for count_of_object in stadium]

# print(lvov.__str__())
# print(kharkov.__str__())
# print(odessa.__str__())


if __name__ == "__main__":
    main()
