import random

zahlen = random.sample(range(1, 43), 6)
glückszahl = random.randint(1, 6)

print("Ihre Lottozahlen sind:", sorted(zahlen))
print("Ihre Glückszahl ist:", glückszahl)