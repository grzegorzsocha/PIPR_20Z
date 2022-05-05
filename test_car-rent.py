from model import Car, Rental, Booking
from datetime import date
import operations as op


def test_model_car_new_brand():
    car = Car("ford", "c-max", "blue", 2004, "estate", "petrol", 7.5, 5, 45, 7)
    car.new_brand("bmw")
    assert car.brand() == "bmw"


def test_model_car_new_model():
    car = Car("ford", "c-max", "blue", 2004, "estate", "petrol", 7.5, 5, 45, 7)
    car.new_model("x2")
    assert car.model() == "x2"


def test_model_car_new_color():
    car = Car("ford", "c-max", "blue", 2004, "estate", "petrol", 7.5, 5, 45, 7)
    car.new_color("red")
    assert car.color() == "red"


def test_model_car_new_production_year():
    car = Car("ford", "c-max", "blue", 2004, "estate", "petrol", 7.5, 5, 45, 7)
    car.new_production_year(2003)
    assert car.production_year() == 2003


def test_model_car_new_type():
    car = Car("ford", "c-max", "blue", 2004, "estate", "petrol", 7.5, 5, 45, 7)
    car.new_car_type("suv")
    assert car.car_type() == "suv"


def test_model_car_new_engine():
    car = Car("ford", "c-max", "blue", 2004, "estate", "petrol", 7.5, 5, 45, 7)
    car.new_engine("diesel")
    assert car.engine() == "diesel"


def test_model_car_new_fuel_consumption():
    car = Car("ford", "c-max", "blue", 2004, "estate", "petrol", 7.5, 5, 45, 7)
    car.new_fuel_consumption(10)
    assert car.fuel_consumption() == 10.0


def test_model_car_new_seats():
    car = Car("ford", "c-max", "blue", 2004, "estate", "petrol", 7.5, 5, 45, 7)
    car.new_seats(7)
    assert car.seats() == 7


def test_model_car_new_rent_cost():
    car = Car("ford", "c-max", "blue", 2004, "estate", "petrol", 7.5, 5, 45, 7)
    car.new_rent_cost(50)
    assert car.rent_cost() == 50


def test_model_car_new_avability():
    car = Car("ford", "c-max", "blue", 2004, "estate", "petrol", 7.5, 5, 45, 7)
    car.new_avability("rented")
    assert car.avability() == "rented"


def test_model_car_new_id():
    car = Car("ford", "c-max", "blue", 2004, "estate", "petrol", 7.5, 5, 45, 7)
    car.new_id(3)
    assert car.id() == 3


def test_model_booking_new_car_id():
    booking = Booking(7, "ferrari f40", "2021-10-27", "2021-12-17", 4, 2000)
    booking.new_car_id(3)
    assert booking.car_id() == 3


def test_model_booking_new_car_info():
    booking = Booking(7, "ferrari f40", "2021-10-27", "2021-12-17", 4, 2000)
    booking.new_car_info("bmw z4")
    assert booking.car_info() == "bmw z4"


def test_model_booking_new_begin():
    booking = Booking(7, "ferrari f40", "2021-10-27", "2021-12-17", 4, 2000)
    booking.new_begin(2021-12-17)
    assert booking.begin() == 2021-12-17


def test_model_booking_new_end():
    booking = Booking(7, "ferrari f40", "2021-10-27", "2021-12-17", 4, 2000)
    booking.new_end(2021-12-30)
    assert booking.end() == 2021-12-30


def test_model_booking_new_booking_id():
    booking = Booking(7, "ferrari f40", "2021-10-27", "2021-12-17", 4, 2000)
    booking.new_booking_id(5)
    assert booking.booking_id() == 5


def test_model_booking_new_cost():
    booking = Booking(7, "ferrari f40", "2021-10-27", "2021-12-17", 4, 2000)
    booking.new_cost(500)
    assert booking.cost() == 500


def test_model_rental_new_car_id():
    rental = Rental(1, "ferrari 458", "2021-10-27", "2021-12-17", 100, 1)
    rental.new_car_id(3)
    assert rental.car_id() == 3


def test_model_rental_new_car_info():
    rental = Rental(1, "ferrari 458", "2021-10-27", "2021-12-17", 100, 1)
    rental.new_car_info("bmw z4")
    assert rental.car_info() == "bmw z4"


def test_model_rental_new_begin():
    rental = Rental(1, "ferrari 458", "2021-10-27", "2021-12-17", 100, 1)
    rental.new_begin(2021-12-17)
    assert rental.begin() == 2021-12-17


def test_model_rental_new_end():
    rental = Rental(1, "ferrari 458", "2021-10-27", "2021-12-17", 100, 1)
    rental.new_end(2021-12-30)
    assert rental.end() == 2021-12-30


def test_model_rental_new_rent_id():
    rental = Rental(1, "ferrari 458", "2021-10-27", "2021-12-17", 100, 1)
    rental.new_rent_id(5)
    assert rental.rent_id() == 5


def test_model_rental_new_cost():
    rental = Rental(1, "ferrari 458", "2021-10-27", "2021-12-17", 100, 1)
    rental.new_cost(500)
    assert rental.cost() == 500


def test_op_get_menu_options():
    output = op.get_menu_options()
    expected_output = "\nPlease choose your action."
    expected_output += "\n1. Search for a car.\n2. Show car edit options."
    expected_output += "\n3. Show booking options.\n4. Show rental options."
    expected_output += "\n5. Show database options.\n6. Exit Car-Rent."
    assert output == expected_output


def test_op_get_editing_options():
    output = op.get_editing_options()
    expected_output = "\nWhat would u like to do?"
    expected_output += "\n1. Add new car.\n2. Edit existing car."
    expected_output += "\n3. Delete existing car.\n4. Back to main menu."
    assert output == expected_output


def test_op_get_booking_options():
    output = op.get_booking_options()
    expected_output = "\nWhat would u like to do?"
    expected_output += "\n1. Book a car.\n2. Modify existing booking."
    expected_output += "\n3. Cancel a booking.\n4. Back to main menu."
    assert output == expected_output


def test_op_get_rental_options():
    output = op.get_rental_options()
    expected_output = "\nWhat would u like to do?"
    expected_output += "\n1. Pick up a booking."
    expected_output += "\n2. Rent car without previous booking."
    expected_output += "\n3. Return rented car."
    expected_output += "\n4. Show rentals that exceeded their rental time."
    expected_output += "\n5. Back to main menu."
    assert output == expected_output


def test_op_get_open_database():
    output = op.get_open_database()
    expected_output = "\nWhat would u like to do?"
    expected_output += "\n1. Show car list.\n2. Show booking list."
    expected_output += "\n3. Show rental list.\n4. Back to main menu."
    assert output == expected_output


def test_op_get_search_options():
    output = op.get_search_options()
    expected_output = "\nBy which parametr would you like to search for a car?"
    expected_output += "\n1. Id.\n2. Brand\n3. Model.\n4. Color."
    expected_output += "\n5. Production year.\n6. Type."
    expected_output += "\n7. Engine.\n8. Fuel consumption."
    expected_output += "\n9. Number of seats.\n10. Rent cost"
    expected_output += "\n11. Avablility status.\n12. Back to main menu."
    assert output == expected_output


def test_op_get_edit_param_of_car_options():
    output = op.get_edit_param_of_car_options()
    expected_output = "\nWhat parametr of a car would you like to change?"
    expected_output += "\n1. Brand.\n2. Model.\n3. Color."
    expected_output += "\n4. Production year.\n5. Type\n6. Engine."
    expected_output += "\n7. Fuel consumption.\n8. Number of seats."
    expected_output += "\n9. Rent cost.\n10. Back to edit menu."
    assert output == expected_output


def test_op_get_car_headline():
    output = op.get_car_headline()
    expected_output = "-" * 163
    expected_output += "\n| Id  |     Brand      |    Model     |   Color    |"
    expected_output += " Production year |      Type      |   Engine   |"
    expected_output += " Fuel consumption | Number of seats |"
    expected_output += " Rent cost |  Avability  |\n"
    expected_output += "-" * 163
    assert output == expected_output


def test_op_get_booking_headline():
    output = op.get_booking_headline()
    expected_output = "-" * 79
    expected_output += "\n| Booking id | Car id |      Car info      "
    expected_output += "|    From    |     To     |  Cost  |\n"
    expected_output += "-" * 79
    assert output == expected_output


def test_op_get_rental_headline():
    output = op.get_rental_headline()
    expected_output = "-" * 90
    expected_output += "\n| Rental id  | Car id |      Car info      |"
    expected_output += "    From    |     To     |  Cost  | Exceeded |\n"
    expected_output += "-" * 90
    assert output == expected_output


def test_op_get_car():
    car = Car("ford", "c-max", "blue", 2004, "estate", "petrol", 7.5, 5, 45, 7)
    output = op.get_car(car)
    expected_output = "|  7  |      ford      |    c-max     |    blue    |"
    expected_output += "      2004       |     estate     |   petrol   |"
    expected_output += "       7.5        |        5        |"
    expected_output += "    45     |  avalible   |"
    assert output == expected_output


def test_op_get_booking():
    booking = Booking(7, "ferrari f40", "2021-10-27", "2021-12-17", 4, 2000)
    output = op.get_booking(booking)
    expected_output = "|     4      |   7    |    ferrari f40     |"
    expected_output += " 2021-10-27 | 2021-12-17 |  2000  |"
    assert output == expected_output


def test_op_get_rental():
    rental = Rental(1, "ferrari 458", "2021-10-27", "2021-12-17", 100, 1)
    output = op.get_rental(rental)
    expected_output = "|     1      |   1    |    ferrari 458     |"
    expected_output += " 2021-10-27 | 2021-12-17 |  100   |    no    |"
    assert output == expected_output


def test_get_brand(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "bmw")
    expected_brand = op.get_brand("")
    assert expected_brand == "bmw"


def test_get_model(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "x6")
    expected_model = op.get_model("")
    assert expected_model == "x6"


def test_get_color(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "red")
    expected_color = op.get_color("")
    assert expected_color == "red"


def test_get_production_year(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "2003")
    expected_production_year = op.get_production_year("")
    assert expected_production_year == 2003


def test_get_type(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "suv")
    expected_type = op.get_type("")
    assert expected_type == "suv"


def test_get_engine(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "diesel")
    expected_engine = op.get_engine("")
    assert expected_engine == "diesel"


def test_get_fuel_consumption(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "7")
    expected_fuel_consumption = op.get_fuel_consumption("")
    assert expected_fuel_consumption == 7.0


def test_get_seats(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "5")
    expected_seats = op.get_seats("")
    assert expected_seats == 5


def test_get_cost(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "2000")
    expected_cost = op.get_cost("")
    assert expected_cost == 2000


def test_get_begin(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "2021-10-27")
    expected_begin = op.get_begin()
    assert str(expected_begin) == "2021-10-27"


def test_get_end(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "2021-10-27")
    expected_end = op.get_end()
    assert str(expected_end) == "2021-10-27"


def test_avability_check_false():
    booking_list = []
    bkn_begin = date(2021, 1, 12)
    bkn_end = date(2021, 1, 19)
    booking = Booking(7, "ford fiesta", bkn_begin, bkn_end)
    booking_list.append(booking)
    begin = date(2021, 1, 20)
    end = date(2021, 1, 30)
    expected_result = op.avability_check(booking_list, begin, end, 7)
    assert expected_result is False


def test_avability_check_true():
    booking_list = []
    bkn_begin = date(2021, 1, 12)
    bkn_end = date(2021, 1, 21)
    booking = Booking(7, "ford fiesta", bkn_begin, bkn_end)
    booking_list.append(booking)
    begin = date(2021, 1, 20)
    end = date(2021, 1, 30)
    expected_result = op.avability_check(booking_list, begin, end, 7)
    assert expected_result is True


def test_avability_check_empty_list():
    begin = date(2021, 1, 20)
    end = date(2021, 1, 30)
    expected_result = op.avability_check([], begin, end, 7)
    assert expected_result is False
