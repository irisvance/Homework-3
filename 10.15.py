#Iris Vance
#1270481

class Team:
  def __init__(self, team_name = 0, team_wins = 0, team_losses = 0):
    self.team_name = "None"
    self.team_wins = team_wins
    self.team_losses = team_losses

  def get_win_percentage(self):
    win_rate = (self.team_wins) / (self.team_wins + self.team_losses)
    return win_rate

if __name__ == "__main__":
  team = Team()
  team_name = input()
  team_wins = float(input())
  team_losses = float(input())

  team.team_name = team_name
  team.team_wins = team_wins
  team.team_losses = team_losses

  if team.get_win_percentage() >= 0.5:
    print('Congratulations, Team',team.team_name, 'has a winning average!')

  else:
    print('Team', team.team_name, 'has a losing average.')


