# import library
import pandas as pd
import plotly_express as px
import plotly.graph_objects as go # for radar chart


############################ def card ###############################
def card(df_player,param,param_title,player_name):

    value = df_player[df_player['player']==player_name][param].item()

    t = f"""<div class='card'>
        <div class='container normal_color' style='font-size :20px'>{param_title}</div>
        <div class='container2' style='border-bottom-left-radius: 5px;border-bottom-right-radius: 5px;'>
        <div class='row' style='font-size :30px'>
            <div Class='column'> {value} </div>
        </div>
        </div>
        </div>"""

    return(t)

############################ Shooting, SCA GCA ######################
def pos_player(df_player,pos):
    pos_player_df = df_player[
    (df_player['position']==pos) |
    (df_player['position1']==pos)]

    pos_player_df2 = pos_player_df[
    (pos_player_df['team']=='Troyes')
    ]['player']

    return pos_player_df2

def shooting_sca_gca(df_player,pos,player_name):
    dict_goals_sca_gca = {
        'sca':'Shoot-Creation Action',
        'gca':'Goal-Creation Action',
        'assists':'Assists',
        'xg_net':'Goal Minus Expected Goals',
        'xg':'Expected Goals',
        'shots_on_target':'Shots On Target',
        'shots_total':'Shooting'
        }
    x = []
    y = []
    for i in dict_goals_sca_gca:
        list_forward_player_all = df_player[(df_player['position']==pos) | (df_player['position1']==pos)][['player',i]]
        list_forward_player_all['rank'] = round(list_forward_player_all[i].rank(pct=True)*100)
        x.append(list_forward_player_all[list_forward_player_all['player']==player_name]['rank'].item())
        y.append(dict_goals_sca_gca[i])
       
    colors = []
    for i in x:
        if i < 20:
            colors.append('rgb(233, 22, 40)')
        elif i < 40:
            colors.append('rgb(255, 140, 46)')
        elif i < 60:
            colors.append('rgb(134, 134, 134)')
        elif i < 80:
            colors.append('rgb(91, 235, 103)')
        else:
            colors.append('rgb(0, 105, 47)')

    fig = go.Figure(go.Bar(
                x=x,
                y=y,
                orientation='h',
                marker_color=colors,
                width=0.9,
                ))
    fig.update(layout_xaxis_range = [0,100])
    fig.update_layout(font_size=17,xaxis_visible=False,height=470,title='Shooting, Goal And Shot Creation')
    fig.layout.xaxis.fixedrange = True
    fig.layout.yaxis.fixedrange = True
    return fig           

def passing_and_possesion(df_player,pos,player_name):
    dict_goals_sca_gca = {
        'dribbles_completed_pct':'Dribbles Completed',
        'progressive_passes':'Progressive Passes',
        'assisted_shots':'Assisted Shots',
        'passes_pct':'Passes Completion'

        }

    x = []
    y = []
    for i in dict_goals_sca_gca:
        list_forward_player_all = df_player[(df_player['position']==pos) | (df_player['position1']==pos)][['player',i]]
        list_forward_player_all['rank'] = round(list_forward_player_all[i].rank(pct=True)*100)
        x.append(list_forward_player_all[list_forward_player_all['player']==player_name]['rank'].item())
        y.append(dict_goals_sca_gca[i])
       
    colors = []
    for i in x:
        if i < 20:
            colors.append('rgb(233, 22, 40)')
        elif i < 40:
            colors.append('rgb(255, 140, 46)')
        elif i < 60:
            colors.append('rgb(134, 134, 134)')
        elif i < 80:
            colors.append('rgb(91, 235, 103)')
        else:
            colors.append('rgb(0, 105, 47)')

    fig = go.Figure(go.Bar(
                x=x,
                y=y,
                orientation='h',
                marker_color=colors,
                width=0.9,
                ))
    fig.update(layout_xaxis_range = [0,100])
    fig.update_layout(font_size=17,xaxis_visible=False,height=350,title='Passing & Possesion')
    fig.layout.xaxis.fixedrange = True
    fig.layout.yaxis.fixedrange = True
    return fig      

def defense(df_player,pos,player_name):
    dict_goals_sca_gca = {
        'clearances':'Clearances',
        'interceptions':'Interceptions',
        'blocks':'Blocks',
        'pressure_regain_pct':'Pressure Regain',
        'pressures':'Pressures',
        'dribble_tackles_pct':'Tackles VS Dribbles Won',
        'tackles_won':'Tackles Won',
        'tackles':'Tackles'
        }

    x = []
    y = []
    for i in dict_goals_sca_gca:
        list_forward_player_all = df_player[(df_player['position']==pos) | (df_player['position1']==pos)][['player',i]]
        list_forward_player_all['rank'] = round(list_forward_player_all[i].rank(pct=True)*100)
        x.append(list_forward_player_all[list_forward_player_all['player']==player_name]['rank'].item())
        y.append(dict_goals_sca_gca[i])
       
    colors = []
    for i in x:
        if i < 20:
            colors.append('rgb(233, 22, 40)')
        elif i < 40:
            colors.append('rgb(255, 140, 46)')
        elif i < 60:
            colors.append('rgb(134, 134, 134)')
        elif i < 80:
            colors.append('rgb(91, 235, 103)')
        else:
            colors.append('rgb(0, 105, 47)')

    fig = go.Figure(go.Bar(
                x=x,
                y=y,
                orientation='h',
                marker_color=colors,
                width=0.9,
                ))
    fig.update(layout_xaxis_range = [0,100])
    fig.update_layout(font_size=17,xaxis_visible=False,height=500,title='Defense')
    fig.layout.xaxis.fixedrange = True
    fig.layout.yaxis.fixedrange = True
    return fig         


def goalkeeping(df_goalkeeper,pos,player_name):
    dict_goals_sca_gca = {
        'gk_def_actions_outside_pen_area':'Defense Outside Pen. Area',
        'gk_crosses_stopped_pct':'Crosses Stopped',
        'gk_clean_sheets_pct':'Cleansheet',
        'gk_pens_save_pct':'Penalti Save',
        'gk_save_pct':'Save'
        }

    x = []
    y = []
    for i in dict_goals_sca_gca:
        list_forward_player_all = df_goalkeeper[['player',i]]
        list_forward_player_all['rank'] = round(list_forward_player_all[i].rank(pct=True)*100)
        x.append(list_forward_player_all[list_forward_player_all['player']==player_name]['rank'].item())
        y.append(dict_goals_sca_gca[i])
       
    colors = []
    for i in x:
        if i < 20:
            colors.append('rgb(233, 22, 40)')
        elif i < 40:
            colors.append('rgb(255, 140, 46)')
        elif i < 60:
            colors.append('rgb(134, 134, 134)')
        elif i < 80:
            colors.append('rgb(91, 235, 103)')
        else:
            colors.append('rgb(0, 105, 47)')

    fig = go.Figure(go.Bar(
                x=x,
                y=y,
                orientation='h',
                marker_color=colors,
                width=0.9,
                ))
    fig.update(layout_xaxis_range = [0,100])
    fig.update_layout(font_size=17,xaxis_visible=False,height=390,title='Goalkeeper')
    fig.layout.xaxis.fixedrange = True
    fig.layout.yaxis.fixedrange = True
    return fig         