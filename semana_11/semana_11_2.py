#Cree una clase de `Bus` con:
#Un atributo de `max_passengers`.
# Un método para agregar pasajeros uno por uno (que acepte como parámetro una instancia de la clase `Person` vista en la lección). **Este solo debe agregar pasajeros si lleva menos de su máximo.** Sino, debe mostrar un mensaje de que el bus está lleno.
# Un método para bajar pasajeros uno por uno (en cualquier orden).

class Bus:
    def __init__(self, max_passengers = 120):
        self.max_passengers = max_passengers
        self.current_passengers = 0
        self.available_space = 0
        

    def add_passenger(self):
        while self.current_passengers < self.max_passengers:
            self.available_space = self.max_passengers - self.current_passengers
            try:
                people_on = int(input("How many people are getting on the bus? "))
                if people_on == 0:
                    print("No one got on the bus. Bus is empty!")
                elif  people_on <= self.available_space:
                    self.current_passengers += people_on
                    print(f'The bus received {people_on} passenger. Now, there are {self.current_passengers} people on the bus. On to the next stop...')
                else:
                    board_now = self.available_space
                    left_behind = people_on - self.available_space
                    self.current_passengers += self.available_space
                    print(f'Only {board_now} passengers were able to board. {left_behind} must wait for the next bus.')
                    print(f'The bus received {board_now}. Now, there are {self.current_passengers} people on the bus. On to final destination.')
            except ValueError:
                print("Oops! that was not a valid number. Try again")
        print("The bus is now full! No more passengers can board.")
        return self.current_passengers
    
    def remove_passenger(self):
        while self.current_passengers > 0:
            try:
                people_off = int(input("How many people are getting off the bus? "))
                if people_off <= self.current_passengers:
                    self.current_passengers -= people_off
                    print(f'The bus dropped off {people_off}. Now, there are {self.current_passengers} people on the bus. On to the next stop...')
                else:
                    print(f"There are only {self.current_passengers} passengers left. {people_off} passengers can't get off the bus.")
            except ValueError:
                print("Oops! that was not a valid number. Try again")
        print(f'The bus dropped off all passengers. Now, the bus is empty. Off to the parking lot.')
        print("The bus is now empty! Route finished.")
        return self.current_passengers


my_first_bus = Bus(200)
my_first_bus.add_passenger()
my_first_bus.remove_passenger()
