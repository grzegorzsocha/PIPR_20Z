from model import Car, Rental, Booking
from switchcase import switch
from datetime import date, datetime
import subprocess
import json


today = date.today()
file_paths = ["cars_data.json", "rentals_data.json", "bookings_data.json"]


class Database:
    """
    Class Database.
    A class used to storage data.

    Contains attributes:
    :param cars: list of cars
    :type cars: list

    :param rentals: list of rentals
    :type rentals: list

    :param bookings: list of bookings
    :type bookings: list
    """
    def __init__(self):
        self.cars = []
        self.rentals = []
        self.bookings = []

    def load_cars_from_file(self, path):
        """
        Function used to load Car objects from file
        to car list.
        """
        try:
            with open(path, 'r') as file_handle:
                self.cars = read_cars_from_file(file_handle)
        except json.decoder.JSONDecodeError:
            print(f'Cannot read from file {path}')

    def save_cars_to_file(self, path):
        """
        Function used to save Car objects to file
        from car list.
        """
        with open(path, 'w')as file_handle:
            write_cars_to_file(file_handle, self.cars)

    def load_rentals_from_file(self, path):
        """
        Function used to load Rental objects from file
        to rental list.
        """
        try:
            with open(path, 'r') as file_handle:
                self.rentals = read_rentals_from_file(file_handle)
        except json.decoder.JSONDecodeError:
            print(f'Cannot read from file {path}')

    def save_rentals_to_file(self, path):
        """
        Function used to save Rental objects to file
        from rental list.
        """
        with open(path, 'w')as file_handle:
            write_rentals_to_file(file_handle, self.rentals)

    def load_bookings_from_file(self, path):
        """
        Function used to load Booking objects from file
        to booking list.
        """
        try:
            with open(path, 'r') as file_handle:
                self.bookings = read_bookings_from_file(file_handle)
        except json.decoder.JSONDecodeError:
            print(f'Cannot read from file {path}')

    def save_bookings_to_file(self, path):
        """
        Function used to save Booking objects to file
        from booking list.
        """
        with open(path, 'w')as file_handle:
            write_bookings_to_file(file_handle, self.bookings)


def load_data(database, file_paths):
    """
        Function used to load data from files
        to car, rental and booking list.
        If it doesn't find the file,
        it returns an appropriate message.
    """
    try:
        database.load_cars_from_file(file_paths[0])
    except FileNotFoundError:
        print(f'File {file_paths[0]} not found.')
    except PermissionError:
        print(f'You have no permission to opern {file_paths[0]} file.')
    try:
        database.load_rentals_from_file(file_paths[1])
    except FileNotFoundError:
        print(f'File {file_paths[1]} not found.')
    except PermissionError:
        print(f'You have no permission to opern {file_paths[1]} file.')
    try:
        database.load_bookings_from_file(file_paths[2])
    except FileNotFoundError:
        print(f'File {file_paths[2]} not found.')
    except PermissionError:
        print(f'You have no permission to opern {file_paths[2]} file.')


def save_data(database, file_paths):
    """
        Function used to save data to files
        from car, rental and booking list.
    """
    database.save_cars_to_file(file_paths[0])
    database.save_rentals_to_file(file_paths[1])
    database.save_bookings_to_file(file_paths[2])


def read_cars_from_file(file_handle):
    """
        Function used to load car data from file,
        create Car objects and add it to car list.
    """
    cars = []
    data = json.load(file_handle)
    for item in data:
        brand = item['brand']
        model = item['model']
        color = item['color']
        production_year = item['production_year']
        car_type = item['car_type']
        engine = item['engine']
        fuel_consumption = item['fuel_consumption']
        seats = item['seats']
        rent_cost = item['rent_cost']
        avability = item['avability']
        id = item['id']
        car = Car(
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
        )
        cars.append(car)
    return cars


def write_cars_to_file(file_handle, cars):
    """
        Function used to save Car objects to file.
    """
    data = []
    for car in cars:
        brand = car.brand()
        model = car.model()
        color = car.color()
        production_year = car.production_year()
        car_type = car.car_type()
        engine = car.engine()
        fuel_consumption = car.fuel_consumption()
        seats = car.seats()
        rent_cost = car.rent_cost()
        avability = car.avability()
        id = car.id()
        car_data = {
            'brand': brand,
            'model': model,
            'color': color,
            'production_year': production_year,
            'car_type': car_type,
            'engine': engine,
            'fuel_consumption': fuel_consumption,
            'seats': seats,
            'rent_cost': rent_cost,
            'id': id,
            'avability': avability
        }
        data.append(car_data)
    json.dump(data, file_handle, indent=4)


def read_rentals_from_file(file_handle):
    """
        Function used to load rental data from file,
        create Rental objects and add it to rental list.
        If there is a rental that has already ended and
        hadn't been returned before it will change its exceeded
        parameter to positive.
    """
    rentals = []
    data = json.load(file_handle)
    for item in data:
        car_id = item['car_id']
        car_info = item['car_info']
        begin = item['begin']
        begin = datetime.strptime(begin, "%Y-%m-%d").date()
        end = item['end']
        end = datetime.strptime(end, "%Y-%m-%d").date()
        cost = item['cost']
        rent_id = item['rent_id']
        exceeded = item['exceeded']
        rental = Rental(
            car_id,
            car_info,
            begin,
            end,
            cost,
            rent_id,
            exceeded
        )
        if today > rental.end():
            rental.new_exceeded("yes")
        rentals.append(rental)
    return rentals


def write_rentals_to_file(file_handle, rentals):
    """
        Function used to save Rental objects to file.
    """
    data = []
    for rental in rentals:
        car_id = rental.car_id()
        car_info = rental.car_info()
        begin = rental.begin()
        begin = str(begin)
        end = rental.end()
        end = str(end)
        cost = rental.cost()
        rent_id = rental.rent_id()
        exceeded = rental.exceeded()
        rental_data = {
            'car_id': car_id,
            'car_info': car_info,
            'begin': begin,
            'end': end,
            'cost': cost,
            'rent_id': rent_id,
            'exceeded': exceeded,
        }
        data.append(rental_data)
    json.dump(data, file_handle, indent=4)


def read_bookings_from_file(file_handle):
    """
        Function used to load booking data from file,
        create Booking objects and add it to booking list.
        If there is a booking that start date had passed
        and hadn't been picked up it won't add it to booking list.
    """
    bookings = []
    data = json.load(file_handle)
    for item in data:
        car_id = item['car_id']
        car_info = item['car_info']
        begin = item['begin']
        begin = datetime.strptime(begin, "%Y-%m-%d").date()
        end = item['end']
        end = datetime.strptime(end, "%Y-%m-%d").date()
        booking_id = item['booking_id']
        cost = item['cost']
        booking = Booking(
            car_id,
            car_info,
            begin,
            end,
            booking_id,
            cost
        )
        if today <= booking.begin():
            bookings.append(booking)
    return bookings


def write_bookings_to_file(file_handle, bookings):
    """
        Function used to save Booking objects to file.
    """
    data = []
    for booking in bookings:
        car_id = booking.car_id()
        car_info = booking.car_info()
        begin = booking.begin()
        begin = str(begin)
        end = booking.end()
        end = str(end)
        booking_id = booking.booking_id()
        cost = booking.cost()
        booking_data = {
            'car_id': car_id,
            'car_info': car_info,
            'begin': begin,
            'end': end,
            'booking_id': booking_id,
            'cost': cost
        }
        data.append(booking_data)
    json.dump(data, file_handle, indent=4)


def clear():
    """
        Function used to clear terminal window.
    """
    subprocess.call("clear")


def get_menu_options():
    """
        Function used to get main menu options.
    """
    output = "\nPlease choose your action."
    output += "\n1. Search for a car.\n2. Show car edit options."
    output += "\n3. Show booking options.\n4. Show rental options."
    output += "\n5. Show database options.\n6. Exit Car-Rent."
    return output


def get_editing_options():
    """
        Function used to get editing menu options.
    """
    output = "\nWhat would u like to do?"
    output += "\n1. Add new car.\n2. Edit existing car."
    output += "\n3. Delete existing car.\n4. Back to main menu."
    return output


def get_booking_options():
    """
        Function used to get booking menu options.
    """
    output = "\nWhat would u like to do?"
    output += "\n1. Book a car.\n2. Modify existing booking."
    output += "\n3. Cancel a booking.\n4. Back to main menu."
    return output


def get_rental_options():
    """
        Function used to get rental menu options.
    """
    output = "\nWhat would u like to do?"
    output += "\n1. Pick up a booking."
    output += "\n2. Rent car without previous booking.\n3. Return rented car."
    output += "\n4. Show rentals that exceeded their rental time."
    output += "\n5. Back to main menu."
    return output


def get_open_database():
    """
        Function used to get database menu options.
    """
    output = "\nWhat would u like to do?"
    output += "\n1. Show car list.\n2. Show booking list."
    output += "\n3. Show rental list.\n4. Back to main menu."
    return output


def get_search_options():
    """
        Function used to get search menu options.
    """
    output = "\nBy which parametr would you like to search for a car?"
    output += "\n1. Id.\n2. Brand\n3. Model.\n4. Color.\n5. Production year."
    output += "\n6. Type.\n7. Engine.\n8. Fuel consumption."
    output += "\n9. Number of seats.\n10. Rent cost"
    output += "\n11. Avablility status.\n12. Back to main menu."
    return output


def get_edit_param_of_car_options():
    """
        Function used to get editing options.
    """
    output = "\nWhat parametr of a car would you like to change?"
    output += "\n1. Brand.\n2. Model.\n3. Color.\n4. Production year."
    output += "\n5. Type\n6. Engine.\n7. Fuel consumption."
    output += "\n8. Number of seats.\n9. Rent cost.\n10. Back to edit menu."
    return output


def get_modify_booking_options():
    """
        Function used to get booking modification options.
    """
    output = "\nWhat parametr of a booking would you like to change?"
    output += "\n1. Start date.\n2. End date.\n3. Back to booking menu."
    return output


def get_car_headline():
    """
        Function used to get headline for car list.
    """
    brand = "Brand"
    model = "Model"
    color = "Color"
    year = "Production year"
    tp = "Type"
    engine = "Engine"
    fuel_con = "Fuel consumption"
    seats = "Number of seats"
    cost = "Rent cost"
    avab = "Avability"
    id = "Id"
    output = "-" * 163
    output += f"\n|{id:^5}|{brand:^16}|{model:^14}|{color:^12}|"
    output += f"{year:^17}|{tp:^16}|{engine:^12}|{fuel_con:^18}|"
    output += f"{seats:^17}|{cost:^11}|{avab:^13}|\n"
    output += "-" * 163
    return output


def get_booking_headline():
    """
        Function used to get headline for booking list.
    """
    id = "Booking id"
    car_id = "Car id"
    info = "Car info"
    begin = "From"
    end = "To"
    cost = "Cost"
    output = "-" * 79
    output += f"\n|{id:^12}|{car_id:^8}|{info:^20}|"
    output += f"{begin:^12}|{end:^12}|{cost:^8}|\n"
    output += "-" * 79
    return output


def get_rental_headline():
    """
        Function used to get headline for rental list.
    """
    id = "Rental id"
    car_id = "Car id"
    info = "Car info"
    begin = "From"
    end = "To"
    cost = "Cost"
    exceeded = "Exceeded"
    output = "-" * 90
    output += f"\n|{id:^12}|{car_id:^8}|{info:^20}|"
    output += f"{begin:^12}|{end:^12}|{cost:^8}|{exceeded:^10}|\n"
    output += "-" * 90
    return output


def get_car(car):
    """
        Function used to get car info.
    """
    brand = car.brand()
    model = car.model()
    color = car.color()
    year = car.production_year()
    tp = car.car_type()
    engine = car.engine()
    fuel_con = car.fuel_consumption()
    seats = car.seats()
    cost = car.rent_cost()
    avab = car.avability()
    id = car.id()
    output = f"|{id:^5}|{brand:^16}|{model:^14}|{color:^12}|"
    output += f"{year:^17}|{tp:^16}|{engine:^12}|{fuel_con:^18}|"
    output += f"{seats:^17}|{cost:^11}|{avab:^13}|"
    return output


def get_booking(booking):
    """
        Function used to get booking info.
    """
    id = booking.booking_id()
    car_id = booking.car_id()
    info = booking.car_info()
    begin = str(booking.begin())
    end = str(booking.end())
    cost = booking.cost()
    output = f"|{id:^12}|{car_id:^8}|{info:^20}|"
    output += f"{begin:^12}|{end:^12}|{cost:^8}|"
    return output


def get_rental(rental):
    """
        Function used to get rental info.
    """
    id = rental.rent_id()
    car_id = rental.car_id()
    info = rental.car_info()
    begin = str(rental.begin())
    end = str(rental.end())
    cost = rental.cost()
    exceeded = rental.exceeded()
    output = f"|{id:^12}|{car_id:^8}|{info:^20}|"
    output += f"{begin:^12}|{end:^12}|{cost:^8}|{exceeded:^10}|"
    return output


def print_car_list(car_list):
    """
        Function used to print car list.
    """
    print(get_car_headline())
    for car in car_list:
        print(get_car(car))
    print("-"*163)


def print_booking_list(booking_list):
    """
        Function used to print booking list.
    """
    print(get_booking_headline())
    for booking in booking_list:
        print(get_booking(booking))
    print("-"*79)


def print_rental_list(rental_list):
    """
        Function used to print rental list.
    """
    print(get_rental_headline())
    for rental in rental_list:
        print(get_rental(rental))
    print("-"*90)


def main_menu(data_lists):
    """
        Function used to show main menu and waiting
        for user to input action he want to choose.
        After obtaining correct action it goes to choosen function.
    """
    print(get_menu_options())
    action = input()
    clear()
    for case in switch(action):
        if case("1"):
            searching(data_lists, [], [])
            break
        if case("2"):
            editing(data_lists)
            break
        if case("3"):
            booking(data_lists)
            break
        if case("4"):
            renting(data_lists)
            break
        if case("5"):
            open_database(data_lists)
            break
        if case("6"):
            print("\nGoodbye.\n")
            break
    else:
        print("Invalid input. Please choose your action again.")
        main_menu(data_lists)


def searching(data_lists, new_list, past_search):
    """
        Function used to search car by its parameters.
        It allows user to narrow the search by adding another parametr,
        however it doesn't allow user to narrow the search
        by adding multiple times the same parameter.
    """
    if len(new_list) == 0:
        new_list = data_lists[0]
    search_list = []
    print(get_search_options())
    while True:
        action = input()
        clear()
        if action in past_search:
            print("You have already searched by this parametr")
            print("Please choose your new searching parametr again.")
            print(get_search_options())
        else:
            past_search.append(action)
            break
    for case in switch(action):
        if case("1"):
            while True:
                try:
                    param = int(input("Enter id to search by it.\n"))
                    break
                except ValueError:
                    clear()
                    print("Incorrect input type. Please try again.\n")
            for car in new_list:
                if param == car.id():
                    search_list.append(car)
            searching_show_list(data_lists, search_list, past_search)
            break
        if case("2"):
            param = input("Enter brand to search by it.\n")
            for car in new_list:
                if param == car.brand():
                    search_list.append(car)
            searching_show_list(data_lists, search_list, past_search)
            break
        if case("3"):
            param = input("Enter model to search by it.\n")
            for car in new_list:
                if param == car.model():
                    search_list.append(car)
            searching_show_list(data_lists, search_list, past_search)
            break
        if case("4"):
            param = input("Enter color to search by it.\n")
            for car in new_list:
                if param == car.color():
                    search_list.append(car)
            searching_show_list(data_lists, search_list, past_search)
            break
        if case("5"):
            while True:
                try:
                    inp = input("Enter production year to search by it.\n")
                    param = int(inp)
                    break
                except ValueError:
                    clear()
                    print("Incorrect input type. Please try again.\n")
            for car in new_list:
                if param == car.production_year():
                    search_list.append(car)
            searching_show_list(data_lists, search_list, past_search)
            break
        if case("6"):
            param = input("Enter car type to search by it.\n")
            for car in new_list:
                if param == car.car_type():
                    search_list.append(car)
            searching_show_list(data_lists, search_list, past_search)
            break
        if case("7"):
            param = input("Enter engine type to search by it.\n")
            for car in new_list:
                if param == car.engine():
                    search_list.append(car)
            searching_show_list(data_lists, search_list, past_search)
            break
        if case("8"):
            while True:
                try:
                    inp = input("Enter fuel consumption to search by it.\n")
                    param = float(inp)
                    break
                except ValueError:
                    clear()
                    print("Incorrect input type. Please try again.\n")
            for car in new_list:
                if param == car.fuel_consumption():
                    search_list.append(car)
            searching_show_list(data_lists, search_list, past_search)
            break
        if case("9"):
            while True:
                try:
                    inp = input("Enter number of seats to search by it.\n")
                    param = int(inp)
                    break
                except ValueError:
                    clear()
                    print("Incorrect input type. Please try again.\n")
            for car in new_list:
                if param == car.seats():
                    search_list.append(car)
            searching_show_list(data_lists, search_list, past_search)
            break
        if case("10"):
            while True:
                try:
                    inp = input("Enter cost of rent to search by it.\n")
                    param = int(inp)
                    break
                except ValueError:
                    clear()
                    print("Incorrect input type. Please try again.\n")
            for car in new_list:
                if param == car.rent_cost():
                    search_list.append(car)
            searching_show_list(data_lists, search_list, past_search)
            break
        if case("11"):
            param = input("Enter avablility status to search by it.\n")
            for car in new_list:
                if param == car.avability():
                    search_list.append(car)
            searching_show_list(data_lists, search_list, past_search)
            break
        if case("12"):
            main_menu(data_lists)
            break
    else:
        print("Invalid input, try again.")
        searching(data_lists, search_list, past_search)


def searching_show_list(data_lists, search_list, past_search):
    """
    Function used to print list with found cars if search was successful,
    otherwise, it prints an message about unsuccessful searching.
    """
    clear()
    if len(search_list) > 0:
        print_car_list(search_list)
        search_by_new_parametr(data_lists, search_list, past_search)
    else:
        print("0 cars found.")
        searching(data_lists, [], [])


def search_by_new_parametr(data_lists, search_list, past_search):
    """
    Function used to ask user whether he wants to
    add another parametr to search.
    If input is negative, it get back to main menu.
    """
    repeat = input("Do you want to add another parametr to search (y/n)?\n")
    clear()
    for case in switch(repeat):
        if case("y"):
            searching(data_lists, search_list, past_search)
            break
        if case("n"):
            main_menu(data_lists)
            break
    else:
        print("Invalid input, try again.")
        search_by_new_parametr(data_lists, search_list, past_search)


def editing(data_lists):
    """
        Function used to show editing menu and waiting
        for user to input action he want to choose.
        After obtaining correct action it goes to choosen function.
    """
    print(get_editing_options())
    action = input()
    clear()
    for case in switch(action):
        if case("1"):
            adding_new_car(data_lists)
            break
        if case("2"):
            editing_car(data_lists)
            break
        if case("3"):
            delete_car(data_lists)
            break
        if case("4"):
            main_menu(data_lists)
            break
    else:
        print("Invalid input, try again.")
        editing(data_lists)


def booking(data_lists):
    """
        Function used to show booking menu and waiting
        for user to input action he want to choose.
        After obtaining correct action it goes to choosen function.
    """
    print(get_booking_options())
    action = input()
    clear()
    for case in switch(action):
        if case("1"):
            create_booking(data_lists)
            break
        if case("2"):
            modify_booking(data_lists)
            break
        if case("3"):
            cancel_booking(data_lists)
            break
        if case("4"):
            main_menu(data_lists)
            break
    else:
        print("Invalid input, try again.")
        booking(data_lists)


def renting(data_lists):
    """
        Function used to show renting menu and waiting
        for user to input action he want to choose.
        After obtaining correct action it goes to choosen function.
    """
    print(get_rental_options())
    action = input()
    clear()
    for case in switch(action):
        if case("1"):
            pick_up_booking(data_lists)
            break
        if case("2"):
            create_rental(data_lists)
            break
        if case("3"):
            return_rented_car(data_lists)
            break
        if case("4"):
            exceeded_rentals(data_lists)
            break
        if case("5"):
            clear()
            main_menu(data_lists)
            break
    else:
        clear()
        print("Invalid input, try again.")
        renting(data_lists)


def open_database(data_lists):
    """
        Function used to show database menu and waiting
        for user to input action he want to choose.
        After obtaining correct action it prints choosen list
        or gets back to main menu.
    """
    print(get_open_database())
    action = input()
    clear()
    for case in switch(action):
        if case("1"):
            if len(data_lists[0]) == 0:
                print("\nCar list is empty!")
            else:
                print_car_list(data_lists[0])
            print("\nClick enter to back to database menu.")
            input()
            clear()
            open_database(data_lists)
            break
        if case("2"):
            if len(data_lists[2]) == 0:
                print("\nBooking list is empty!")
            else:
                print_booking_list(data_lists[2])
            print("\nClick enter to back to database menu.")
            input()
            clear()
            open_database(data_lists)
            break
        if case("3"):
            if len(data_lists[1]) == 0:
                print("\nRental list is empty!")
            else:
                print_rental_list(data_lists[1])
            print("\nClick enter to back to database menu.")
            input()
            clear()
            open_database(data_lists)
            break
        if case("4"):
            main_menu(data_lists)
            break
    else:
        print("Invalid input, try again.")
        open_database(data_lists)


def adding_new_car(data_lists):
    """
        Function used to get car data from user, create new Car object
        and add it to car list.
    """
    brand = get_brand("")
    model = get_model("")
    col = get_color("")
    pr_year = get_production_year("")
    typ = get_type("")
    eng = get_engine("")
    fuel_co = get_fuel_consumption("")
    seats = get_seats("")
    cost = get_cost("")
    biggest = 0
    for car in data_lists[0]:
        if car.id() > biggest:
            biggest = car.id()
    id = biggest + 1
    car = Car(brand, model, col, pr_year, typ, eng, fuel_co, seats, cost, id)
    data_lists[0].append(car)
    clear()
    editing(data_lists)


def editing_car(data_lists):
    """
        Function used to get car id from user
        to start edit one of its parametr.
    """
    while True:
        try:
            id = int(input("\nEnter id of the car you want to edit.\n"))
            break
        except ValueError:
            clear()
            print("Incorrect input type, try again.")
    car_to_edit = None
    for car in data_lists[0]:
        if car.id() == id:
            car_to_edit = car
            clear()
            print_car_list([car])
            edit_param_of_car(car, data_lists)
            editing(data_lists)
    if car_to_edit is None:
        clear()
        print(f'Car with {id} id doesn\'t exist in database.')
        editing(data_lists)


def edit_param_of_car(car, data_lists):
    """
        Function used to edit selected parametr of a car.
    """
    print(get_edit_param_of_car_options())
    action = input()
    clear()
    for case in switch(action):
        if case("1"):
            new_brand = get_brand(" new")
            car.new_brand(new_brand)
            clear()
            print("Car successfully edited.")
            break
        if case("2"):
            new_model = get_model(" new")
            car.new_model(new_model)
            clear()
            print("Car successfully edited.")
            break
        if case("3"):
            new_color = get_color(" new")
            car.new_color(new_color)
            clear()
            print("Car successfully edited.")
            break
        if case("4"):
            new_production_year = get_production_year(" new")
            car.new_production_year(new_production_year)
            clear()
            print("Car successfully edited.")
            break
        if case("5"):
            new_car_type = get_type(" new")
            car.new_car_type(new_car_type)
            clear()
            print("Car successfully edited.")
            break
        if case("6"):
            new_engine = get_engine(" new")
            car.new_engine(new_engine)
            clear()
            print("Car successfully edited.")
            break
        if case("7"):
            new_fuel_cons = get_fuel_consumption(" new")
            car.new_fuel_consumption(new_fuel_cons)
            clear()
            print("Car successfully edited.")
            break
        if case("8"):
            new_seats = get_seats(" new")
            car.new_seats(new_seats)
            clear()
            print("Car successfully edited.")
            break
        if case("9"):
            new_rent_cost = get_cost(" new")
            car.new_rent_cost(new_rent_cost)
            clear()
            print("Car successfully edited.")
            break
        if case("10"):
            clear()
            break
    else:
        print("Invalid input, try again.")
        edit_param_of_car(car, data_lists)


def delete_car(data_lists):
    """
        Function used to delete selected Car object
        from car_list. If car is currently rented it won't allow to
        delete that car.
    """
    if len(data_lists[0]) == 0:
        print("\nCar list is empty!")
        print("\nClick enter to back to editing menu.")
        input()
        clear()
        editing(data_lists)
    else:
        print_car_list(data_lists[0])
        while True:
            try:
                id = int(input("\nEnter id of the car you want to delete.\n"))
                break
            except ValueError:
                clear()
                print("Incorrect input type, try again.")
        clear()
        car_to_delete = None
        for car in data_lists[0]:
            if car.id() == id:
                car_to_delete = car
                if car.avability() == "avalible":
                    data_lists[0].remove(car_to_delete)
                    print("Car successfully deleted from database.")
                elif car.avability() == "rented":
                    print("Car is currently rented.")
                    print("Please cancel your rental first.")
                editing(data_lists)
        if car_to_delete is None:
            print(f'Car with {id} id doesn\'t exist in database.')
            editing(data_lists)


def get_brand(new):
    """
        Function used to obtain correct brand from user.
    """
    while True:
        brand = input(f"Enter{new} car's brand.\n")
        clear()
        if len(brand) > 16:
            print("Brand name too long. Please try again.\n")
        else:
            break
    return brand


def get_model(new):
    """
        Function used to obtain correct model from user.
    """
    while True:
        model = input(f"Enter{new} car's model.\n")
        clear()
        if len(model) > 14:
            print("Model name too long. Please try again.\n")
        else:
            break
    return model


def get_color(new):
    """
        Function used to obtain correct color from user.
    """
    while True:
        color = input(f"Enter{new} car's color.\n")
        clear()
        if len(color) > 12:
            print("Color name too long. Please try again.\n")
        else:
            break
    return color


def get_production_year(new):
    """
        Function used to obtain correct production year from user.
    """
    while True:
        try:
            production_year = int(input(f"Enter{new} production year.\n"))
            clear()
            if production_year < 1900:
                print("Incorrect year. Please try again.\n")
            elif production_year > today.year:
                print("Incorrect year. Please try again.\n")
            else:
                break
        except ValueError:
            clear()
            print("Incorrect input type. Please try again.\n")
    return production_year


def get_type(new):
    """
        Function used to obtain correct car type from user.
    """
    while True:
        typ = input(f"Enter{new} car type.\n")
        clear()
        if len(typ) > 16:
            print("Type name too long. Please try again.\n")
        else:
            break
    return typ


def get_engine(new):
    """
        Function used to obtain correct engine type from user.
    """
    while True:
        engine = input(f"Enter{new} car's engine type.\n")
        clear()
        if len(engine) > 12:
            print("Engine type too long. Please try again.\n")
        else:
            break
    return engine


def get_fuel_consumption(new):
    """
        Function used to obtain correct fuel consumption from user.
    """
    while True:
        try:
            fuel_co = float(input(f"Enter{new} car's fuel consumption.\n"))
            clear()
            if fuel_co < 0:
                print("Value too small. Please try again.\n")
            elif fuel_co > 100:
                print("Value too big. Please try again.\n")
            else:
                break
        except ValueError:
            clear()
            print("Incorrect input type. Please try again.\n")
    return fuel_co


def get_seats(new):
    """
        Function used to obtain correct number of seats from user.
    """
    while True:
        try:
            seats = int(input(f"Enter{new} number of seats.\n"))
            clear()
            if seats <= 0:
                print("Value too small. Please try again.\n")
            elif seats > 100:
                print("Value too big. Please try again.\n")
            else:
                break
        except ValueError:
            clear()
            print("Incorrect input type. Please try again.\n")
    return seats


def get_cost(new):
    """
        Function used to obtain correct rent cost from user.
    """
    while True:
        try:
            cost = int(input(f"Enter{new} cost of rent.\n"))
            clear()
            if cost <= 0:
                print("Value too small. Please try again.\n")
            elif cost > 10000:
                print("Value too big. Please try again.\n")
            else:
                break
        except ValueError:
            clear()
            print("Incorrect input type. Please try again.\n")
    return cost


def create_booking(data_lists):
    """
        Function used to get booking data from user,
        create Booking object and add it to booking list.
    """
    while True:
        try:
            car_id = int(input("Enter id of a car you want to book.\n"))
            break
        except ValueError:
            clear()
            print("Incorrect input type, try again.")
    clear()
    not_exist = True
    for car in data_lists[0]:
        if car.id() == car_id:
            not_exist = False
            car_inf = f'{car.brand()} {car.model()}'
            begin = get_begin()
            end = get_end()
            number_of_days = (end - begin).days
            if number_of_days > 180:
                print("You cannot book a car for more than 6 months.")
            if number_of_days == 0:
                print("You have to rent a car for more than one day.")
            elif number_of_days > 0:
                collides = False
                if avability_check(data_lists[2], begin, end, car_id):
                    collides = True
                if avability_check(data_lists[1], begin, end, car_id):
                    collides = True
                if not collides:
                    biggest = 0
                    for some_booking in data_lists[2]:
                        if some_booking.booking_id() > biggest:
                            biggest = some_booking.booking_id()
                    b_id = biggest + 1
                    cost = (number_of_days + 1) * car.rent_cost()
                    bookin = Booking(car.id(), car_inf, begin, end, b_id, cost)
                    data_lists[2].append(bookin)
                    print("Car successfully booked.")
                else:
                    print("The car is unavailable at the time you selected.")
            else:
                print("End date cannot be earlier than start date!")
    if not_exist:
        print(f'Car with {car_id} id doesn\'t exist in database.')
    booking(data_lists)


def get_begin():
    """
        Function used to obtain correct begin date from user.
    """
    while True:
        data = input("Enter start date in 'yyyy-mm-dd' format.\n")
        clear()
        try:
            begin = datetime.strptime(data, "%Y-%m-%d").date()
            number_of_days = (begin - today).days
            if today > begin:
                print("Date must be older than today. Please try again.")
            elif number_of_days > 365:
                print("You cannot book a car more than year in advance.")
            else:
                break
        except ValueError:
            print("Invalid date format. Please try again.")
    return begin


def get_end():
    """
        Function used to obtain correct end date from user.
    """
    while True:
        data = input("Enter end date in 'yyyy-mm-dd' format.\n")
        clear()
        try:
            datetime.strptime(data, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please try again.")
    end = datetime.strptime(data, "%Y-%m-%d").date()
    return end


def avability_check(booking_list, begin, end, car_id):
    """
        Function used to check whether car is avalible during
        obtained dates.
    """
    for bkn in booking_list:
        if car_id == bkn.car_id():
            if begin <= bkn.begin() and bkn.begin() <= end:
                return True
            elif begin <= bkn.end() and bkn.end() <= end:
                return True
            elif bkn.begin() <= begin and begin <= bkn.end():
                return True
            elif bkn.begin() <= end and end <= bkn.end():
                return True
    return False


def modify_booking(data_lists):
    """
        Function used to edit exisitng bookings.
    """
    while True:
        try:
            b_id = int(input("Enter id of a booking you want to modify.\n"))
            break
        except ValueError:
            clear()
            print("Incorrect input type, try again.")
    clear()
    not_exist = True
    for bookin in data_lists[2]:
        if b_id == bookin.booking_id():
            not_exist = False
            print_booking_list([bookin])
            new_booking_param(data_lists, bookin)
    if not_exist:
        print(f'Booking with {b_id} id doesn\'t exist in database.')
    booking(data_lists)


def new_booking_param(data_lists, booking):
    print(get_modify_booking_options())
    action = input()
    clear()
    bookings = []
    for bkn in data_lists[2]:
        if booking.booking_id() != bkn.booking_id():
            bookings.append(bkn)
    for case in switch(action):
        if case("1"):
            new_begin = get_begin()
            end = booking.end()
            c_id = booking.car_id()
            if new_begin > end:
                print("Start date cannot be older than end date.")
            else:
                collides = False
                if avability_check(bookings, new_begin, end, c_id):
                    collides = True
                if avability_check(data_lists[1], new_begin, end, c_id):
                    collides = True
                if not collides:
                    booking.new_begin(new_begin)
                    print("Start date successfully changed.")
                else:
                    print("The car is unavailable at the time you selected.")
            break
        if case("2"):
            new_end = get_end()
            begin = booking.begin()
            c_id = booking.car_id()
            number_of_days = (new_end - begin).days
            if new_end < begin:
                print("End date cannot be earlier than end date.")
            elif number_of_days > 180:
                print("You cannot book a car for more than 6 months.")
            else:
                collides = False
                if avability_check(bookings, begin, new_end, c_id):
                    collides = True
                if avability_check(data_lists[1], begin, new_end, c_id):
                    collides = True
                if not collides:
                    booking.new_end(new_end)
                    print("End date successfully changed.")
                else:
                    print("The car is unavailable at the time you selected.")
            break
        if case("3"):
            break
    else:
        clear()
        print("Invalid input, try again.")
        new_booking_param(data_lists, booking)


def cancel_booking(data_lists):
    """
        Function used to cancel existing booking.
        If entered booking id is correct it will remove
        it from booking list, otherwise, it get back to booking menu.
    """
    if len(data_lists[2]) == 0:
        print("\nBooking list is empty!")
        print("\nClick enter to back to booking menu.")
        input()
        clear()
        booking(data_lists)
    else:
        print_booking_list(data_lists[2])
        while True:
            try:
                id = int(input("\nEnter id of the booking to cancel it.\n"))
                break
            except ValueError:
                clear()
                print("Incorrect input type, try again.")
        booking_to_cancel = None
        for bookin in data_lists[2]:
            if bookin.booking_id() == id:
                booking_to_cancel = bookin
                data_lists[2].remove(booking_to_cancel)
                clear()
                print("Booking successfully canceled.")
                booking(data_lists)
        if booking_to_cancel is None:
            clear()
            print(f'Booking with {id} id doesn\'t exist in database.')
            booking(data_lists)


def pick_up_booking(data_lists):
    """
        Function used to create Rental object based on booking data.
        It will allows to do that if in booking list is
        booking that begin date is present day.
    """
    today_bookings = []
    for booking in data_lists[2]:
        if booking.begin() == today:
            today_bookings.append(booking)
    if len(today_bookings) == 0:
        print("There is no bookings in database to pick up today.")
    else:
        print_booking_list(today_bookings)
        while True:
            try:
                id = int(input("\nEnter id of the booking to pick it up.\n"))
                break
            except ValueError:
                clear()
                print("Incorrect input type, try again.")
        clear()
        match = False
        for booking in today_bookings:
            if id == booking.booking_id():
                match = True
                c_id = booking.car_id()
                info = booking.car_info()
                begin = booking.begin()
                end = booking.end()
                cost = booking.cost()
                biggest = 0
                for rental in data_lists[1]:
                    if rental.rent_id() > biggest:
                        biggest = rental.rent_id()
                rnt_id = biggest + 1
                ren = Rental(c_id, info, begin, end, cost, rnt_id)
                data_lists[1].append(ren)
                data_lists[2].remove(booking)
                for car in data_lists[0]:
                    if car.id() == c_id:
                        car.new_avability("rented")
                        break
                print("Booking picked up successfully.")
        if not match:
            print("Invalid booking id. Please try again.")
    renting(data_lists)


def create_rental(data_lists):
    """
        Function used to get rental data from user,
        create Rental object and add it to rental list.
    """
    while True:
        try:
            car_id = int(input("Enter id of a car you want to rent.\n"))
            break
        except ValueError:
            clear()
            print("Incorrect input type, try again.")
    clear()
    not_exist = True
    for car in data_lists[0]:
        if car.id() == car_id:
            not_exist = False
            car_inf = f'{car.brand()} {car.model()}'
            begin = today
            end = get_end()
            number_of_days = (end - begin).days
            if number_of_days > 180:
                print("You cannot rent a car for more than 6 months.")
            elif number_of_days > 0:
                collides = False
                if avability_check(data_lists[2], begin, end, car_id):
                    collides = True
                if avability_check(data_lists[1], begin, end, car_id):
                    collides = True
                if not collides:
                    biggest = 0
                    for some_rental in data_lists[1]:
                        if some_rental.rent_id() > biggest:
                            biggest = some_rental.rent_id()
                    r_id = biggest + 1
                    cost = (number_of_days + 1) * car.rent_cost()
                    rent = Rental(car.id(), car_inf, begin, end, cost, r_id)
                    data_lists[1].append(rent)
                    car.new_avability("rented")
                    print("Car successfully rented.")
                else:
                    print("The car is unavailable at the time you selected.")
            else:
                print("End date cannot be earlier than start date!")
    if not_exist:
        print(f'Car with {car_id} id doesn\'t exist in database.')
    renting(data_lists)


def return_rented_car(data_lists):
    """
        Function used to return rented car and delete Rental object
        from rental list. It will allows to do that if in rental list is
        rental that end date is on or before today.
    """
    cars_to_return = []
    for rent in data_lists[1]:
        if rent.end() <= today:
            cars_to_return.append(rent)
    if len(cars_to_return) == 0:
        print("There is no cars to return today.")
    else:
        print_rental_list(cars_to_return)
        while True:
            try:
                id = int(input("\nPlease enter rent id.\n"))
                break
            except ValueError:
                clear()
                print("Incorrect input type, try again.")
        clear()
        found = False
        for rent in cars_to_return:
            if rent.rent_id() == id:
                found = True
                total_cost = rent.cost()
                for car in data_lists[0]:
                    if car.id() == rent.car_id():
                        car.new_avability("avalible")
                        if rent.end() < today:
                            late_days = (today - rent.end()).days
                            total_cost += late_days * car.rent_cost()
                        break
                print("Car succesfuly returned.")
                print(f"Total cost of rental is {total_cost}")
                data_lists[1].remove(rent)
        if not found:
            print("Invalid rent id. Please try again.")
    renting(data_lists)


def exceeded_rentals(data_lists):
    """
        Function used to check if there are exceeded rentals in rental list.
        If so, it will show list of them.
    """
    exceeded = []
    for rental in data_lists[1]:
        if rental.exceeded() == "yes":
            exceeded.append(rental)
    if len(exceeded) == 0:
        print("There is no rentals that exceeded their rental time.")
    else:
        print_rental_list(exceeded)
        print("\nClick enter to back to database menu.")
        input()
        clear()
    renting(data_lists)
