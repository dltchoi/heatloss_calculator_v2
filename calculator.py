def heatloss_estimate (gasuse_total, dhw_monthly, balance_point, furnace_eff, hl_derate, location, heatpumpsize, heatpumpcap_17_c1, heatpumpcap_47_c1, heatpumpcap_17_c2, heatpumpcap_47_c2, heatpumpcap_17_c3, heatpumpcap_47_c3, hp_derate, derate_c1, derate_c2, derate_c3):
    import pandas as pd
    import numpy as np
    import math
    from datetime import datetime
    import datetime

    estimate_2021=[]
    start_2021 = '2021-01-01 00:00:00'
    end_2021 = '2021-12-31 23:00:00'
    # import weather data and specify design temperature based on location
    if location == 'toronto':
        weatherdata = pd.read_csv("static/5yr_toronto_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Toronto'
        dtemp = -16.3
    elif location == 'london':
        weatherdata = pd.read_csv("static/5yr_london_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'London'
        dtemp = -18.4
    elif location == 'niagarafalls':
        weatherdata = pd.read_csv("static/5yr_niagarafalls_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Niagara Falls'
        dtemp = -13
    elif location == 'ottawa':
        weatherdata = pd.read_csv("static/5yr_ottawa_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Ottawa'
        dtemp = -24.3
    elif location == 'sudbury':
        weatherdata = pd.read_csv("static/5yr_sudbury_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Sudbury'
        dtemp = -27.7
    elif location == 'markham':
        weatherdata = pd.read_csv("static/5yr_markham_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Markham'
        dtemp = -19.8
    elif location == 'brampton':
        weatherdata = pd.read_csv("static/5yr_brampton_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Brampton'
        dtemp = -18.3
    elif location == 'mississauga':
        weatherdata = pd.read_csv("static/5yr_mississauga_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Mississauga'
        dtemp = -18.3
    elif location == 'burlington':
        weatherdata = pd.read_csv("static/5yr_burlington_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Burlington'
        dtemp = -15.6
    elif location == 'hamilton':
        weatherdata = pd.read_csv("static/5yr_hamilton_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Hamilton'
        dtemp = -15.6
    elif location == 'oakville':
        weatherdata = pd.read_csv("static/5yr_oakville_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Oakville'
        dtemp = -15.6
    elif location == 'windsor':
        weatherdata = pd.read_csv("static/5yr_windsor_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Windsor'
        dtemp = -15.2
    elif location == 'stratford':
        weatherdata = pd.read_csv("static/5yr_stratford_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Stratford'
        dtemp = -18.4
    elif location == 'richmondhill':
        weatherdata = pd.read_csv("static/5yr_richmondhill_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Richmond Hill'
        dtemp = -19.8
    elif location == 'vaughan':
        weatherdata = pd.read_csv("static/5yr_vaughan_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Vaughan'
        dtemp = -19.8
    elif location == 'oshawa':
        weatherdata = pd.read_csv("static/5yr_oshawa_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Oshawa'
        dtemp = -19.8
    elif location == 'pickering':
        weatherdata = pd.read_csv("static/5yr_pickering_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Pickering'
        dtemp = -19.8
    elif location == 'cobourg':
        weatherdata = pd.read_csv("static/5yr_cobourg_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Cobourg'
        dtemp = -19.4
    elif location == 'peterborough':
        weatherdata = pd.read_csv("static/5yr_peterborough_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Peterborough'
        dtemp = -23.3
    elif location == 'orillia':
        weatherdata = pd.read_csv("static/5yr_orillia_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Orillia'
        dtemp = -23.5
    elif location == 'barrie':
        weatherdata = pd.read_csv("static/5yr_barrie_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Barrie'
        dtemp = -18.5
    elif location == 'collingwood':
        weatherdata = pd.read_csv("static/5yr_collingwood_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Collingwood'
        dtemp = -18.5
    elif location == 'guelph':
        weatherdata = pd.read_csv("static/5yr_guelph_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Guelph'
        dtemp = -15.6
    elif location == 'kitchener-waterloo':
        weatherdata = pd.read_csv("static/5yr_kitchenerwaterloo_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Kitchener - Waterloo'
        dtemp = -15.6
    elif location == 'goderich':
        weatherdata = pd.read_csv("static/5yr_goderich_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Goderich'
        dtemp = -16.5
    elif location == 'owensound':
        weatherdata = pd.read_csv("static/5yr_owensound_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Owen Sound'
        dtemp = -18.3
    elif location == 'gravenhurst':
        weatherdata = pd.read_csv("static/5yr_gravenhurst_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Gravenhurst'
        dtemp = -26.6
    elif location == 'parrysound':
        weatherdata = pd.read_csv("static/5yr_parrysound_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Parry Sound'
        dtemp = -26.6
    elif location == 'bancroft':
        weatherdata = pd.read_csv("static/5yr_bancroft_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Bancroft'
        dtemp = -28.7
    elif location == 'northbay':
        weatherdata = pd.read_csv("static/5yr_northbay_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'North Bay'
        dtemp = -27.8
    elif location == 'kingston':
        weatherdata = pd.read_csv("static/5yr_kingston_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Kingston'
        dtemp = -19.9
    elif location == 'trenton':
        weatherdata = pd.read_csv("static/5yr_trenton_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Trenton'
        dtemp = -21.8
    elif location == 'timmins':
        weatherdata = pd.read_csv("static/5yr_timmins_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Timmins'
        dtemp = -32.2
    elif location == 'thunderbay':
        weatherdata = pd.read_csv("static/5yr_thunderbay_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Thunder Bay'
        dtemp = -28.6
    elif location == 'kenora':
        weatherdata = pd.read_csv("static/5yr_kenora_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Kenora'
        dtemp = -30.5
    elif location == 'saultstemarie':
        weatherdata = pd.read_csv("static/5yr_saultstemarie_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Sault Ste. Marie'
        dtemp = -24
    elif location == 'orangeville':
        weatherdata = pd.read_csv("static/5yr_orangeville_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Orangeville'
        dtemp = -18.3
    elif location == 'wiarton':
        weatherdata = pd.read_csv("static/5yr_wiarton_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Wiarton'
        dtemp = -18.3
    elif location == 'cornwall':
        weatherdata = pd.read_csv("static/5yr_cornwall_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Cornwall'
        dtemp = -24.9
    elif location == 'newmarket':
        weatherdata = pd.read_csv("static/5yr_newmarket_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Newmarket'
        dtemp = -19.8
    elif location == 'pembroke':
        weatherdata = pd.read_csv("static/5yr_pembroke_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Pembroke'
        dtemp = -28.7
    elif location == 'picton':
        weatherdata = pd.read_csv("static/5yr_picton_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Picton'
        dtemp = -19.9
    elif location == 'whiteriver':
        weatherdata = pd.read_csv("static/5yr_whiteriver_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'White River'
        dtemp = -28.5
    elif location == 'moosonee':
        weatherdata = pd.read_csv("static/5yr_moosonee_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Moosonee'
        dtemp = -33.8
    elif location == 'peawanuck':
        weatherdata = pd.read_csv("static/5yr_peawanuck_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Peawanuck'
        dtemp = -37.3
    elif location == 'bigtroutlake':
        weatherdata = pd.read_csv("static/5yr_bigtroutlake_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Big Trout Lake'
        dtemp = -36.2
    elif location == 'sandylake':
        weatherdata = pd.read_csv("static/5yr_sandylake_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Sandy Lake'
        dtemp = -34.8
    elif location == 'redlake':
        weatherdata = pd.read_csv("static/5yr_redlake_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Red Lake'
        dtemp = -30.5
    elif location == 'dryden':
        weatherdata = pd.read_csv("static/5yr_dryden_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Dryden'
        dtemp = -31.9
    elif location == 'kapuskasing':
        weatherdata = pd.read_csv("static/5yr_kapuskasing_weather.csv",parse_dates=['date_time_local'])
        weatherdata = weatherdata.set_index('date_time_local')
        estimate_2021 = weatherdata.loc[start_2021 : end_2021]
        location_name = 'Kapuskasing'
        dtemp = -33.1

    # standard heat pump performance data points (Goodman 9.0 HSPF, 15 SEER)
    hp_derate = 1-(hp_derate/100) # convert heat pump derate
    m_15 = ((18-10)*hp_derate)/(8.3+8.3)
    b_15 = (18*hp_derate)-(m_15*8.3)
    m_2 = ((23.2-12.6)*hp_derate)/(8.3+8.3)
    b_2 = (23.2*hp_derate)-(m_2*8.3)
    m_25 = ((28.4-16.2)*hp_derate)/(8.3+8.3)
    b_25 = (28.4*hp_derate)-(m_25*8.3)
    m_3 = ((32.8-19)*hp_derate)/(8.3+8.3)
    b_3 = (32.8*hp_derate)-(m_3*8.3)
    m_35 = ((40-24)*hp_derate)/(8.3+8.3)
    b_35 = (40*hp_derate)-(m_35*8.3)
    m_4 = ((44.5-28)*hp_derate)/(8.3+8.3)
    b_4 = (44.5*hp_derate)-(m_4*8.3)
    m_5 = ((59-36)*hp_derate)/(8.3+8.3)
    b_5 = (59*hp_derate)-(m_5*8.3)

    # standard heat pump cops
    # 1.5 ton
    cop_65_15 = 4.60
    cop_60_15 = 4.37
    cop_55_15 = 4.15
    cop_50_15 = 3.92
    cop_47_15 = 3.76
    cop_45_15 = 3.63
    cop_40_15 = 3.31
    cop_35_15 = 3.01
    cop_30_15 = 2.76
    cop_25_15 = 2.59
    cop_20_15 = 2.46
    cop_17_15 = 2.40
    cop_15_15 = 2.29
    cop_10_15 = 2.02
    cop_5_15 = 1.74
    cop_0_15 = 1.43
    cop_neg5_15 = 1.11

    scop_15 = [0,0,0,0,0,0,0,0,0,
            cop_neg5_15,cop_neg5_15,cop_neg5_15,
            cop_0_15,cop_0_15,
            cop_5_15,cop_5_15,cop_5_15,
            cop_10_15,cop_10_15,cop_10_15,
            cop_15_15,cop_17_15,cop_17_15,
            cop_20_15,cop_20_15,cop_20_15,
            cop_25_15,cop_25_15,
            cop_30_15,cop_30_15,
            cop_35_15,cop_35_15,cop_35_15,
            cop_40_15,cop_40_15,cop_40_15,
            cop_45_15,cop_47_15,cop_47_15,
            cop_50_15,cop_50_15,
            cop_55_15,cop_55_15,cop_55_15,
            cop_60_15,cop_60_15,cop_60_15,
            cop_65_15
            ]

    # 2 ton
    cop_65_2 = 4.57
    cop_60_2 = 4.36
    cop_55_2 = 4.14
    cop_50_2 = 3.91
    cop_47_2 = 3.76
    cop_45_2 = 3.63
    cop_40_2 = 3.31
    cop_35_2 = 3.00
    cop_30_2 = 2.76
    cop_25_2 = 2.58
    cop_20_2 = 2.46
    cop_17_2 = 2.40
    cop_15_2 = 2.29
    cop_10_2 = 2.01
    cop_5_2 = 1.71
    cop_0_2 = 1.39
    cop_neg5_2 = 1.05

    scop_2 = [0,0,0,0,0,0,0,0,0,
            cop_neg5_2,cop_neg5_2,cop_neg5_2,
            cop_0_2,cop_0_2,
            cop_5_2,cop_5_2,cop_5_2,
            cop_10_2,cop_10_2,cop_10_2,
            cop_15_2,cop_17_2,cop_17_2,
            cop_20_2,cop_20_2,cop_20_2,
            cop_25_2,cop_25_2,
            cop_30_2,cop_30_2,
            cop_35_2,cop_35_2,cop_35_2,
            cop_40_2,cop_40_2,cop_40_2,
            cop_45_2,cop_47_2,cop_47_2,
            cop_50_2,cop_50_2,
            cop_55_2,cop_55_2,cop_55_2,
            cop_60_2,cop_60_2,cop_60_2,
            cop_65_2
            ]

    # 2.5 ton
    cop_65_25 = 4.39
    cop_60_25 = 4.20
    cop_55_25 = 4.00
    cop_50_25 = 3.80
    cop_47_25 = 3.66
    cop_45_25 = 3.55
    cop_40_25 = 3.26
    cop_35_25 = 2.99
    cop_30_25 = 2.77
    cop_25_25 = 2.61
    cop_20_25 = 2.51
    cop_17_25 = 2.46
    cop_15_25 = 2.36
    cop_10_25 = 2.12
    cop_5_25 = 1.85
    cop_0_25 = 1.57
    cop_neg5_25 = 1.27

    scop_25 = [0,0,0,0,0,0,0,0,0,
            cop_neg5_25,cop_neg5_25,cop_neg5_25,
            cop_0_25,cop_0_25,
            cop_5_25,cop_5_25,cop_5_25,
            cop_10_25,cop_10_25,cop_10_25,
            cop_15_25,cop_17_25,cop_17_25,
            cop_20_25,cop_20_25,cop_20_25,
            cop_25_25,cop_25_25,
            cop_30_25,cop_30_25,
            cop_35_25,cop_35_25,cop_35_25,
            cop_40_25,cop_40_25,cop_40_25,
            cop_45_25,cop_47_25,cop_47_25,
            cop_50_25,cop_50_25,
            cop_55_25,cop_55_25,cop_55_25,
            cop_60_25,cop_60_25,cop_60_25,
            cop_65_25
            ]

    # 3 ton
    cop_65_3 = 4.46
    cop_60_3 = 4.24
    cop_55_3 = 4.03
    cop_50_3 = 3.81
    cop_47_3 = 3.66
    cop_45_3 = 3.55
    cop_40_3 = 3.24
    cop_35_3 = 2.96
    cop_30_3 = 2.73
    cop_25_3 = 2.57
    cop_20_3 = 2.46
    cop_17_3 = 2.40
    cop_15_3 = 2.30
    cop_10_3 = 2.06
    cop_5_3 = 1.80
    cop_0_3 = 1.53
    cop_neg5_3 = 1.24

    scop_3 = [0,0,0,0,0,0,0,0,0,
            cop_neg5_3,cop_neg5_3,cop_neg5_3,
            cop_0_3,cop_0_3,
            cop_5_3,cop_5_3,cop_5_3,
            cop_10_3,cop_10_3,cop_10_3,
            cop_15_3,cop_17_3,cop_17_3,
            cop_20_3,cop_20_3,cop_20_3,
            cop_25_3,cop_25_3,
            cop_30_3,cop_30_3,
            cop_35_3,cop_35_3,cop_35_3,
            cop_40_3,cop_40_3,cop_40_3,
            cop_45_3,cop_47_3,cop_47_3,
            cop_50_3,cop_50_3,
            cop_55_3,cop_55_3,cop_55_3,
            cop_60_3,cop_60_3,cop_60_3,
            cop_65_3
            ]

    # 3.5 ton
    cop_65_35 = 4.44
    cop_60_35 = 4.24
    cop_55_35 = 4.04
    cop_50_35 = 3.84
    cop_47_35 = 3.70
    cop_45_35 = 3.60
    cop_40_35 = 3.32
    cop_35_35 = 3.05
    cop_30_35 = 2.84
    cop_25_35 = 2.69
    cop_20_35 = 2.59
    cop_17_35 = 2.54
    cop_15_35 = 2.45
    cop_10_35 = 2.22
    cop_5_35 = 1.98
    cop_0_35 = 1.72
    cop_neg5_35 = 1.45

    scop_35 = [0,0,0,0,0,0,0,0,0,
            cop_neg5_35,cop_neg5_35,cop_neg5_35,
            cop_0_35,cop_0_35,
            cop_5_35,cop_5_35,cop_5_35,
            cop_10_35,cop_10_35,cop_10_35,
            cop_15_35,cop_17_35,cop_17_35,
            cop_20_35,cop_20_35,cop_20_35,
            cop_25_35,cop_25_35,
            cop_30_35,cop_30_35,
            cop_35_35,cop_35_35,cop_35_35,
            cop_40_35,cop_40_35,cop_40_35,
            cop_45_35,cop_47_35,cop_47_35,
            cop_50_35,cop_50_35,
            cop_55_35,cop_55_35,cop_55_35,
            cop_60_35,cop_60_35,cop_60_35,
            cop_65_35
            ]

    # 4 ton
    cop_65_4 = 4.72
    cop_60_4 = 4.49
    cop_55_4 = 4.25
    cop_50_4 = 4.02
    cop_47_4 = 3.86
    cop_45_4 = 3.74
    cop_40_4 = 3.45
    cop_35_4 = 3.17
    cop_30_4 = 2.94
    cop_25_4 = 2.77
    cop_20_4 = 2.66
    cop_17_4 = 2.60
    cop_15_4 = 2.51
    cop_10_4 = 2.28
    cop_5_4 = 2.04
    cop_0_4 = 1.80
    cop_neg5_4 = 1.56

    scop_4 = [0,0,0,0,0,0,0,0,0,
            cop_neg5_4,cop_neg5_4,cop_neg5_4,
            cop_0_4,cop_0_4,
            cop_5_4,cop_5_4,cop_5_4,
            cop_10_4,cop_10_4,cop_10_4,
            cop_15_4,cop_17_4,cop_17_4,
            cop_20_4,cop_20_4,cop_20_4,
            cop_25_4,cop_25_4,
            cop_30_4,cop_30_4,
            cop_35_4,cop_35_4,cop_35_4,
            cop_40_4,cop_40_4,cop_40_4,
            cop_45_4,cop_47_4,cop_47_4,
            cop_50_4,cop_50_4,
            cop_55_4,cop_55_4,cop_55_4,
            cop_60_4,cop_60_4,cop_60_4,
            cop_65_4
            ]

    # 5 ton
    cop_65_5 = 4.52
    cop_60_5 = 4.35
    cop_55_5 = 4.17
    cop_50_5 = 3.99
    cop_47_5 = 3.86
    cop_45_5 = 3.76
    cop_40_5 = 3.50
    cop_35_5 = 3.25
    cop_30_5 = 3.05
    cop_25_5 = 2.92
    cop_20_5 = 2.84
    cop_17_5 = 2.80
    cop_15_5 = 2.71
    cop_10_5 = 2.49
    cop_5_5 = 2.25
    cop_0_5 = 2.00
    cop_neg5_5 = 1.73

    scop_5 = [0,0,0,0,0,0,0,0,0,
            cop_neg5_5,cop_neg5_5,cop_neg5_5,
            cop_0_5,cop_0_5,
            cop_5_5,cop_5_5,cop_5_5,
            cop_10_5,cop_10_5,cop_10_5,
            cop_15_5,cop_17_5,cop_17_5,
            cop_20_5,cop_20_5,cop_20_5,
            cop_25_5,cop_25_5,
            cop_30_5,cop_30_5,
            cop_35_5,cop_35_5,cop_35_5,
            cop_40_5,cop_40_5,cop_40_5,
            cop_45_5,cop_47_5,cop_47_5,
            cop_50_5,cop_50_5,
            cop_55_5,cop_55_5,cop_55_5,
            cop_60_5,cop_60_5,cop_60_5,
            cop_65_5
            ]

    # gather data based on user heat pump size selections
    m_list = []
    b_list = []
    cop_df = pd.DataFrame()
    
    for i in heatpumpsize:
        if float(i) == 1.5:
            m_list.append(m_15)
            b_list.append(b_15)
            cop_df['scop_15'] = scop_15
        elif float(i) == 2:
            m_list.append(m_2)
            b_list.append(b_2)
            cop_df['scop_2'] = scop_2
        elif float(i) == 2.5:
            m_list.append(m_25)
            b_list.append(b_25)
            cop_df['scop_25'] = scop_25
        elif float(i) == 3:
            m_list.append(m_3)
            b_list.append(b_3)
            cop_df['scop_3'] = scop_3
        elif float(i) == 3.5:
            m_list.append(m_35)
            b_list.append(b_35)
            cop_df['scop_35'] = scop_35
        elif float(i) == 4:
            m_list.append(m_4)
            b_list.append(b_4)
            cop_df['scop_4'] = scop_4
        elif float(i) == 5:
            m_list.append(m_5)
            b_list.append(b_5)
            cop_df['scop_5'] = scop_5

    # import heat pump capacities and capacity derate based on user input
    if (heatpumpcap_17_c1 > 0) & (heatpumpcap_47_c1 > 0):
        m_hp_1 = ((heatpumpcap_47_c1-heatpumpcap_17_c1)*(1-(derate_c1/100)))/(8.3+8.3)
        b_hp_1 = (heatpumpcap_47_c1*(1-(derate_c1/100)))-(m_hp_1*8.3)
        derate_c1 = [round(derate_c1)]
    else:
        m_hp_1 = -999
        b_hp_1 = -999
        derate_c1 = []
    
    if (heatpumpcap_17_c2 > 0) & (heatpumpcap_47_c2 > 0):
        m_hp_2 = ((heatpumpcap_47_c2-heatpumpcap_17_c2)*(1-(derate_c2/100)))/(8.3+8.3)
        b_hp_2 = (heatpumpcap_47_c2*(1-(derate_c2/100)))-(m_hp_2*8.3)
        derate_c2 = [round(derate_c2)]
    else:
        m_hp_2 = -999
        b_hp_2 = -999
        derate_c2 = []

    if (heatpumpcap_17_c3 > 0) & (heatpumpcap_47_c3 > 0):
        m_hp_3 = ((heatpumpcap_47_c3-heatpumpcap_17_c3)*(1-(derate_c3/100)))/(8.3+8.3)
        b_hp_3 = (heatpumpcap_47_c3*(1-(derate_c3/100)))-(m_hp_3*8.3)
        derate_c3 = [round(derate_c3)]
    else:
        m_hp_3 = -999
        b_hp_3 = -999
        derate_c3 = []

    # calculate annual gas use from furnace
    dhw_annual = dhw_monthly*12
    gasuse_annual = gasuse_total - dhw_annual
    
    # define variables and state first heat loss guess
    heatloss_guess = 10 # kBtu/hr - first guess of heat loss at -15C (not a reasonable guess, but a relatively low value to reduce runtime)
    gas_estimate_total = 0
    
    # loop through different heat loss estimates until annual usage estimate is close to the user input
    while int(gas_estimate_total) < gasuse_annual*(1+(hl_derate/100)):
        heatloss_guess += 1
        # estimate heat loss slope and intercept with each guess
        m = (heatloss_guess - 0)/(-15 - balance_point)
        b = 0 - (m * balance_point)
    
    # estimate hourly heat loss based on weather data
        heatloss = []
        for x in estimate_2021.temperature:
            if x > balance_point:
                heatloss.append(0)
            else:
                heatloss.append(m * x + b)
        estimate_2021['heatloss'] = heatloss
        estimate_2021['gas_m3'] = estimate_2021.heatloss * (1/3.41) * (1/10.5) * (1/(furnace_eff/100))
    
    # calculate total annual estimated gas use
        gas_estimate_total = estimate_2021.gas_m3.sum()

        if int(gas_estimate_total) == gasuse_annual*(1+(hl_derate/100)):
            break

    # calculate total annual heat loss (needed for histogram plot)
    heatloss_annual = estimate_2021.heatloss.sum()

    # calculate design heat loss 
    heatloss_design = (m * dtemp) + b

    # create output variables for plotting
    x_plot = np.linspace(-30,balance_point,20)
    x_std = np.linspace(-15,balance_point,20)

    # calculate heatloss for 5-year period (2017-2021)
    weatherdata['heatloss'] = m * weatherdata.temperature + b

    # create dataframe for plotting heat load distribution histogram
    bin_midpoints = np.arange(-29.5,balance_point,1)
    hours = []
    load = []
    for mid_point in bin_midpoints:
        hour_count = 0
        load_sum = 0
        for temp,hl in zip(weatherdata['temperature'],weatherdata['heatloss']):
            if (temp >= (mid_point - 0.5)) & (temp < mid_point + 0.5):
                hour_count = hour_count + 1
                load_sum = load_sum + hl
        hour_count = hour_count/5 # average over 5 years
        load_sum = load_sum/5
        hours.append(hour_count)
        load.append(load_sum)
    hours_dict = {
        'temp':bin_midpoints,
        'hours': hours,
        'load':load}
    heatload_dist = pd.DataFrame(hours_dict)
    # calculate heat load required in GJ
    # convert load from kBTU to GJ using a factor of 0.001055
    heatload_dist['GJ'] = heatload_dist.load*0.001055

    return [m, b, dtemp, heatloss_design, m_hp_1, b_hp_1, m_hp_2, b_hp_2, m_hp_3, b_hp_3, x_plot, x_std, m_list, b_list, heatloss_annual, estimate_2021, heatload_dist, gasuse_annual, derate_c1, derate_c2, derate_c3, location_name, cop_df]