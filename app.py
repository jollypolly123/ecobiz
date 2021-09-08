from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)
# google_maps = googlemaps.Client(key=API_KEY)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # address = request.form['address']
        # try:
        #     pattern = re.compile("[0-9]+ ([a-zA-Z]+ )?([a-zA-Z]+ )?([a-zA-Z]+ )?([a-zA-Z]+ )?[a-zA-Z]+, ([a-zA-Z]+ )?"
        #                          "([a-zA-Z]+ )?([a-zA-Z]+ )?([a-zA-Z]+ )?[a-zA-Z]+, ([a-zA-Z]+ )?[a-zA-Z]+ [0-9]+, "
        #                          "([a-zA-Z]+ )?[a-zA-Z]+")
        #     geocode_result = google_maps.geocode(address)
        #     # print(geocode_result)
        #     geocode_input = geocode_result[0]['formatted_address']
        #     if re.search(pattern, geocode_input):
        #         return redirect(url_for('services', address=geocode_input))
        #     else:
        #         error_msg = "Please input a valid address. Example: 6392 Truckee Court, Newark, CA"
        # except:
        #     error_msg = "Please input an address. Example: 6392 Truckee Court, Newark, CA"
        # return render_template('index.html', error_msg=error_msg)
        return render_template('index.html')
    else:
        return render_template('index.html')
