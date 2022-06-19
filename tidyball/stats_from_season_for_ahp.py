import pandas as pd
from tidyball import NEW_NAMES


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


def get_penalties_on_season_for_player(player):
    return _get_metrics_on_season_for_player(player, "penalty")


def get_table_of_goals_players(players):
    return _get_table_for_metric_of_players(players, "goals")


def get_table_of_games_players(players):
    return _get_table_for_metric_of_players(players, "games")


def get_table_of_passes_players(players):
    return _get_table_for_metric_of_players(players, "passes")


def _get_table_for_metric_of_players(players, metric):
    player_metrics = [_get_metrics_on_season_for_player(player, metric) for player in players]
    table = pd.DataFrame(player_metrics).rename(columns=NEW_NAMES[metric])
    return table
