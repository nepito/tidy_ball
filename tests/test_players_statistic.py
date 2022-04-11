import pandas as pd
import numpy as np
import json
from pandas._testing import assert_frame_equal
import pytest

from tidyball import (
    read_json,
    get_players_statistic_from_match,
    Goal,
    Passes,
    Games,
    MatchTeam,
    Tackles,
    get_id_team_from_response,
    get_id_players_from_data,
    get_info_game_by_player_from_data,
    get_info_goal_by_player_from_data,
    get_info_passes_by_player_from_data,
    get_info_tackles_by_player_from_data,
)

league_path = "tests/data/data_statisitcs_players_718522.json"
data = read_json(league_path)

pre_expected = {
    "match": [
        "718522",
        "718522",
        "718522",
        "718522",
        "718522",
        "718522",
        "718522",
        "718522",
        "718522",
    ],
    "team": [106, 106, 106, 82, 82, 82, 82, 82, 82],
    "player": [36878, 99, 22164, 2801, 8478, 21585, 21443, 879, 1918],
    "minutes": [90, 90, 90, 90, 77, 90, 90, 89, 45],
    "position": ["G", "D", "D", "G", "D", "M", "M", "M", "F"],
    "number": [40, 18, 23, 1, 2, 6, 11, 10, 9],
    "goal_total": [np.nan, np.nan, np.nan, np.nan, np.nan, 1, np.nan, 1, 1],
    "goal_conceded": [4, 0, 0, 0, 0, 0, 0, 0, 0],
    "goal_assists": [np.nan, np.nan, np.nan, np.nan, 1, np.nan, 1, np.nan, 1],
    "goal_saves": [np.nan, np.nan, np.nan, 6, np.nan, np.nan, np.nan, np.nan, np.nan],
    "passes_total": [20, 39, 40, 34, 29, 32, 63, 24, 13],
    "passes_key": [1, np.nan, np.nan, np.nan, 1, np.nan, 2, 1, 2],
    "passes_accuracy": [16, 32, 37, 29, 21, 24, 45, 21, 13],
}


def test_get_players_statistic_from_match():
    obtained = get_players_statistic_from_match(data)
    expected = pd.DataFrame(pre_expected)
    assert_frame_equal(expected, obtained)


def test_Goal():
    typical_goal = {
        "goals_total": None,
        "goals_conceded": 2,
        "goal_assists": 3,
        "goal_saves": 4,
    }
    obtained_goal = Goal(**typical_goal)


def test_passes():
    typical_passes = {"total": None, "key": None, "accuaracy": 2}
    obtained = Passes(**typical_passes)


def test_Games():
    typical_games = {"player": "23", "minutes": 4, "position": "G", "number": 45}
    obtained_games = Games(**typical_games)


def test_Match():
    typical_match = {"match": "23", "team": "34"}
    obtained_match = MatchTeam(**typical_match)


def test_Tackles():
    typical_tackles = {"total": "5", "blocks": None, "interceptions": "1"}
    obtained_tackles = Tackles(**typical_tackles)


def test_get_id_team_from_response():
    expected_id_team = [106, 106, 106]
    obtained_id_team = get_id_team_from_response(data["response"][0])
    assert expected_id_team == obtained_id_team
    expected_id_team = [82, 82, 82, 82, 82, 82]
    obtained_id_team = get_id_team_from_response(data["response"][1])
    assert expected_id_team == obtained_id_team


def test_get_id_players_from_data():
    expected = [36878, 99, 22164, 2801, 8478, 21585, 21443, 879, 1918]
    obtained = get_id_players_from_data(data)
    assert expected == obtained


def test_get_info_game_by_player_from_data():
    for_dataframe = {
        "minutes": [90, 90, 90, 90, 77, 90, 90, 89, 45],
        "position": ["G", "D", "D", "G", "D", "M", "M", "M", "F"],
        "number": [40, 18, 23, 1, 2, 6, 11, 10, 9],
    }
    expected = pd.DataFrame(for_dataframe)
    obtained = get_info_game_by_player_from_data(data)
    assert_frame_equal(expected, obtained)


def test_get_info_goal_by_player_from_data():
    for_dataframe = {
        "goal_total": [np.nan, np.nan, np.nan, np.nan, np.nan, 1, np.nan, 1, 1],
        "goal_conceded": [4, 0, 0, 0, 0, 0, 0, 0, 0],
        "goal_assists": [np.nan, np.nan, np.nan, np.nan, 1, np.nan, 1, np.nan, 1],
        "goal_saves": [np.nan, np.nan, np.nan, 6, np.nan, np.nan, np.nan, np.nan, np.nan],
    }
    expected = pd.DataFrame(for_dataframe)
    obtained = get_info_goal_by_player_from_data(data)
    assert_frame_equal(expected, obtained)


def test_get_info_passes_by_player_from_data():
    for_dataframe = {
        "passes_total": [20, 39, 40, 34, 29, 32, 63, 24, 13],
        "passes_key": [1, np.nan, np.nan, np.nan, 1, np.nan, 2, 1, 2],
        "passes_accuracy": [16, 32, 37, 29, 21, 24, 45, 21, 13],
    }
    expected = pd.DataFrame(for_dataframe)
    obtained = get_info_passes_by_player_from_data(data)
    assert_frame_equal(expected, obtained)


def test_get_info_tackles_by_player_from_data():
    for_dataframe = {
        "tackles_total": [np.nan, 5, 4, np.nan, 3, 5, 1, 3, np.nan],
        "tackles_blocks": [None, None, None, None, None, None, None, None, None],
        "tackles_interceptions": [np.nan, 1, np.nan, np.nan, 1, 1, 3, np.nan, np.nan],
    }
    expected = pd.DataFrame(for_dataframe)
    obtained = get_info_tackles_by_player_from_data(data)
    assert_frame_equal(expected, obtained)
