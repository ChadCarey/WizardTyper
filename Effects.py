import Entities

# effect is a base class for all effects
class Effect(object):
	def __init__(self):
		self.timer = 1
		self.power = 1
		self.active = True

	def updateSpellProgress(self):
		if(self.timer > 0):
			self.timer = self.timer - 1
		else:
			self.active = False

# burn is a damage effect
class Burn(Effect):
	def __init__(self, duration, power):
		# call super constuctor
		super(Burn, self).__init__()
		self.timer = duration
		self.power = power

	def applyEffect(self, entity):
		self.updateSpellProgress()
		if self.active:
			entity.damage(self.power)
			