import json

class TinyTourney:

    standings = {
        'alpha': {
            'wins': 0,
            'ties': 0,
            'losses': 0
        },
        'beta': {
            'wins': 5,
            'ties': 0,
            'losses': 0
        },
        'charlie': {
            'wins': 1,
            'ties': 0,
            'losses': 0
        }
    }

    def start(self):
        self.pull("standings.txt")
        while(1):
            cmd = input("> ")
            tokens = cmd.split()
            if tokens[0] == "team":
                if tokens[1] == "add":
                    team = tokens[2]
                    self.add_team(team)
                    print("added team " + team + "\n")
                    self.push("standings.txt")

            if tokens[0] == "display":
                if len(tokens) == 1:
                    self.display_standings()
                elif tokens[1] == "all":
                    self.display_all()
                
            if tokens[0] == "exit":
                break

            if tokens[0] == "add":
                team1 = tokens[1]
                team2 = tokens[2]
                score1 = tokens[3]
                score2 = tokens[4]
                self.add_result(team1, team2, score1, score2)
                self.push("standings.txt")
            

    def add_result(self, team1, team2, score1, score2):
        if score1 > score2:
            self.increment_wins(team1)
            self.increment_losses(team2)
            print("team1 beat team2")
        elif score2 > score1:
            self.increment_wins(team2)
            self.increment_losses(team1)
        else:
            self.increment_ties(team1)
            self.increment_ties(team2)

    def order_teams(self):
        return sorted(self.standings, key=lambda x: (
            self.standings[x]['wins'], self.standings[x]['ties']), reverse=True)

    def display_standings(self):
        ordered_teams = self.order_teams()
        print("TEAM\t\tW  T  L")
        for team in ordered_teams:
            print("%s\t\t%d  %d  %d" % (
                team, self.standings[team]["wins"], self.standings[team]["ties"], self.standings[team]["losses"]))

    def display_all(self):
        print(self.standings)

    def push(self, filename):
        with open(filename, 'w') as json_file:
            json.dump(self.standings, json_file, sort_keys=True, indent=4, separators=(',', ': '))
    
    def pull(self, filename):
        with open(filename) as json_file:
            self.standings = json.load(json_file)

    def increment_wins(self, team):
        self.increment_stat(team, "wins")
    
    def increment_ties(self, team):
        self.increment_stat(team, "ties")

    def increment_losses(self, team):
        self.increment_stat(team, "losses")

    def get_wins(self, team):
        self.get_stat(team, "wins")

    def get_ties(self, team):
        self.get_stat(team, "ties")

    def get_losses(self, team):
        self.get_stat(team, "losses")

    def update_wins(self, team, val):
        self.update_stat(team, "wins", val)

    def update_losses(self, team, val):
        self.update_stat(team, "losses", val)

    def update_ties(self, team, val):
        self.update_stat(team, "losses", val)

    def update_stat(self, team, key, val):
        if team in self.standings:
            if key in self.standings[team]:
                self.standings[team][key] = val
            else:
                print("ERROR: key does not exist")
        else:
            print("ERROR: team does not exist")

    def get_stat(self, team, key):
        if team in self.standings:
            if key in self.standings[team]:
                return self.standings[team][key]
            else:
                print("ERROR: key does not exist")
        else:
            print("ERROR: team does not exist")

    def increment_stat(self, team, key):
        val = self.get_stat(team, key)
        self.update_stat(team, key, val + 1)

    def add_team(self, team):
        self.standings[team] = {
            'wins': 0,
            'ties': 0,
            'losses': 0
        }


if __name__ == '__main__':
    a = TinyTourney()
    a.start()
