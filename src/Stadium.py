class Stadium:
    price_in_millions_of_dollars = 12.5

    def __init__(self, name=None, __count_of_spectators__=None, country=None,
                 size_of_field_in_square_meters=None,
                 lighting_power_in_lux=None, year_of_foundation=None):
        self.name = name
        self.count_of_spectators = __count_of_spectators__
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

#################################################
    def get_name(self):
        return self.name

    def set_country(self, name):
        self.name = name

#################################################
    def get_country(self):
        return self.country

    def set_country(self, country):
        self.country = country

#################################################
    def get_count_of_spectators(self):
        return self.count_of_spectators

    def set_count_of_spectators(self, count_of_spectators):
        self.count_of_spectators = count_of_spectators

#################################################
    def get_size_of_field_in_square_meters(self):
        return self.size_of_field_in_square_meters

    def set_size_of_field_in_square_meters(self, size_of_field_in_square_meters):
        self.size_of_field_in_square_meters = size_of_field_in_square_meters

#################################################
    def get_lighting_power_in_lux(self):
        return self.lighting_power_in_lux

    def set_lighting_power_in_lux(self, lighting_power_in_lux):
        self.lighting_power_in_lux = lighting_power_in_lux

#################################################
    def get_year_of_foundation(self):
        return self.year_of_foundation

    def set_year_of_foundation(self, year_of_foundation):
        self.year_of_foundation = year_of_foundation
#################################################
