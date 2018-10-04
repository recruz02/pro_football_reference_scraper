
def xstr(s):
    return '' if s is None else str(s)

# CREATE CLASS OBJECT
class nflplayer():

	def __init__(self):
		self.nflplayerid = None
		self.url = None
		self.first_name = None
		self.last_name = None
		self.player_position = None
		self.player_height = None
		self.player_weight = None
		self.birthdate = None
		self.birthplace = None
		self.college = None
