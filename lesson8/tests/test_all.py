import pytest
from playwright.sync_api import expect, sync_playwright

games = [ "gta", "fifa", "call_of_duty", "minecraft", "fortnite"]
consoles = ["xbox", "playstation", "nintendo", "pc"]

print(input("Enter your favorite game: "))
print(input("Enter your favorite console: "))
if input("Enter your favorite game: ") in games and input("Enter your favorite console: ") in consoles:
    print("You have good taste in games and consoles!")

    
    
