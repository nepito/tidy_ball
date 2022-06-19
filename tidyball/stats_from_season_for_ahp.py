def get_appearences_on_season_for_player(player):
    return player["response"][0]["statistics"][0]["games"]


def get_passes_on_season_for_player(player):
    expected_passes = player["response"][0]["statistics"][0]["passes"]
    return expected_passes
