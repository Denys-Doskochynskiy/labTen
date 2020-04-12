class Stadium:
    price_in_millions_of_dollars = 12.5

    def __init__(self, name=None, count_of_spectators=None, country=None,
                 size_of_field_in_square_meters=None,
                 lighting_power_in_lux=None, year_of_foundation=None):
        self.name = name
        self.count_of_spectators = count_of_spectators
        self.country = country
        self.size_of_field_in_square_meters = size_of_field_in_square_meters
        self.lighting_power_in_lux = lighting_power_in_lux
        self.year_of_foundation = year_of_foundation

    @staticmethod
    def staticmethod():
        return Stadium.price_in_millions_of_dollars

    def __str__(self):
        name = "Name: {0}\n".format(self.name)
        count_of_spectators = "Count of spectators: {0}\n".format(self.count_of_spectators)
        country = "Country: {0}\n".format(self.country)
        size_of_field_in_square_meters = "Size of field in square meters: {0}\n".format(
            self.size_of_field_in_square_meters)
        lighting_power_in_lux = "Lighting power in lux: {0}\n".format(self.lighting_power_in_lux)
        year_of_foundation = "Year of foundation: {0}\n".format(self.year_of_foundation)
        price_in_millions_of_dollars = "Price in millions of dollars: {0}\n".format(
            Stadium.price_in_millions_of_dollars)
        return name + count_of_spectators + country + size_of_field_in_square_meters + lighting_power_in_lux + \
               year_of_foundation + price_in_millions_of_dollars

    def __del__(self):
        print("Delete " + self.__class__.__name__ + " | Object ID: " + str(id(self)))
        return
