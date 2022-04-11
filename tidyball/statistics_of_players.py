import numpy as np
import pandas as pd
from pydantic import BaseModel
from typing import Optional, List


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
    number: int


class Tackles(BaseModel):
    total: Optional[int]
    blocks: Optional[int]
    interceptions: Optional[int]


class MatchTeam(BaseModel):
    match: str
    team: str


def get_players_statistic_from_match(league_file: dict):
    match = league_file["parameters"]["fixture"]
    teams = get_teams_from_data(league_file)
    match_team = [match for team in teams]
    id_players = get_id_players_from_data(league_file)
    for_dataframe = {"match": match_team, "team": teams, "player": id_players}
    output = pd.DataFrame(for_dataframe)
    players = get_info_game_by_player_from_data(league_file)
    goals = get_info_goal_by_player_from_data(league_file)
    passes = get_info_passes_by_player_from_data(league_file)
    return pd.concat([output, players, goals, passes], axis=1)


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


def get_info_goal_by_player_from_data(data: dict) -> pd.DataFrame:
    players = get_players(data)
    for_dataframe = [Goal(**player["statistics"][0]["goals"]).dict() for player in players]
    info_goal_of_players = pd.DataFrame(for_dataframe)
    new_names = {
        "total": "goal_total",
        "conceded": "goal_conceded",
        "assists": "goal_assists",
        "saves": "goal_saves",
    }
    return info_goal_of_players.rename(columns=new_names)


def get_info_passes_by_player_from_data(data: dict) -> pd.DataFrame:
    players = get_players(data)
    for_dataframe = [Passes(**player["statistics"][0]["passes"]).dict() for player in players]
    info_goal_of_players = pd.DataFrame(for_dataframe)
    new_names = {
        "total": "passes_total",
        "key": "passes_key",
        "accuracy": "passes_accuracy",
    }
    return info_goal_of_players.rename(columns=new_names)


def get_players(data: dict) -> list:
    home_players = data["response"][0]["players"]
    away_players = data["response"][1]["players"]
    players = home_players + away_players
    return players


def get_info_tackles_by_player_from_data(data: dict) -> pd.DataFrame:
    new_names = {
        "total": "tackles_total",
        "blocks": "tackles_blocks",
        "interceptions": "tackles_interceptions",
    }
    return get_info_by_player_from_data(data, "tackles", new_names)


def get_info_by_player_from_data(data: dict, set_of_info: str, new_names: dict) -> pd.DataFrame:
    players = get_players(data)
    info = SET_OF_INFO["tackles"]
    for_dataframe = [info(**player["statistics"][0][set_of_info]).dict() for player in players]
    info_tackles_of_players = pd.DataFrame(for_dataframe)
    return info_tackles_of_players.rename(columns=new_names)

SET_OF_INFO = {"tackles": Tackles}