weights = {
            'small_importancy': 1.0,
            'regular_importancy': 2.0,
            'great_importancy': 3.0,
            'extreme_importancy': 5.0,
            'no_importancy': 0
        }


kpi_scoring_fcm = {

    "build-up accuracy" : {
        'accurate_passes_percent' : 0.1
        ,'successful_forward_passes_percent' : 0.1
        ,'successful_back_passes_percent' : 0.1
        ,'successful_vertical_passes_percent' : 0.1
        ,'accurate_short_medium_pass_percent' : 0.1
        ,'successful_long_passes_percent' : 0.1
        ,'accurate_passes_to_final_third_percent' : 0.1
        ,'accurate_pass_to_penalty_area_percent' : 0.1
        ,'successful_through_passes_percent' : 0.1
        ,'successful_progressive_pass_percent' : 0.1},

    "build-up involvement" : {
        'received_pass_avg' : 0.1
        ,'received_long_pass_avg' : 0.1 
        ,'forward_passes_avg' : 0.1
        ,'back_passes_avg' : 0.1
        ,'vertical_passes_avg' : 0.1
        ,'short_medium_pass_avg' : 0.1
        ,'long_passes_avg' : 0.1
        ,'key_passes_avg' : 0.1
        ,'passes_to_final_third_avg' : 0.1
        ,'pass_to_penalty_area_avg' : 0.1
        ,'through_passes_avg' : 0.1 
    },

    "build-up progressiveness" : {
        'forward_passes_ratio' : 0.3
        ,'key_passes_ratio' : 0.15
        ,'passes_to_final_third_ratio' : 0.3
        ,'pass_to_penalty_area_ratio': 0.1 
        ,'through_passes_ratio' : 0.15

    },

    "defensive_intensity": {
        'defensive_duels_avg': 0.4
        ,'aerial_duels_avg': 0.15
        ,'fouls_avg': 0.1
        ,'interceptions_avg': 0.1
        ,'shot_block_avg': 0.05
        ,'tackle_avg': 0.1
        ,"loose_ball_duels_avg" : 0.1
    },

    "defensive_accuracy": {
        'defensive_duels_won': 0.5
        ,'aerial_duels_won': 0.1
        ,'foul_making_avg': 0.05
        ,'interceptions_avg': 0.1
        ,'tackle_avg': 0.1
        ,'shot_block_avg': 0.05
        ,"loose_ball_duels_won" : 0.1
    },

    "aerial_power": {
        'aerial_duels_won': 0.7
        ,'head_goals_avg': 0.1
        ,'aerial_duels_avg': 0.2
    },


    "crossing": {
        'cross_to_goalie_box_avg': 0.15
        ,'accurate_crosses_percent' : 0.4
        ,'deep_completed_cross_avg': 0.15
        ,'succeed_crosses_avg': 0.15
        ,"cross_eagerness": 0.15
    },

    "creativity": {                         
        "xg_assist_avg": 0.15
        ,"assists_avg": 0.15
        ,'deep_completed_pass_avg': 0.1
        ,'key_passes_avg': 0.1
        ,'pre_assist_avg': 0.1
        ,'pre_pre_assist_avg': 0.1
        ,'shot_assists_avg': 0.1
        ,'succeed_pass_to_penalty_area_avg': 0.1
        ,'succeed_through_passes_avg': 0.1
        ,'forward_pass_eagerness': 0.1
    },

    "ball_carrying": {
        "accelerations_avg": 0.4
        ,"progressive_run_avg": 0.4
        ,"run_eagerness": 0.2
    },

    "dribbling": {
        'dribble_eagerness': 0.1
        ,'succeed_dribbles_avg': 0.25
        ,'foul_suffered_avg': 0.1
        ,'touch_in_box_avg' : 0.1
        ,'successful_dribbles_percent' : 0.45
    },

    "finishing": {
        "shot_eagerness": 0.05
        ,'shot_location_quality': 0.05
        ,'head_goals_avg': 0.1
        ,'goals_avg' : 0.2
        ,'succeed_shots_avg': 0.1
        ,'non_pen_goals-xg_goals_avg': 0.5
    },

    "duel_power": {
        "succeed_loose_ball_duels_avg" : 0.100
        ,"loose_ball_duels_won" : 0.150
        ,'succeed_offensive_physical_duels' : 0.125
        ,'offensive_physical_duels_won' : 0.175
        ,'aerial_duels_won' : 0.125
        ,'succeed_aerial_duels_avg' : 0.075
        ,'succeed_defensive_duels_avg' : 0.1
        ,'defensive_duels_won' : 0.15
    },  

    "SP": {
        'corners_taken_avg': 0.3
        ,'free_kicks_taken_avg': 0.25
        ,'direct_free_kicks_taken_avg': 0.25
        ,'accurate_crosses_percent': 0.2
    },

    'goal_keeping': {
        'goalkeeper_exits_avg': 0.15
        ,'save_percent': 0.15
        ,'prevented_goals_avg': 0.4
        ,'conceded_goals_avg': 0.15
        ,'succeed_aerial_duels_avg' : 0.15
    }
}



 
position_score_fcm = { 
    'CF': {
        'small_importancy': ['SP', 'crossing', 'build-up involvement',  "build-up progressiveness"]
        ,'regular_importancy': ['ball_carrying', 'creativity', 'defensive_intensity', 'build-up accuracy']
        ,'great_importancy': ['dribbling', 'duel_power', 'aerial_power']
        ,'extreme_importancy': ['finishing']
        ,'no_importancy': ['goal_keeping']
    },

    'CB': {
        'small_importancy': ['SP'],
        'regular_importancy': ['ball_carrying', 'dribbling', 'build-up involvement'],
        'great_importancy': ['defensive_intensity', "build-up progressiveness", 'aerial_power'],
        'extreme_importancy': ['defensive_accuracy', 'duel_power', 'build-up accuracy'],
        'no_importancy': ['goal_keeping', 'creativity', 'finishing', 'crossing']
    },

    'RB': {
        'small_importancy': ['SP', 'finishing'],
        'regular_importancy': ['creativity', 'build-up involvement', "build-up progressiveness", 'aerial_power'],
        'great_importancy': ['ball_carrying', 'dribbling', 'duel_power', 'defensive_intensity', 'build-up accuracy'],
        'extreme_importancy': ['defensive_accuracy', 'crossing'],
        'no_importancy': ['goal_keeping']
    },


    'LB': {
        'small_importancy': ['aerial_power', 'SP', 'finishing'],
        'regular_importancy': ['creativity', 'build-up involvement',  "build-up progressiveness"],
        'great_importancy': ['ball_carrying', 'dribbling', 'duel_power', 'defensive_intensity'],
        'extreme_importancy': ['defensive_accuracy', 'crossing', 'build-up accuracy'],
        'no_importancy': ['goal_keeping']
    },

    'RW': {
        'small_importancy': ['aerial_power', 'SP', 'defensive_accuracy', 'build-up involvement'],
        'regular_importancy': ['defensive_intensity', 'duel_power', "build-up progressiveness", 'build-up accuracy'],
        'great_importancy': ['ball_carrying', 'finishing'],
        'extreme_importancy': ['dribbling', 'creativity', 'crossing'],
        'no_importancy': ['goal_keeping']
    },

    'LW': {
        'small_importancy': ['aerial_power', 'SP', 'defensive_accuracy', 'build-up involvement'],
        'regular_importancy': ['defensive_intensity', 'duel_power', "build-up progressiveness", 'build-up accuracy'],
        'great_importancy': ['ball_carrying', 'finishing'],
        'extreme_importancy': ['dribbling', 'creativity', 'crossing'],
        'no_importancy': ['goal_keeping']
    },

    'CM': {
        'small_importancy': ['aerial_power', 'SP'],
        'regular_importancy': ['finishing', 'crossing'],
        'great_importancy': ['creativity', 'ball_carrying', 'defensive_intensity', 'defensive_accuracy', "build-up progressiveness", 'build-up involvement'],
        'extreme_importancy': ['dribbling', 'build-up accuracy', 'duel_power'],
        'no_importancy': ['goal_keeping']
    },


    'CAM': {
        'small_importancy': ['SP'],
        'regular_importancy': ['crossing', 'defensive_intensity', 'defensive_accuracy', 'aerial_power'],
        'great_importancy': ['creativity', 'ball_carrying', 'build-up accuracy', 'build-up involvement'],
        'extreme_importancy': ['dribbling', 'duel_power', 'finishing', "build-up progressiveness"],
        'no_importancy': ['goal_keeping']
    },

    'GK': {
        'small_importancy': [],
        'regular_importancy': ["build-up progressiveness", 'build-up involvement'],
        'great_importancy': ['build-up accuracy'],
        'extreme_importancy': ['goal_keeping'],
        'no_importancy': ['creativity', 'ball_carrying', 'dribbling', 'finishing', 'defensive_intensity', 'defensive_accuracy', 'crossing', 'aerial_power', 'SP']
    }
}