import random
import streamlit as st
import requests


st.set_page_config(
    page_title="Airline Passenger Satisfaction",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/sonnyrd',
        'Report a bug': "https://github.com/sonnyrd",
        'About': "# Airline Passenger Satisfication"
    }
)


st.write("<h1 style='text-align: center; '>Airline Passenger Satisfaction</h1>", unsafe_allow_html=True)

st.image('https://previews.123rf.com/images/qualitdesign/qualitdesign1909/qualitdesign190900017/130031429-retraso-de-vuelo-o-concepto-de-cancelaci%C3%B3n-ilustraci%C3%B3n-de-dibujos-animados-plano-de-vector-pasajeros.jpg'
,use_column_width=True)

a = st.button("Generate inf data")
if a == True:
    st.write('press "reset" if you want to input manual')

if st.button('reset'):
    a == False
    st.write('Now you can input manual')


st.write(f"<h2 style='text-align: left; '>Customer Profile</h2>", unsafe_allow_html=True)
with st.container():
    col1, col2, = st.columns(2)
    with col1:
        # customer_type = st.selectbox('Customer Type',['Loyal Customer', 'disloyal Customer'])
        if a == True:
            list1 = ['Loyal Customer','disloyal Customer']
            customer_type = st.selectbox('Customer Type',[random.choice(list1)])
        else:
            customer_type = st.selectbox('Customer Type',['Loyal Customer', 'disloyal Customer'])

    with col2:
        # age = st.number_input('Age',value=30,min_value=0,max_value=100)
        if a == True:
            age = st.number_input('Age',random.randint(1,85))
        else:
            age = st.number_input('Age',value=30,min_value=0,max_value=85)

    
      
with st.container():
    col1, col2, = st.columns(2)
    with col1:
        # type_of_travel = st.selectbox('Type of Travel',['Personal Travel', 'Business travel'])
        if a == True:
            list2 = ['Personal Travel', 'Business travel']
            type_of_travel = st.selectbox('Type of Travel',[random.choice(list2)])
        else:
            type_of_travel = st.selectbox('Type of Travel',['Personal Travel', 'Business travel'])

    with col2:
        # flight_class = st.selectbox('Class',['Eco Plus', 'Business', 'Eco'])
        if a == True:
            list3 = ['Eco Plus', 'Business', 'Eco']
            flight_class = st.selectbox('Class',[random.choice(list3)])
        else:
            flight_class = st.selectbox('Class',['Eco Plus', 'Business', 'Eco'])

if a == True:
    flight_distance = st.slider('Flight Distance',30,5000,random.randint(30,5000))
else:
    flight_distance = st.slider('Flight Distance',30,5000,100)


with st.expander("Rating Information"):
            st.write('0 : Not Applicable \n 1 - 5 : bad to good')

st.write(f"<h2 style='text-align: left; '>Pre-Flight Services</h2>", unsafe_allow_html=True)


with st.container():
    col1, col2, = st.columns(2)
    with col1:
        # checkin_service = st.slider('Checkin service',0,5,3)
        if a == True:
            checkin_service = st.slider('Checkin service',0,5,random.randint(0,5))
        else:
            checkin_service = st.slider('Checkin service',0,5,3) 

    with col2:
        # ease_of_online_booking = st.slider('Ease of Online booking',0,5,3)
        if a == True:
            ease_of_online_booking = st.slider('Ease of Online booking',0,5,random.randint(0,5))
        else:
            ease_of_online_booking = st.slider('Ease of Online booking',0,5,3)

with st.container():
    col1, col2, = st.columns(2)
    with col1:
        # gate_location = st.slider('Gate location',0,5,3)
        if a == True:
            gate_location = st.slider('Gate location',0,5,random.randint(0,5))
        else:
            gate_location = st.slider('Gate location',0,5,3)

    with col2:
        # online_boarding = st.slider ('Online boarding',0,5,3)
        if a == True:
            online_boarding = st.slider ('Online boarding',0,5,random.randint(0,5))
        else:
            online_boarding = st.slider ('Online boarding',0,5,3)

with st.container():
    col1, col2, = st.columns(2)
    with col1:
        # departure_arrival_time_convenient = st.slider('Departure/Arrival time convenient',0,5,3)
        if a == True:
            departure_arrival_time_convenient = st.slider('Departure/Arrival time convenient',0,5,random.randint(0,5))
        else:
            departure_arrival_time_convenient = st.slider('Departure/Arrival time convenient',0,5,3)

    with col2:
        # baggage_handling = st.slider('Baggage handling',0,5,3)
        if a == True:
            baggage_handling = st.slider('Baggage handling',1,5,random.randint(1,5))
        else:
            baggage_handling = st.slider('Baggage handling',1,5,3) 



st.write(f"<h2 style='text-align: left; '>Flight Services</h2>", unsafe_allow_html=True)


with st.container():
    col1, col2, = st.columns(2)
    with col1:
        # seat_comfort = st.slider('Seat comfort',0,5,3)
        if a == True:
            seat_comfort = st.slider('Seat comfort',0,5,random.randint(0,5))
        else:
            seat_comfort = st.slider('Seat comfort',0,5,3)

    with col2:
        # leg_room_service = st.slider('Leg room service',0,5,3)
        if a == True:
            leg_room_service = st.slider('Leg room service',0,5,random.randint(0,5))
        else:
            leg_room_service = st.slider('Leg room service',0,5,3)   



with st.container():
    col1, col2, = st.columns(2)
    with col1:
        # onboard_service = st.slider('On-board service',0,5,3)
        if a == True:
            onboard_service = st.slider('On-board service',0,5,random.randint(0,5))
        else:
            onboard_service = st.slider('On-board service',0,5,3)

    with col2:
        # inflight_service = st.slider('Inflight service',0,5,3)
        if a == True:
            inflight_service = st.slider('Inflight service',0,5,random.randint(0,5))
        else:
            inflight_service = st.slider('Inflight service',0,5,3)

with st.container():
    col1, col2, = st.columns(2)
    with col1:
        # inflight_entertainment = st.slider('Inflight entertainment',0,5,3)
        if a == True:
            inflight_entertainment = st.slider('Inflight entertainment',0,5,random.randint(0,5))
        else:
            inflight_entertainment = st.slider('Inflight entertainment',0,5,3)

    with col2:
        # inflight_wifi_service = st.slider('Inflight wifi service',0,5,3)
        if a == True:
            inflight_wifi_service = st.slider('Inflight wifi service',0,5,random.randint(0,5))
        else:
            inflight_wifi_service = st.slider('Inflight wifi service',0,5,3)

with st.container():
    col1, col2, = st.columns(2)
    with col1:
        # cleanliness = st.slider('Cleanliness',0,5,3)
        if a == True:
            cleanliness = st.slider('Cleanliness',0,5,random.randint(0,5))
        else:
            cleanliness = st.slider('Cleanliness',0,5,3)

    with col2:
        # food_and_drink = st.slider('Food and drink',0,5,3)
        if a == True:
            food_and_drink = st.slider('Food and drink',0,5,random.randint(0,5))
        else:
            food_and_drink = st.slider('Food and drink',0,5,3)

# inference
data = {
 'Customer Type': customer_type,
 'Age' : age,
 'Type of Travel' : type_of_travel,
 'Class' : flight_class,
 'Flight Distance': flight_distance,
 'Inflight wifi service' : inflight_wifi_service,
 'Departure/Arrival time convenient' : departure_arrival_time_convenient,
 'Ease of Online booking': ease_of_online_booking,
 'Gate location' : gate_location,
 'Food and drink': food_and_drink,
 'Online boarding': online_boarding,
 'Seat comfort':seat_comfort,
 'Inflight entertainment':inflight_entertainment,
 'On-board service':onboard_service,
 'Leg room service':leg_room_service,
 'Baggage handling':baggage_handling,
 'Checkin service':checkin_service,
 'Inflight service':inflight_service,
 'Cleanliness':cleanliness,
 }

URL = "https://p1ml2-backend-sonnyrd.herokuapp.com/predict"

# komunikasi
r = requests.post(URL, json=data)
res = r.json()
if res['code'] == 200:
    st.write(f"<h2 style='text-align: center; '>Prediction Result </h2>", unsafe_allow_html=True)
    st.write(f"<h1 style='text-align: center; '>{res['result']['description']}</h1>", unsafe_allow_html=True)
   
else:
    st.write("Mohon maaf terjadi kesalahan")
    st.write(f"keterangan : {res['result']['error_msg']}")



