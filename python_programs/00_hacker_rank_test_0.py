from abc import ABC, abstractmethod

class Quacker(ABC):
	@abstractmethod
	def quack(self):
		pass

class Duck(Quacker):
	def quack(self):
		return 'Quack!'

class Cat:
	def quack(self):
		return 'Meow!'

def is_quacker(obj):
	if isinstance(obj, Quacker):
		return True
	return False

duck = Duck()
cat = Cat()

print(is_quacker(duck))
print(is_quacker(cat))
print(issubclass(Duck, Quacker))
print(issubclass(Cat, Quacker))
