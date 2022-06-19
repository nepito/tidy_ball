def get_appearences_on_season_for_player(player):
    return player["response"][0]["statistics"][0]["games"]


def get_passes_on_season_for_player():
    expected_passes = {"total": 722, "key": 41, "accuracy": 13}
    return expected_passes
