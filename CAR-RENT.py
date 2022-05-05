import operations as op


def start():
    """
    Loads data from files and creates database object.
    After exiting from programm saves data to files.
    """
    op.clear()
    database = op.Database()
    op.load_data(database, op.file_paths)
    print("\n***   Welcome to Car-Rent!   ***")
    data_lists = [database.cars, database.rentals, database.bookings]
    op.main_menu(data_lists)
    op.save_data(database, op.file_paths)


if __name__ == "__main__":
    start()
