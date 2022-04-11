from pydantic import BaseModel
import pandas as pd
from typing import Optional, List


class Penalty(BaseModel):
    won: Optional[int]
    commited: Optional[int]
    scored: Optional[int]
    missed: Optional[int]
    saved: Optional[int]


class Penalties_Team:
    def __init__(self, players: List[dict]) -> None:
        self.penalties: List[Penalty] = [
            Penalty(**local_player["statistics"][0]["penalty"]) for local_player in players
        ]

    def missed(self) -> int:
        missed: int = sum(penalty.missed for penalty in self.penalties)
        return missed

    def scored(self) -> int:
        scored: int = sum(penalty.scored for penalty in self.penalties)
        return scored


class Penalty_Match(BaseModel):
    away_scored: Optional[int]
    away_missed: Optional[int]
    home_scored: Optional[int]
    home_missed: Optional[int]
    id_match: Optional[int]
    home_total: Optional[int]
    away_total: Optional[int]

    def __init__(self, **data) -> None:
        super().__init__(**data)
        self.away_total = self.away_scored + self.away_missed
        self.home_total = self.home_scored + self.home_missed


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
