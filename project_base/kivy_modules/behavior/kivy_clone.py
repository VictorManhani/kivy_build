# kivy_clone.py
# created by Victor G. Manhani

class CloneWidget:
	def __init__(self, **kwargs):
		self.kwargs = kwargs
		self.__dict__.update(kwargs)
		super().__init__(**kwargs)

	def copy(self):
		return self.__class__(**self.kwargs)

# inheriting this class, allows the class that inherited it to be cloned.
