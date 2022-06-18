from tidyball import read_json, get_appearences_on_season_for_player

data_to_test = "tests/data/data_file_16482_2021.json"
jenssen = read_json(data_to_test)


def test_get_appearences_on_season_for_player():
    expected_appearences = {
        "appearences": 32,
        "lineups": 26,
        "minutes": 2257,
        "number": None,
        "position": "Attacker",
        "rating": "7.165625",
        "captain": False,
    }
    obtained_appearences = get_appearences_on_season_for_player()
    assert expected_appearences == obtained_appearences
