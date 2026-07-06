class FootballTeam:
    def __init__(self, team_name, coach):
        self.team_name = team_name
        self.coach = coach
        self.players = []  # ცარიელი სია შექმნისას

    # 1. მოთამაშის დამატება
    def add_player(self, name, position, number, age, nationality):
        player = {
            "name": name,
            "position": position,
            "number": number,
            "age": age,
            "nationality": nationality
        }
        self.players.append(player)
        print(f"player {name} added to team {self.team_name}.")

    # 2. მოთამაშის წაშლა ნომრის მიხედვით
    def remove_player(self, number):
        for player in self.players:
            if player["number"] == number:
                self.players.remove(player)
                print(f"player #{number} removed from team {self.team_name}.")
                return
        print(f"player with number {number} not found in team {self.team_name}.")

    # 3. მოთამაშის ინფორმაციის განახლება
    def update_player(self, number, key, value):
        for player in self.players:
            if player["number"] == number:
                player[key] = value
                print(f"player (#{number}) {key} updated: {value}")
                return
        print(f"player with number {number} not found in team {self.team_name}.")

    # 4. კლუბის ინფორმაციის ჩვენება
    def display_team_info(self):
        print(f"team: {self.team_name}")
        print(f"coach: {self.coach}")
        print("players:")
        if not self.players:
            print("  no players added.")
        for player in self.players:
            print(f"  {player}")

    # 5. მოთამაშის ინფორმაციის ჩვენება ნომრის მიხედვით
    def display_player_info(self, number):
        for player in self.players:
            if player["number"] == number:
                print(f"player information (#{number}):")
                for key, value in player.items():
                    print(f"  {key}: {value}")
                return
        print(f"player with number {number} not found in team {self.team_name}.")


# --- გამოყენების მაგალითი ---
if __name__ == "__main__":
    team = FootballTeam("Dinamo Tbilisi", "Levan Khomeriki")

    team.add_player("Giorgi Chakvetadze", "Midfielder", 10, 21, "Georgia")
    team.add_player("Guram Kashia", "Defender", 4, 34, "Georgia")

    team.display_team_info()

    team.update_player(10, "goal", 1)
    team.display_player_info(10)

    team.remove_player(4)
    team.display_team_info()