from flask import Flask
from flask import Flask, request, render_template
import numpy as np
import matplotlib.pyplot as plt
import folium
from sklearn.tree import DecisionTreeRegressor
from joblib import load
import overpy
app = Flask(__name__)

# ar = []
mpans = 0

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/getprediction',methods=['POST'])
def getprediction():
    input = [float(x) for x in request.form.values()]
    final_input = [np.array(input)]
    # ar.append(final_input[0])
    # ar.append(final_input[1])
    mdl = load('pcmodel.joblib')
    prediction = mdl.predict(final_input)
    mpans = prediction
    # print(ar)

    return render_template('index.html', output='Predicted Magnitude :{}'.format(prediction))
# Create a Folium map centered at the specified coordinates
# Save the map as an HTML file
# map_filename = 'templates/map.html'
# my_map.save(map_filename)
# Create a Folium map centered at the specified coordinates
mpans = 2.61
# Save the map as an HTML file
# map_filename = 'templates/map.html'
# my_map.save(map_filename)
# Create a Folium map centered at the specified coordinates
@app.route('/getmap', methods=['POST'])
def getmap():
    # Get latitude and longitude from the form
    lati = float(request.form['latitude'])
    longi = float(request.form['longitude'])

    # Create a Folium map centered at the specified coordinates
    map_center = [lati, longi]
    ans = mpans
    my_map = folium.Map(location=map_center, zoom_start=5)

    # Add a marker at the specified coordinates
    folium.Marker(location=map_center, popup='Selected Location').add_to(my_map)

    # Save the map as an HTML file
    # map_filename = 'templates/map.html'
    # my_map.save(map_filename)

    return render_template('map.html', output='Predicted Magnitude :{}'.format(ans))

# m = folium.Map(location=(ar[0], ar[1]), tiles="cartodb positron")
# m.save("footprint.html")

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     # return 'Hello, Worlddd!'
#     mdl = load('pcmodel.joblib')
#     test_np_input = np.array([[33.19,	-115.57,	4.45,	3,	46.00,	0.04,	0.22,	0,	0.41,	0.16,	49.00,	1,	0,	3,	15,	1]])
#     pred = mdl.predict(test_np_input)
#     pred_str = str(pred)
#     return pred_str
#     # return test_np_input

# print(np.array([[12,34], [45,76]]))

# def floats_string_to_input_arr(floats_str):
#   floats = [float(x.strip()) for x in floats_str.split(',')]
#   as_np_arr = np.array(floats).reshape(len(floats), 1)
#   return as_np_arr

# floats_string_to_input_arr('33.19,	-115.57,	4.45,	3,	46.00,	0.04,	0.22,	0,	0.41,	0.16,	49.00,	1,	0,	3,	15,	1')