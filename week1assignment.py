class RestaurantTable:
    restaurant_name = "Taste of Tashkent"
    max_seats = 4
    total_tables = 0
    def init(self, table_number, section):
        self.table_number = table_number
        self.section = section
        self.diners = []
        RestaurantTable.total_tables += 1
    def seat_diner(self, name):
        if len(self.diners) < RestaurantTable.max_seats:
            self.diners.append(name)
            print(f"Seated {name} at Table {self.table_number}")
        else:
            print("Table is full")  
    def unseat_diner(self, name):
        if name in self.diners:
            self.diners.remove(name)
            print(f"Removed {name} from Table {self.table_number}")  
        else:
            print("Diner not found")  
    def display_table(self):
        print(f"Table {self.table_number} in {self.section} at {self.restaurant_name}")
    
table = RestaurantTable(5, "Patio")

table.display_table()
table.seat_diner("Nodira")
table.seat_diner("Kamola")
table.seat_diner("Farhod")
table.seat_diner("Shavkat")
table.seat_diner("Dilshod")   
table.unseat_diner("Kamola")
table.unseat_diner("Zafar") 

print(f"Total tables: {RestaurantTable.total_tables}")
