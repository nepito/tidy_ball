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
    goals = [get_goals_on_season_for_player(player) for player in players]
    return pd.DataFrame(goals).rename(columns=NEW_NAMES["goals"])


def get_table_of_games_players(players):
    games = [get_appearences_on_season_for_player(player) for player in players]
    return pd.DataFrame(games)
