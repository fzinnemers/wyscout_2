succeed_actions_variables = [
    ['crosses_avg', 'accurate_crosses_percent'],
    ['aerial_duels_avg', 'aerial_duels_won'],
    ['smart_passes_avg', 'accurate_smart_passes_percent'],
    ['short_medium_pass_avg', 'accurate_short_medium_pass_percent'],
    ['pass_to_penalty_area_avg', 'accurate_pass_to_penalty_area_percent'],
    ['passes_avg', 'accurate_passes_percent'],
    ['dribbles_avg', 'successful_dribbles_percent'],
    ['cross_from_left_avg', 'successful_cross_from_left_percent'],
    ['cross_from_right_avg', 'successful_cross_from_right_percent'],
    ['offensive_duels_avg', 'offensive_duels_won'],
    ['duels_avg', 'duels_won'],
    ['forward_passes_avg', 'successful_forward_passes_percent'],
    ['long_passes_avg', 'successful_long_passes_percent'],
    ['progressive_pass_avg', 'successful_progressive_pass_percent'],
    ['through_passes_avg', 'successful_through_passes_percent'],
    ['vertical_passes_avg', 'successful_vertical_passes_percent'],
    ['defensive_duels_avg', 'defensive_duels_won'],
    ['direct_free_kicks_taken_avg', 'direct_free_kicks_on_target_percent'],
    ['passes_to_final_third_avg', 'accurate_passes_to_final_third_percent'],
    ['back_passes_avg', 'successful_back_passes_percent'],
    ['penalties_taken', 'penalties_conversion_percent'],
    ['shots_avg', 'shots_on_target_percent'],
    ['loose_ball_duels_avg', 'loose_ball_duels_won'],
    ['offensive_physical_duels', 'offensive_physical_duels_won']
]

in_possession_variables =  ["successful_attacking_actions_avg", "goals_avg", "non_penalty_goal_avg", "xg_shot_avg", "head_goals_avg", "shots_avg", "assists_avg", "crosses_avg",
                            "cross_from_left_avg", "cross_from_right_avg", "cross_to_goalie_box_avg", "dribbles_avg", "offensive_duels_avg", 'offensive_physical_duels', 'succeed_offensive_physical_duels',"touch_in_box_avg", "progressive_run_avg",
                            "accelerations_avg", "received_pass_avg", "received_long_pass_avg", "passes_avg", "forward_passes_avg", "back_passes_avg", "vertical_passes_avg", 
                            "short_medium_pass_avg", "long_passes_avg", "xg_assist_avg", "shot_assists_avg", "pre_assist_avg", "pre_pre_assist_avg", "smart_passes_avg", "key_passes_avg", 
                            "passes_to_final_third_avg", "pass_to_penalty_area_avg", "through_passes_avg", "deep_completed_pass_avg", "deep_completed_cross_avg", "progressive_pass_avg", 
                            "conceded_goals_avg", "shots_against_avg","xg_save_avg", "prevented_goals_avg", "back_pass_to_gk_avg", "goalkeeper_exits_avg", "gk_aerial_duels_avg", 
                            "free_kicks_taken_avg", "direct_free_kicks_taken_avg", "corners_taken_avg", "penalties_taken", "foul_suffered_avg", "succeed_short_medium_pass_avg", 'run_eagerness',
                            'succeed_offensive_duels_avg', 'succeed_vertical_passes_avg', 'succeed_crosses_avg', 'succeed_through_passes_avg', 'succeed_long_passes_avg',  'succeed_forward_passes_avg',
                            'succeed_shots_avg','succeed_cross_from_right_avg', 'cross_eagerness', 'succeed_progressive_pass_avg', 'shot_location_quality',
                            'goals-xg_goals_avg', 'succeed_passes_avg', 'succeed_direct_free_kicks_taken_avg', 'succeed_smart_passes_avg','dribble_eagerness', 'forward_pass_eagerness',
                            'succeed_dribbles_avg','succeed_back_passes_avg',  'succeed_passes_to_final_third_avg','non_pen_goals-xg_goals_avg','shot_eagerness','succeed_cross_from_left_avg','succeed_pass_to_penalty_area_avg',
                            ]

out_possession_variables = ["successful_defensive_actions_avg", "defensive_duels_avg", "tackle_avg", "shot_block_avg", "interceptions_avg", "fouls_avg", 'succeed_defensive_duels_avg',
                             'foul_making_avg', "yellow_cards_avg", "red_cards_avg"]

no_possession_influence_variables = ["goals", "xg_shot", "assists", "xg_assist", "duels_avg", "duels_won", "defensive_duels_won", "aerial_duels_avg", "aerial_duels_won", 
                                    "possession_adjusted_tackle", "red_cards", "non_penalty_goal",
                                    "head_goals", "shots", "shots_on_target_percent", "goal_conversion_percent", "accurate_crosses_percent", "successful_cross_from_left_percent",
                                    "successful_cross_from_right_percent", "successful_dribbles_percent", "offensive_duels_won", 'offensive_physical_duels_won', "accurate_passes_percent",
                                    "successful_forward_passes_percent", "successful_back_passes_percent", "successful_vertical_passes_percent", "accurate_short_medium_pass_percent", 
                                    "successful_long_passes_percent", "average_pass_length", "average_long_pass_length", "accurate_smart_passes_percent", 
                                    "accurate_passes_to_final_third_percent", "accurate_pass_to_penalty_area_percent", "successful_through_passes_percent", 
                                    "successful_progressive_pass_percent", "conceded_goals", "shots_against", "clean_sheets", "save_percent", "xg_save", "prevented_goals", 
                                    "direct_free_kicks_on_target_percent", "penalties_conversion_percent", "possession_adjusted_interceptions", 'succeed_penalties_taken', 
                                    'succeed_duels_avg', 'succeed_aerial_duels_avg', "yellow_cards", 'loose_ball_duels_avg', 'loose_ball_duels_won','passes_to_final_third_ratio', 
                                    'through_passes_ratio', 'key_passes_ratio', 'forward_passes_ratio', 'pass_to_penalty_area_ratio', 'succeed_loose_ball_duels_avg', 'high_speed_running_count_avg','sprinting_distance_avg','high_deceleration_count_avg','medium_deceleration_count_avg',
                                    'running_distance_avg','high_acceleration_count_avg','sprint_count_avg','medium_acceleration_count_avg','meters_per_minute','total_distance_avg',
                                    'max_speed','high_intensity_count_avg','high_speed_running_distance_avg','high_intensity_distance_avg']
