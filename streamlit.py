import pickle
import streamlit as st 


with open('saved.pkl','rb') as f:
  saved=pickle.load(f)

model=saved['model']
weather_encoder=saved['weather_freq']
road_encoder=saved['road_traffic_density']
type_of_order_encoder=saved['type_of_order_encoder']
type_of_vehicle_encoder=saved['type_of_vehicle_encoder']
festival_encoder=saved['festival_encoder']
city_encoder=saved['city_encoder']


st.title('how long will it take for an order to be delivered?')
st.write('fill in the below boxes')

age=st.slider(' the delivery person age',min_value=15,max_value=50)
ratings=st.slider(' the avegrage rating of the delivery person',min_value=1.0, max_value=6.0)
weather=[' Sunny', ' Stormy', ' Sandstorms', ' Cloudy', ' Fog', ' Windy',
       'unknown']
select_weather=st.selectbox(' whats the weather?',weather)
road_traffic=['High ', 'Jam ', 'Low ', 'Medium ', 'unknown']
select_roadtraffic=st.selectbox(' what is the weather?',road_traffic)
st.slider(' what is the condition of the vehicle',min_value=0, max_value=3)
type_of_order=['Snack ', 'Drinks ', 'Buffet ', 'Meal ']
select_order=st.selectbox('what is the order?',type_of_order)
type_of_vehicle=['motorcycle ', 'scooter ', 'electric_scooter ', 'bicycle ']
select_vehicle=st.selectbox('what vehicle does the delivery person use?',type_of_vehicle)
how_many_deliveries=st.slider('how many deliveries?',min_value=0,max_value=1)
festival=['No ', 'Yes ', 'unknown']
select_festival=st.selectbox('was there a festival?',festival)
city=['Urban ', 'Metropolitian ', 'Semi-Urban ', 'unknown']
select_city=st.selectbox('waht type of city are you in?',city)


ok=st.button('predict')
if ok:
  input_df=pd.DataFrame({
    'Delivery_person_Age':[age],
     'Delivery_person_Ratings'[ratings],
       'Road_traffic_density'[traffic], 
       'Vehicle_condition'[condition],
        'multiple_deliveries'[number of deliveries],
       'Festival'[festival], 
       'City'[city]

  })
  weather_encoded=weather_encoder.transform(select_weather)
  road_encoded=road_encoder.transform(select_roadtraffic)
  order_encoded=type_of_order_encoder.transform(select_order)
  vehicle_encoded=type_of_vehicle_encoder.transform(select_vehicle)
  festival_encoded=festival_encoder.transform(select_festival)
  city_encoded=city_encoder.transform(select_city)

  features=pd.concat(age,ratings,roadtraffic,how_many_deliveries,weather_encoded,order_encoded,vehicle_encoded,festival_encoded,city_encoded)
  scaled=scaler.transform(features)

  prediction = model.predict(scaled)
  st.success(f"Predicted result: {prediction[0]}")

st.show()