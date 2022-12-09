# import library
from bs4 import BeautifulSoup
import pandas as pd
import plotly_express as px
import plotly.graph_objects as go # for radar chart


############################ title container ###################
def title_name(title):
  t = f"""<div class="title_container">{title}</div>"""
  return(t)

############################ Result ###########################
def match_result(df):
  df_result = df[(df['team']=='Troyes')][['opponent','result']].reset_index()
  data = """<div class='card2'>
  <table id="myTable">
  <tr>
    <td>Win</td>
  </tr>
  <tr>
    <td>Draw</td>
  </tr>
  <tr>
    <td>Lose</td>
  </tr>

  </table>
          </div>
  """

  soup = BeautifulSoup(data, 'html.parser')

  new_soup = soup.find_all('tr')

  for i in new_soup:
    if i.find('td').text == 'Win':
      new_td = soup.new_tag('td')
      for j in df_result.index:
        if df_result.result[j] == 'W':
          new_span = soup.new_tag('span',attrs={'class':['result_icon','very_good']})
          new_td.append(new_span)
      i.append(new_td)

    if i.find('td').text == 'Draw':
      new_td = soup.new_tag('td')
      for j in df_result.index:
        if df_result.result[j] == 'D':
          new_span = soup.new_tag('span',attrs={'class':['result_icon','draw']})
          new_td.append(new_span)
      i.append(new_td)
    
    if i.find('td').text == 'Lose':
      new_td = soup.new_tag('td')
      for j in df_result.index:
        if df_result.result[j] == 'L':
          new_span = soup.new_tag('span',attrs={'class':['result_icon','very_poor']})
          new_td.append(new_span)
      i.append(new_td)

  return(soup)


############################# Ligue1 Table ##########################
def ligue1_table(df):
  df_table = df[['team','round','goals_for','goals_against','goals_diff','point']]
  df_table = df_table.groupby(['team']).agg({'round':'count','goals_for':'sum','goals_against':'sum','goals_diff':'sum','point':'sum'}).sort_values(['point','goals_diff'],ascending=[False,False]).reset_index()
  df_table['pos'] = [i+1 for i in df_table.index]
  df_table = df_table[['pos','team','round','goals_for','goals_against','goals_diff','point']]
    
  data = """<table class="styled-table">
      <thead>
          <tr>
              <th>pos</th>
              <th>Team</th>
              <th>MP</th>
              <th>GF</th>
              <th>GA</th>
              <th>GD</th>
              <th>Pts</th>
          </tr>
      </thead>
      <tbody>
      </tbody>
  </table>"""


  soup = BeautifulSoup(data, 'html.parser')
  


  for i in df_table.index:
      if df_table.team[i] == 'Troyes':
          new_tr = soup.new_tag('tr class="active-row"')
      else: 
          new_tr = soup.new_tag('tr')

      #Add as many td (data) you want.
      new_td = soup.new_tag('td')
      new_td1 = soup.new_tag('td')
      new_td2 = soup.new_tag('td')
      new_td3 = soup.new_tag('td')
      new_td4 = soup.new_tag('td')
      new_td5 = soup.new_tag('td')
      new_td6 = soup.new_tag('td')

      # data
      new_td.string = f"{df_table.pos[i]}"
      new_td1.string = f"{df_table.team[i]}"
      new_td2.string = f"{df_table['round'][i]}"
      new_td3.string = f"{df_table.goals_for[i]}"
      new_td4.string = f"{df_table.goals_against[i]}"
      new_td5.string = f"{df_table.goals_diff[i]}"
      new_td6.string = f"{df_table.point[i]}"

      new_tr.append(new_td)
      new_tr.append(new_td1)
      new_tr.append(new_td2)
      new_tr.append(new_td3)
      new_tr.append(new_td4)
      new_tr.append(new_td5)
      new_tr.append(new_td6)

      #Add whole 'tr'(row) to table.
      soup.tbody.append(new_tr)

  return str(soup)

########################## Radar Chart ############################



def radar_chart(df,option):
  df_radar = df[['team','possession','shots_on_target_pct','gk_save_pct','passes_pct','pressure_regain_pct']]
  df_radar = df_radar.groupby(['team']).mean().reset_index()

  r1 = df_radar.loc[df_radar['team']=='Troyes'].values.flatten().tolist()

  if option=='Ligue1':
    r2 = df_radar.describe().loc['mean'].to_list()
    r2.insert(0,'Ligue1')

  else:
    r2 = df_radar.loc[df_radar['team']==option].values.flatten().tolist()

  categories = ['Possesion','Shot on Target','Save',
                'Passes', 'Succesfull Pressure']

  fig = go.Figure()

  fig.add_trace(go.Scatterpolar(
      r=r1[1:],
      theta=categories,
      fill='toself',
      name=r1[0],
      fillcolor = '#0F3460',
      opacity = 0.5,
      line=dict(
          color='#0F3460'
      ),
      mode='markers+lines'

  ))

  fig.add_trace(go.Scatterpolar(
      r=r2[1:],
      theta=categories,
      fill='toself',
      name=r2[0],
      fillcolor = '#533483',
      opacity = 0.5,
      line=dict(
          color='#533483'
      ),
      mode='markers+lines'

  ))

  fig.update_layout(
  polar=dict(
      radialaxis=dict(
      visible=False,
      range=[0, max(max(r1[1:],r2[1:]))],
      
      )
      ,gridshape='linear'),

  showlegend=True,
  # width=1200, height=600,
  font=dict(size=18),
  legend=dict(orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1)

  )

  return fig

#################################### Cal card #########################
def cal_card(df,title,parameter,option):
  df_team = df.groupby(['team']).mean()

  list_low = ['goals_against','gk_shots_on_target_against','gk_psxg']

  value1 = df[
                (df['team']=='Troyes')
          ][parameter].mean()
  if option =='Ligue1':
    value2 = df[parameter].mean()

  else:
    value2 = df[
                (df['team']==option)
          ][parameter].mean()

  if parameter in list_low:
    if value1 > df_team[parameter].quantile(0.8):
      card_color = 'very_poor'
      tooltip = 'Performance is Very Poor'
    elif value1 > df_team[parameter].quantile(0.6):
      card_color = 'poor'
      tooltip = 'Performance is  Poor'
    elif value1 > df_team[parameter].quantile(0.4):
      card_color = 'draw'
      tooltip = 'Performance is Average'
    elif value1 > df_team[parameter].quantile(0.2):
      card_color = 'good'
      tooltip = 'Performance is Good'
    else:
      card_color = 'very_good'
      tooltip = 'Performance is Very Good'
  else:
    if value1 < df_team[parameter].quantile(0.2):
      card_color = 'very_poor'
      tooltip = 'Performance is Very Poor'
    elif value1 < df_team[parameter].quantile(0.4):
      card_color = 'poor'
      tooltip = 'Performance is  Poor'
    elif value1 < df_team[parameter].quantile(0.6):
      card_color = 'draw'
      tooltip = 'Performance is Average'
    elif value1 < df_team[parameter].quantile(0.8):
      card_color = 'good'
      tooltip = 'Performance is Good'
    else:
      card_color = 'very_good'
      tooltip = 'Performance is Very Good'

  t = f"""<div class='card'>
  <span class="tooltiptext">{tooltip}</span>
        <div class='container {card_color}'>{title}</div>
        <div class='container2'>
          <div class='row'>
            <div Class='column'> {round(value1,2)} </div>
            <div Class='column'>  {round(value2,2)} </div>
          </div>
            <div class='row' style='font-size :15px'>
            <div Class='column'> Troyes </div>
            <div Class='column'> {option} </div>
          </div>
        </div>
      </div>"""

  return(t)

#################################### Cal card pct#########################
def cal_card2(df,title,parameter,option):
  df_team = df.groupby(['team']).mean().reset_index()
  df_team['shots_on_target_pct'] = (df_team['shots_on_target']/df_team['shots_total'])*100

  list_low = ['goals_against']

  value1 = df_team[
                (df_team['team']=='Troyes')
          ][parameter].to_list()[0]
  if option =='Ligue1':
    value2 = df_team[parameter].mean()

  else:
    value2 = df_team[
                (df_team['team']==option)
          ][parameter].to_list()[0]

  if parameter in list_low:
    if value1 > df_team[parameter].quantile(0.8):
      card_color = 'very_poor'
      tooltip = 'Performance is Very Poor'
    elif value1 > df_team[parameter].quantile(0.6):
      card_color = 'poor'
      tooltip = 'Performance is  Poor'
    elif value1 > df_team[parameter].quantile(0.4):
      card_color = 'draw'
      tooltip = 'Performance is Average'
    elif value1 > df_team[parameter].quantile(0.2):
      card_color = 'good'
      tooltip = 'Performance is Good'
    else:
      card_color = 'very_good'
      tooltip = 'Performance is Very Good'
  else:
    if value1 < df_team[parameter].quantile(0.2):
      card_color = 'very_poor'
      tooltip = 'Performance is Very Poor'
    elif value1 < df_team[parameter].quantile(0.4):
      card_color = 'poor'
      tooltip = 'Performance is  Poor'
    elif value1 < df_team[parameter].quantile(0.6):
      card_color = 'draw'
      tooltip = 'Performance is Average'
    elif value1 < df_team[parameter].quantile(0.8):
      card_color = 'good'
      tooltip = 'Performance is Good'
    else:
      card_color = 'very_good'
      tooltip = 'Performance is Very Good'

  t = f"""<div class='card'>
  <span class="tooltiptext">{tooltip}</span>
        <div class='container {card_color}'>{title}</div>
        <div class='container2'>
          <div class='row'>
            <div Class='column'> {round(value1,2)} </div>
            <div Class='column'>  {round(value2,2)} </div>
          </div>
            <div class='row' style='font-size :15px'>
            <div Class='column'> Troyes </div>
            <div Class='column'> {option} </div>
          </div>
        </div>
      </div>"""

  return(t)

####################################### plot df trend #########################
# Df trend
def func_trend(df,param_title,parameter):
  df_trend = df[
      (df['team']=='Troyes')
  ][[parameter,'round']]

  df_trend['trend'] = df_trend[parameter].expanding().mean()
  df_trend = df_trend.iloc[-5:]

  fig = px.line(df_trend,
               x="round", 
               y="trend",
               labels={'round':'Matchweek','trend':'Trend Average'})

  fig.update_layout(title_text=param_title, title_x=0.5)
  return(fig)

################################################# plot goals vs xg ####################+
def funct_goals_xg(df):
  df_trend = df[
    (df['team']=='Troyes')
][['round','goals','xg','xg_net']]

  df_trend = df_trend.iloc[-5:]

  fig = px.line(df_trend, x="round", y=['goals','xg'],labels={'round':'Matchweek'},title='Last 5 Match Goals Vs Expected Goals')
  newnames = {'goals':'Goals','xg':'Expected Goals'}
  fig.for_each_trace(lambda trace: trace.update(name = newnames[trace.name]))

  fig.update_layout(title_x=0.5,hovermode="x" ,width=1000, height=500,)
  
  return(fig)





###################################### Insight : Point ###############################

def insight_point(df):
  current_matchweek = df['round'].unique()[-1:].item()
  df_team = df.groupby(['team']).mean().reset_index()
  value1 = df_team[
              (df_team['team']=='Troyes')
        ]['point'].to_list()[0]

  if value1 < df_team['point'].quantile(0.2):
    performance = 'Very Poor'
  elif value1 < df_team['point'].quantile(0.4):
    performance = ' Poor'
  elif value1 < df_team['point'].quantile(0.6):
    performance = 'Average'
  elif value1 < df_team['point'].quantile(0.8):
    performance = 'Good'
  else:
    performance = 'Very Good'
  insight = f"Team Performance Until {current_matchweek} is in {performance} form, Currently Troyes have \
              {(df[(df['team']=='Troyes') & (df['result']=='W')]['result'].count())/(df[(df['team']=='Troyes')]['result'].count())*100}% Win Rate "

  return insight