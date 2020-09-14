class NBAPlayer():
    def __init__(self, name, position, team):
        self.name = name
        self.position = position
        self.team = team
        self.salary = 0

    def add_salary(self, salary_amount):
        self.salary += salary_amount

    def fine(self, fine_amount):
        self.salary -= fine_amount
    
    def trade_player(self, new_team):
        self.team = new_team

lebron_james = NBAPlayer("Lebron James", "Point Guard", "Lakers")
lebron_james.add_salary(3000000)
print("{} salary is {} ".format(lebron_james.name, lebron_james.salary))


carmelo_anothny = NBAPlayer("Carmelo Anthony", "SF", "Rockets")
carmelo_anothny.add_salary(500000)
print("{} salary is {} ".format(carmelo_anothny.name, carmelo_anothny.salary))

carmelo_anothny.fine(20000)
print(f"{carmelo_anothny.name} is fine 20000")

carmelo_anothny.trade_player("Blazers")
print(f"{carmelo_anothny.name} is currently a member the {carmelo_anothny.team}")