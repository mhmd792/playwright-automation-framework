def test_favorite_choices_are_supported():
    games = ["gta", "fifa", "call_of_duty", "minecraft", "fortnite"]
    consoles = ["xbox", "playstation", "nintendo", "pc"]

    favorite_game = "fifa"
    favorite_console = "xbox"

    assert favorite_game in games
    assert favorite_console in consoles
