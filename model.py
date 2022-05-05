class Car:
    """
    Class Car.
    A class used to represent a Car.

    Contains attributes:
    :param brand: car's brand
    :type brand: str

    :param model: car's model
    :type model: str

    :param color: car's color
    :type color: str

    :param poduction_year: car's poduction year
    :type poduction_year: int

    :param car_type: car's body type
    :type car_type: str

    :param engine: car's type of engine
    :type engine: str

    :param fuel_consumption: car's fuel consumption
    :type fuel_consumption: float

    :param seats: number of seats in car
    :type seats: int

    :param rent_cost: cost of renting a car for one day
    :type rent_cost: int

    :param id: car's id
    :type id: int

    :param avability: status of avablility
    :type avability: str


    Contains methods:

    new_brand(self, new_brand)
        assigns a new value to the param brand

    new_model(self, new_model)
        assigns a new value to the param model

    new_color(self, new_color)
        assigns a new value to the param color

    new_production_year(self, new_production_year)
        assigns a new value to the param production_year

    new_car_type(self, new_car_type)
        assigns a new value to the param car_type

    new_engine(self, new_engine)
        assigns a new value to the param engine

    new_fuel_consumption(self, new_fuel_consumption)
        assigns a new value to the param fuel_consumption

    new_seats(self, new_seats)
        assigns a new value to the param seats

    new_rent_cost(self, new_rent_cost)
        assigns a new value to the param rent_cost

    new_id(self, new_id)
        assigns a new value to the param id

    new_avability(self, new_avability)
        assigns a new value to the param avability
    """

    def __init__(
        self,
        brand,
        model,
        color,
        production_year,
        car_type,
        engine,
        fuel_consumption,
        seats,
        rent_cost,
        id=None,
        avability="avalible"
    ):
        """
        Constructor.

        Arguments:
            brand,
            model,
            color,
            production_year,
            car_type,
            engine,
            fuel_consumption,
            seats,
            rent_cost,
            id,
            avability
        """
        self._brand = brand
        self._model = model
        self._color = color
        self._production_year = production_year
        self._car_type = car_type
        self._engine = engine
        self._fuel_consumption = fuel_consumption
        self._seats = seats
        self._rent_cost = rent_cost
        self._id = id
        self._avability = avability

    def brand(self):
        return self._brand

    def model(self):
        return self._model

    def color(self):
        return self._color

    def production_year(self):
        return self._production_year

    def car_type(self):
        return self._car_type

    def engine(self):
        return self._engine

    def fuel_consumption(self):
        return self._fuel_consumption

    def seats(self):
        return self._seats

    def rent_cost(self):
        return self._rent_cost

    def id(self):
        return self._id

    def avability(self):
        return self._avability

    def new_brand(self, new_brand):
        self._brand = new_brand

    def new_model(self, new_model):
        self._model = new_model

    def new_color(self, new_color):
        self._color = new_color

    def new_production_year(self, new_production_year):
        self._production_year = new_production_year

    def new_car_type(self, new_car_type):
        self._car_type = new_car_type

    def new_engine(self, new_engine):
        self._engine = new_engine

    def new_fuel_consumption(self, new_fuel_consumption):
        self._fuel_consumption = new_fuel_consumption

    def new_seats(self, new_seats):
        self._seats = new_seats

    def new_rent_cost(self, new_rent_cost):
        self._rent_cost = new_rent_cost

    def new_id(self, new_id):
        self._id = new_id

    def new_avability(self, new_avability):
        self._avability = new_avability


class Booking:
    """
    Class Booking.
    A class used to represent a Booking.

    Contains attributes:
    :param car_id: id of a booked car
    :type car_id: int

    :param car_info: short information about booked car
    :type car_info: str

    :param begin: date when booking starts
    :type begin: date

    :param end: end date of the booking
    :type end: date

    :param booking_id: booking id
    :type booking_id: int

    :param cost: total cost
    :type cost: int


    Contains methods:

    new_car_id(self, new_car_id)
        assigns a new value to the param car_id

    new_car_info(self, new_car_info)
        assigns a new value to the param car_info

    new_begin(self, new_begin)
        assigns a new value to the param begin

    new_end(self, new_end)
        assigns a new value to the param end

    new_booking_id(self, new_booking_id)
        assigns a new value to the param booking_id

    new_cost(self, new_cost)
        assigns a new value to the param cost
    """

    def __init__(self, car_id, car_info, begin, end, booking_id=None, cost=0):
        """
        Constructor.

        Arguments:
            self,
            car_id,
            car_info,
            begin,
            end,
            booking_id,
            cost
        """
        self._car_id = car_id
        self._car_info = car_info
        self._begin = begin
        self._end = end
        self._booking_id = booking_id
        self._cost = cost

    def car_id(self):
        return self._car_id

    def car_info(self):
        return self._car_info

    def begin(self):
        return self._begin

    def end(self):
        return self._end

    def booking_id(self):
        return self._booking_id

    def cost(self):
        return self._cost

    def new_car_id(self, new_car_id):
        self._car_id = new_car_id

    def new_car_info(self, new_car_info):
        self._car_info = new_car_info

    def new_begin(self, new_begin):
        self._begin = new_begin

    def new_end(self, new_end):
        self._end = new_end

    def new_booking_id(self, new_booking_id):
        self._booking_id = new_booking_id

    def new_cost(self, new_cost):
        self._cost = new_cost


class Rental:
    """
    Class Rental.
    A class used to represent a Rental.

    Contains attributes:
    :param car_id: id of a rented car
    :type car_id: int

    :param car_info: short information about rented car
    :type car_info: str

    :param begin: date when rental starts
    :type begin: date

    :param end: end date of the rental
    :type end: date

    :param cost: total cost of renting
    :type cost: int

    :param rent_id: id of a rental
    :type rent_id: int

    :param exceeded: information about exceeded return time
    :type exceeded: int


    Contains methods:

    new_car_id(self, new_car_id)
        assigns a new value to the param car_id

    new_car_info(self, new_car_info)
        assigns a new value to the param car_info

    new_begin(self, new_begin)
        assigns a new value to the param begin

    new_end(self, new_end)
        assigns a new value to the param end

    new_cost(self, new_cost)
        assigns a new value to the param cost

    new_rent_id(self, new_rent_id)
        assigns a new value to the param rent_id

    new_exceeded(self, new_exceeded)
        assigns a new value to the param exceeded
    """

    def __init__(
        self,
        car_id,
        car_info,
        begin,
        end,
        cost,
        rent_id,
        exceeded="no"
    ):
        """
        Constructor.

        Arguments:
            self,
            car_id,
            car_info,
            begin,
            end,
            cost,
            rent_id,
            exceeded
        """
        self._car_id = car_id
        self._car_info = car_info
        self._begin = begin
        self._end = end
        self._cost = cost
        self._rent_id = rent_id
        self._exceeded = exceeded

    def car_id(self):
        return self._car_id

    def car_info(self):
        return self._car_info

    def begin(self):
        return self._begin

    def end(self):
        return self._end

    def cost(self):
        return self._cost

    def rent_id(self):
        return self._rent_id

    def exceeded(self):
        return self._exceeded

    def new_car_id(self, new_car_id):
        self._car_id = new_car_id

    def new_car_info(self, new_car_info):
        self._car_info = new_car_info

    def new_begin(self, new_begin):
        self._begin = new_begin

    def new_end(self, new_end):
        self._end = new_end

    def new_cost(self, new_cost):
        self._cost = new_cost

    def new_rent_id(self, new_rent_id):
        self._rent_id = new_rent_id

    def new_exceeded(self, new_exceeded):
        self._exceeded = new_exceeded
