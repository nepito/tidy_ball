import pandas as pd
from pydantic import BaseModel
from typing import Optional


class Penalty(BaseModel):
    won: Optional[int]
    commited: Optional[int]
    scored: Optional[int]
    missed: Optional[int]
    saved: Optional[int]


class Goal(BaseModel):
    total: Optional[int]
    conceded: Optional[int]
    assists: Optional[int]
    saves: Optional[int]


class Passes(BaseModel):
    total: Optional[int]
    key: Optional[int]
    accuracy: Optional[int]


class Games(BaseModel):
    minutes: Optional[int]
    position: str
    number: Optional[int]


class Tackles(BaseModel):
    total: Optional[int]
    blocks: Optional[int]
    interceptions: Optional[int]


class Dribbles(BaseModel):
    attempts: Optional[int]
    success: Optional[int]
    past: Optional[int]


class MatchTeam(BaseModel):
    match: str
    team: str


def get_players_statistic_from_match(league_file: dict):
    column_names = ["goals", "passes"]
    return _get_statistic_players_from_match(league_file, column_names)


_AXIS = 1


def _get_statistic_players_from_match(league_file, column_names):
    output = _get_match_team_player_from_dictionary_league(league_file)
    players = get_info_game_by_player_from_data(league_file)
    values_columns = [
        output,
        players,
        *[_get_info_by_player_from_data(league_file, column_name) for column_name in column_names],
    ]
    return pd.concat(values_columns, axis=_AXIS)


def _get_match_team_player_from_dictionary_league(league_file: dict):
    match = league_file["parameters"]["fixture"]
    teams = get_teams_from_data(league_file)
    match_team = [match for team in teams]
    id_players = get_id_players_from_data(league_file)
    for_dataframe = {"match": match_team, "team": teams, "player": id_players}
    return pd.DataFrame(for_dataframe)


def get_teams_from_data(league_file: dict) -> list:
    home = get_id_team_from_response(league_file["response"][0])
    away = get_id_team_from_response(league_file["response"][1])
    return home + away


def get_id_team_from_response(response: dict) -> list:
    team = response["team"]["id"]
    return [team for player in response["players"]]


def get_id_players_from_data(data: dict) -> list:
    home_players = data["response"][0]["players"]
    away_players = data["response"][1]["players"]
    id_players = [player["player"]["id"] for player in home_players + away_players]
    return id_players


def get_info_game_by_player_from_data(data: dict) -> pd.DataFrame:
    players = get_players(data)
    for_dataframe = [Games(**player["statistics"][0]["games"]).dict() for player in players]
    info_game_of_players = pd.DataFrame(for_dataframe)
    return info_game_of_players


def get_players(data: dict) -> list:
    home_players = data["response"][0]["players"]
    away_players = data["response"][1]["players"]
    players = home_players + away_players
    return players


def get_info_goal_by_player_from_data(data: dict) -> pd.DataFrame:
    set_of_info = "goals"
    return _get_info_by_player_from_data(data, set_of_info)


def get_info_passes_by_player_from_data(data: dict) -> pd.DataFrame:
    set_of_info = "passes"
    return _get_info_by_player_from_data(data, set_of_info)


def get_info_tackles_by_player_from_data(data: dict) -> pd.DataFrame:
    set_of_info = "tackles"
    return _get_info_by_player_from_data(data, set_of_info)


def get_info_dribbles_by_player_from_data(data: dict):
    set_of_info = "dribbles"
    return _get_info_by_player_from_data(data, set_of_info)


def _get_info_by_player_from_data(data: dict, set_of_info: str) -> pd.DataFrame:
    players = get_players(data)
    info_tackles_of_players = _info_players_to_dataframe(players, set_of_info)
    return info_tackles_of_players.rename(columns=NEW_NAMES[set_of_info])


def _info_players_to_dataframe(players, set_of_info):
    info = SET_OF_INFO[set_of_info]
    for_dataframe = [info(**player["statistics"][0][set_of_info]).dict() for player in players]
    return pd.DataFrame(for_dataframe)


SET_OF_INFO = {"tackles": Tackles, "passes": Passes, "goals": Goal, "dribbles": Dribbles}

PASSES_NEW_NAMES = {
    "total": "passes_total",
    "key": "passes_key",
    "accuracy": "passes_accuracy",
}
GOALS_NEW_NAMES = {
    "total": "goal_total",
    "conceded": "goal_conceded",
    "assists": "goal_assists",
    "saves": "goal_saves",
}
TACKLES_NEW_NAMES = {
    "total": "tackles_total",
    "blocks": "tackles_blocks",
    "interceptions": "tackles_interceptions",
}
DRIBBLES_NEW_NAMES = {
    "attempts": "dribbles_attempts",
    "success": "dribbles_success",
    "past": "dribbles_past",
}
GAMES_NEW_NAMES = {
    "appearences": "player_appearences",
    "lineups": "player_lineups",
    "minutes": "player_minutes",
    "number": "player_number",
    "position": "player_position",
    "rating": "player_rating",
    "captain": "is_captain",
}
SHOTS_NEW_NAMES = {"total": "shots_total", "on": "shots_on"}
NEW_NAMES = {
    "dribbles": DRIBBLES_NEW_NAMES,
    "tackles": TACKLES_NEW_NAMES,
    "passes": PASSES_NEW_NAMES,
    "goals": GOALS_NEW_NAMES,
    "games": GAMES_NEW_NAMES,
    "shots": SHOTS_NEW_NAMES,
}


def get_goals_passes_tackles_and_dribbles_statistic_from_match(league_file):
    column_names = ["goals", "passes", "tackles", "dribbles"]
    return _get_statistic_players_from_match(league_file, column_names)
