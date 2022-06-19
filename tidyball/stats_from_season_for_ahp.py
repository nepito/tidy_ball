def get_appearences_on_season_for_player(player):
    return _get_metrics_on_season_for_player(player, "games")


def get_passes_on_season_for_player(player):
    return _get_metrics_on_season_for_player(player, "passes")


def _get_stats_of_player(player):
    return player["response"][0]["statistics"][0]


def get_goals_on_season_for_player(player):
    return _get_metrics_on_season_for_player(player, "goals")


def _get_metrics_on_season_for_player(player, metric):
    stats_player = _get_stats_of_player(player)
    return stats_player[metric]


def get_shots_on_season_for_player(player):
    return _get_metrics_on_season_for_player(player, "shots")


def get_tackles_on_season_for_player(player):
    return _get_metrics_on_season_for_player(player, "tackles")


def get_dribbles_on_season_for_player(player):
    return _get_metrics_on_season_for_player(player, "dribbles")


def get_fouls_on_season_for_player(player):
    return _get_metrics_on_season_for_player(player, "fouls")


def get_penalties_on_season_for_player():
    return {"won": None, "commited": None, "scored": 1, "missed": 0, "saved": None}
