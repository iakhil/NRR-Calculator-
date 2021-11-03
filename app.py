import math 
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)


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


@app.route('/nz',methods=['POST'])
def nz():
        
    runs_scored = [134, 111, 172]
    runs_given = [135, 110, 156]
    overs_played = [20, 14.6, 20]
    overs_bowled = [18.67, 20, 20]


    afg_runs_scored = [190, 147, 160, 144]
    afg_runs_given = [60, 148, 98, 210] 
    afg_overs_bowled = [20, 19, 20, 20]
    afg_overs_played = [20, 20, 20, 20]
    cur_a_nrr = (sum(afg_runs_scored) / sum(afg_overs_played)) - (sum(afg_runs_given) / sum(afg_overs_bowled))
    print("Afg NRR: ", cur_a_nrr)
    input_data = [float(x) for x in request.form.values()]
    print(input_data)
    input_data[1] = convert(input_data[1])  
    afg_runs_scored.append(input_data[0])
    runs_given.append(input_data[0])
    afg_overs_played.append(input_data[1])
    overs_bowled.append(input_data[1])
    runs_scored.append(input_data[2])
    afg_runs_given.append(input_data[2])
    input_data[3] = convert(input_data[3])
    overs_played.append(input_data[3])
    afg_overs_bowled.append(input_data[3])
 
    # final_features = [np.array(int_features)]
    nrr_for = sum(runs_scored) / sum(overs_played)
    nrr_aga = sum(runs_given) / sum(overs_bowled) 
    nrr = nrr_for - nrr_aga 
    #print("India NRR: ",  nrr) 

    #print(afg_runs_scored[0:3])
    afg_nrr_for = sum(afg_runs_scored) / sum(afg_overs_played) 

    afg_nrr_aga = sum(afg_runs_given) / sum(afg_overs_bowled)

    afg_nrr = afg_nrr_for - afg_nrr_aga

    print("Afghanistan NRR: ", afg_nrr) 
    return render_template('index.html', ind_nrr=nrr)
    #return render_template('index.html', afg_nrr='{}'.format(afg_nrr), ind_nrr='{}'.format(nrr))

    
if __name__ == "__main__":
    app.run(debug=False)