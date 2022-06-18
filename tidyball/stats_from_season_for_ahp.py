from tidyball import read_json, get_appearences_on_season_for_player

data_to_test = "tests/data/data_file_16482_2021.json"
jenssen = read_json(data_to_test)

def test_get_appearences_on_season_for_player():
    get_appearences_on_season_for_player()