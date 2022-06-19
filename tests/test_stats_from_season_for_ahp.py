from tidyball import (
    read_json,
    get_appearences_on_season_for_player,
    get_dribbles_on_season_for_player,
    get_fouls_on_season_for_player,
    get_goals_on_season_for_player,
    get_passes_on_season_for_player,
    get_penalties_on_season_for_player,
    get_shots_on_season_for_player,
    get_tackles_on_season_for_player,
)

data_to_test = "tests/data/data_file_16482_2021.json"
aguirre = read_json(data_to_test)
data_to_test = "tests/data/data_file_6485_2021.json"
berterame = read_json(data_to_test)


def test_get_appearences_on_season_for_player():
    aguirre_appearences = {
        "appearences": 32,
        "lineups": 26,
        "minutes": 2257,
        "number": None,
        "position": "Attacker",
        "rating": "7.165625",
        "captain": False,
    }
    _assert_appearences_on_season_for(aguirre, aguirre_appearences)
    berterame_appearences = {
        "appearences": 37,
        "lineups": 37,
        "minutes": 3219,
        "number": None,
        "position": "Attacker",
        "rating": "7.029729",
        "captain": False,
    }
    _assert_appearences_on_season_for(berterame, berterame_appearences)


def _assert_appearences_on_season_for(player, expected_appearences):
    obtained_appearences = get_appearences_on_season_for_player(player)
    assert expected_appearences == obtained_appearences


def test_get_passes_on_season_for_player():
    berterame_passes = {"total": 722, "key": 41, "accuracy": 13}
    _assert_passes_on_season_for(berterame, berterame_passes)
    aguirre_passes = {"total": 446, "key": 25, "accuracy": 9}
    _assert_passes_on_season_for(aguirre, aguirre_passes)


def _assert_passes_on_season_for(player, expected_passes):
    aguirre_passes = get_passes_on_season_for_player(player)
    assert expected_passes == aguirre_passes


def test_get_goals_on_season_for_player():
    aguirre_goals = {"total": 12, "conceded": 0, "assists": 4, "saves": None}
    _assert_goals_on_season_for(aguirre, aguirre_goals)
    berterame_goals = {"total": 17, "conceded": 0, "assists": 5, "saves": None}
    _assert_goals_on_season_for(berterame, berterame_goals)


def _assert_goals_on_season_for(player, expected_goals):
    obtained_goals = get_goals_on_season_for_player(player)
    assert expected_goals == obtained_goals


def test_get_shots_on_season_for_player():
    aguirre_shots = {"total": 84, "on": 42}
    _assert_shots_on_season_for(aguirre, aguirre_shots)
    berterame_shots = {"total": 94, "on": 45}
    _assert_shots_on_season_for(berterame, berterame_shots)


def _assert_shots_on_season_for(player, expected_tackles):
    obtained_shots = get_shots_on_season_for_player(player)
    assert expected_tackles == obtained_shots


def test_get_tackles_on_season_for_player():
    berterame_tackles = {"total": 25, "blocks": 4, "interceptions": 18}
    _assert_tackles_on_season_for(berterame, berterame_tackles)
    aguirre_tackles = {"total": 20, "blocks": 1, "interceptions": 3}
    _assert_tackles_on_season_for(aguirre, aguirre_tackles)


def _assert_tackles_on_season_for(player, expected):
    obtained_tackles = get_tackles_on_season_for_player(player)
    assert expected == obtained_tackles


def test_get_dribbles_on_season_for_player():
    aguirre_dribbles = {"attempts": 54, "success": 23, "past": None}
    _assert_dribbles_on_season_for(aguirre, aguirre_dribbles)
    berterame_dribbles = {"attempts": 79, "success": 32, "past": None}
    _assert_dribbles_on_season_for(berterame, berterame_dribbles)


def _assert_dribbles_on_season_for(player, expected_dribbles):
    obtiained_dribles = get_dribbles_on_season_for_player(player)
    assert expected_dribbles == obtiained_dribles


def test_get_fouls_on_season_for_player():
    aguirre_fouls = {"drawn": 28, "committed": 67}
    _assert_fouls_on_season_for_player(aguirre, aguirre_fouls)
    berterame_fouls = {"drawn": 35, "committed": 45}
    _assert_fouls_on_season_for_player(berterame, berterame_fouls)


def _assert_fouls_on_season_for_player(player, expected_fouls):
    obtained_fouls = get_fouls_on_season_for_player(player)
    assert expected_fouls == obtained_fouls


def test_get_penalties_on_season_for_player():
    aguirre_penalties = {"won": None, "commited": None, "scored": 1, "missed": 0, "saved": None}
    expected_penalties = get_penalties_on_season_for_player()
    assert aguirre_penalties == expected_penalties
    berterame_penalties = {"won": None, "commited": None, "scored": 5, "missed": 2, "saved": None}
    expected_penalties = get_penalties_on_season_for_player()
    assert berterame_penalties == expected_penalties
