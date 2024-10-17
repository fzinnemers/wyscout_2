# All columns related to a specific action of a player
wyscout_score_columns = ["goals", "xg_shot", "assists", "xg_assist", "duels_avg", "duels_won", "successful_defensive_actions_avg", "defensive_duels_avg", 
    "defensive_duels_won", "aerial_duels_avg", "aerial_duels_won", "tackle_avg", "possession_adjusted_tackle", 
    "shot_block_avg", "interceptions_avg", "possession_adjusted_interceptions", "fouls_avg", "yellow_cards", 
    "yellow_cards_avg", "red_cards", "red_cards_avg", "successful_attacking_actions_avg", "goals_avg", 
    "non_penalty_goal", "non_penalty_goal_avg", 'xg_shot_avg','head_goals','head_goals_avg','shots','shots_avg',
    'shots_on_target_percent','goal_conversion_percent','assists_avg','crosses_avg', 'accurate_crosses_percent','cross_from_left_avg',
    'successful_cross_from_left_percent','cross_from_right_avg','successful_cross_from_right_percent','cross_to_goalie_box_avg',
    'dribbles_avg','successful_dribbles_percent','offensive_duels_avg','offensive_duels_won','touch_in_box_avg',
    'progressive_run_avg','accelerations_avg','received_pass_avg','received_long_pass_avg','foul_suffered_avg','passes_avg',
    'accurate_passes_percent','forward_passes_avg','successful_forward_passes_percent','back_passes_avg','successful_back_passes_percent',
    'vertical_passes_avg','successful_vertical_passes_percent', 'short_medium_pass_avg','accurate_short_medium_pass_percent',
    'long_passes_avg','successful_long_passes_percent','average_pass_length','average_long_pass_length','xg_assist_avg',
    'shot_assists_avg','pre_assist_avg','pre_pre_assist_avg','smart_passes_avg','accurate_smart_passes_percent','key_passes_avg',
    'passes_to_final_third_avg','accurate_passes_to_final_third_percent','pass_to_penalty_area_avg',
    'accurate_pass_to_penalty_area_percent','through_passes_avg','successful_through_passes_percent',
    'deep_completed_pass_avg','deep_completed_cross_avg','progressive_pass_avg','successful_progressive_pass_percent',
    'conceded_goals','conceded_goals_avg','shots_against','shots_against_avg','clean_sheets','save_percent','xg_save',
    'xg_save_avg','prevented_goals','prevented_goals_avg','back_pass_to_gk_avg','goalkeeper_exits_avg','gk_aerial_duels_avg',
    'free_kicks_taken_avg','direct_free_kicks_taken_avg','direct_free_kicks_on_target_percent','corners_taken_avg','penalties_taken',
    'penalties_conversion_percent']

# personal information about the player not related to any 
wyscout_personal_columns =  ['id', 'full_name', 'name', 'birth_date', 'birth_day', "age", "image", 'birth_country_name', 'birth_country_code','passport_country_codes1',
                    'passport_country_codes2', 'passport_country_codes', 'passport_country_names', 'passport_country_names1', 'passport_country_names2', 'positions',
                    'positions1', 'positions2','positions3','primary_position','primary_position_percent', 'secondary_position','secondary_position_percent', 
                    'third_position', 'third_position_percent','contract_expires', "market_value", "total_matches", "minutes_on_field", "foot", "height", "weight", 
                    "on_loan"]

# Information about the team the player is playing in 
wyscout_team_season_columns = ['domestic_competition_name', 'current_team_name', 'current_team_color', 'current_team_logo', 'last_club_name', 'league_id', 'division', 
                       'league_country', 'year', 'start_moment', 'league_competition']

# This are the columns that are new in Wyscout but are only measured in some leagues
wyscout_pilot_columns = ['high_speed_running_count_avg','sprinting_distance_avg','high_deceleration_count_avg','medium_deceleration_count_avg',
 'running_distance_avg','high_acceleration_count_avg','sprint_count_avg','medium_acceleration_count_avg','meters_per_minute','total_distance_avg',
 'max_speed','high_intensity_count_avg','high_speed_running_distance_avg','high_intensity_distance_avg']


pos_translation_dict = {
    'LCMF3': 'CM',
    'CF': 'CF',
    'LAMF': 'LW',
    'RWB': 'RB',
    'RAMF': 'RW',
    'DMF': 'CM',
    'RWF': 'RW',
    'LB': 'LB',
    'AMF': 'CAM',
    'LCB': 'CB',
    'LCMF': 'CM',
    'LW': 'LW',
    'RCMF': 'CM',
    'LDMF': 'CM',
    'RW': 'RW',
    'RDMF': 'CM',
    'RB': 'RB',
    'RCB': 'CB',
    'LWB': 'LB',
    'LCB3': 'CB',
    'RCMF3': 'CM',
    'CB': 'CB',
    'RCB3': 'CB',
    'LWF': 'LW',
    "LB5": "LB",
    "RB5": "RB",
    'RCB3': "CB",
    'GK': "GK",
    ''  : 'UNKNOWN'
}