# Data, an encoding system by Jessica Emberly.
# Message: abc
# Rule: {"a", "b", "c"}
# Seed adds 1 to the alphabet letter position.
# Generates a random number in range for LID.
# Letter Identifier | Position
# Seed: -159c098b1509a2
# The seed is used to map the letter positions which is used in order to decode the Message.
import os
import time
import random

os.system("clear")
message = input("What do I encode?: ")
rule = {"a", "b", "c"}
nr = str(rule).split()
letter_a = ""
letter_b = ""
letter_c = ""
a = str(random.randint(-501, -1)) + str(nr[0]).replace(",", " ").replace("{", " ").replace("}", " ").replace("'", " ").replace(" ", "") + str(message.index("a"))
letter_a = a
b = str(random.randint(0, 500)) + str(nr[1]).replace(",", " ").replace("{", " ").replace("}", " ").replace("'", " ").replace(" ", "") + str(message.index("b"))
letter_b = b
c = str(random.randint(501, 1001)) + str(nr[2]).replace(",", " ").replace("{", " ").replace("}", " ").replace("'", " ").replace(" ", "") + str(message.index("c"))
letter_c = c
list = []
la = message.find("a")
lb = message.find("b")
lc = message.find("c")
if la == 0:
  list.append(letter_a)
if lb == 0:
  list.append(letter_b)
if lc == 0:
  list.append(letter_c)
if la == 1:
  list.append(letter_a)
if lb == 1:
  list.append(letter_b)
if lc == 1:
  list.append(letter_c)
if la == 2:
  list.append(letter_a)
if lb == 2:
  list.append(letter_b)
if lc == 2:
  list.append(letter_c)
os.system("clear")
print("Encoded String: " + str(list).replace(",", " ").replace("[", " ").replace("]", " ").replace("'", " ").replace(" ", ""))
