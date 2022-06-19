def get_appearences_on_season_for_player(player):
    stats_player = _get_stats_of_player(player)
    return stats_player["games"]


def get_passes_on_season_for_player(player):
    stats_player = _get_stats_of_player(player)
    passes = stats_player["passes"]
    return passes


def _get_stats_of_player(player):
    return player["response"][0]["statistics"][0]


def get_goals_on_season_for_player():
    pass
