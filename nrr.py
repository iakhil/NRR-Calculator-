import math 
from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

runs_scored = [151, 110]
runs_given = [152, 111]
overs_played = [20, 20]
overs_bowled = [17.83, 14.5]


afg_runs_scored = [190, 147, 160]
afg_runs_given = [60, 148, 98] 
afg_overs_bowled = [20, 19, 20]
afg_overs_played = [20, 20, 20]

def convert(ele):
    overs = math.floor(ele)
    balls = round(ele - math.floor(ele), 1) * 10 
    conv = overs + (balls / 6) 
    return round(conv, 2)   


@app.route('/')
def home():

    return render_template('index.html')

@app.route('/afg')
def show_ques():
    
    return render_template('index.html')


@app.route('/afg',methods=['POST'])
def show_nrr():
    '''
    For rendering results on HTML GUI
    '''
    input_data = [x for x in request.form.values()]
    input_data[1] = convert(input_data[1])  
    afg_runs_scored.append(input_data[0])
    runs_given.append(input_data[0])
    afg_overs_played.append(input_data[1])
    overs_bowled.append(input_data[1])
    runs_scored.append(input_data[2])
    afg_runs_given.append(input_data[2])
    input_data[3] = convert(input_data[3])
    overs_played.append(input_data[3])
    overs_bowled.append(input_data[3])
 
    # final_features = [np.array(int_features)]
    nrr_for = sum(runs_scored) / sum(overs_played)
    nrr_aga = sum(runs_given) / sum(overs_bowled) 
    nrr = nrr_for - nrr_aga 
    #print("India NRR: ",  nrr) 

    #print(afg_runs_scored[0:3])
    afg_nrr_for = sum(afg_runs_scored) / sum(afg_overs_played) 

    afg_nrr_aga = sum(afg_runs_given) / sum(afg_overs_bowled)

    afg_nrr = afg_nrr_for - afg_nrr_aga

    #print("Afghanistan NRR: ", afg_nrr) 

    return render_template('index.html', afg_nrr='{}'.format(afg_nrr), ind_nrr='{}'.format(nrr))


if __name__ == "__main__":
    app.run(debug=False)