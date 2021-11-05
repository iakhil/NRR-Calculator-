import math 
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
class NRR:
    
    def __init__ (self, runs_scored, overs_faced, runs_given, overs_bowled): 
        self.runs_scored = runs_scored 
        self.overs_faced = overs_faced
        self.runs_given = runs_given 
        self.overs_bowled = overs_bowled





def convert(ele):
    overs = math.floor(ele)
    balls = round(ele - math.floor(ele), 1) * 10 
    conv = overs + (balls / 6) 
    return round(conv, 2)   



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/afghanistan')
def show_ques():
    
    return render_template('afg.html')

@app.route('/newzealand')
def show_nz():
    
    return render_template('nz.html')


@app.route('/india')
def show_ind():
    
    return render_template('ind.html')


@app.route('/southafrica')
def show_sa():

    return render_template('sa.html')


@app.route('/australia')
def show_aus():

    return render_template('aus.html')


@app.route('/afghanistan',methods=['POST'])
def afghanistan():
    ind = NRR([151, 110, 210], [20, 20, 20], [152, 111, 144], [17.83, 14.5, 20])
    afg = NRR([190, 147, 160, 144], [20, 20, 20, 20], [60, 148, 98, 210], [20, 19, 20, 20])
    nz = NRR([134, 111, 172], [20, 14.5, 20], [135, 110, 156], [18.67, 20, 20])

    input_data = [float(x) for x in request.form.values()]
    print(input_data)
    input_data[1] = convert(input_data[1])  
    afg.runs_scored.append(input_data[0])
    nz.runs_given.append(input_data[0])
    afg.overs_faced.append(input_data[1])
    nz.overs_bowled.append(input_data[1])
    nz.runs_scored.append(input_data[2])
    afg.runs_given.append(input_data[2])
    input_data[3] = convert(input_data[3])
    nz.overs_faced.append(input_data[3])
    afg.overs_bowled.append(input_data[3])
 
    # final_features = [np.array(int_features)]
    nz_for = sum(nz.runs_scored) / sum(nz.overs_faced)
    nz_aga = sum(nz.runs_given) / sum(nz.overs_bowled) 
    nz_nrr = nz_for - nz_aga 
    #print("India NRR: ",  nrr) 

    #print(afg_runs_scored[0:3])
    afg_for = sum(afg.runs_scored) / sum(afg.overs_faced) 

    afg_aga = sum(afg.runs_given) / sum(afg.overs_bowled)

    afg_nrr = afg_for - afg_aga

    print("Afghanistan NRR: ", afg_nrr) 
    return render_template('afg.html', nz_nrr=nz_nrr, afg_nrr=afg_nrr)
    #return render_template('index.html', afg_nrr='{}'.format(afg_nrr), ind_nrr='{}'.format(nrr))

@app.route('/newzealand',methods=['POST'])
def newzealand():
    ind = NRR([151, 110, 210], [20, 20, 20], [152, 111, 144], [17.83, 14.5, 20])
    afg = NRR([190, 147, 160, 144], [20, 20, 20, 20], [60, 148, 98, 210], [20, 19, 20, 20])
    nz = NRR([134, 111, 172, 163], [20, 14.5, 20, 20], [135, 110, 156, 111], [18.67, 20, 20, 20])
    input_data = [float(x) for x in request.form.values()]
    print(input_data)
    input_data[1] = convert(input_data[1])  
    nz.runs_scored.append(input_data[0])
    nz.overs_faced.append(input_data[1])
    nz.runs_given.append(input_data[2])
    input_data[3] = convert(input_data[3])
    nz.overs_bowled.append(input_data[3])
    


    nz_for = sum(nz.runs_scored) / sum(nz.overs_faced) 
    nz_aga = sum(nz.runs_given) / sum(nz.overs_bowled)

    nz_nrr = nz_for - nz_aga

    return render_template('nz.html', nz_nrr=nz_nrr)


@app.route('/india',methods=['POST'])
def india():
    ind = NRR([151, 110, 210, 89], [20, 20, 20, 6.3], [152, 111, 144, 85], [17.83, 14.5, 20, 20])
    afg = NRR([190, 147, 160, 144], [20, 20, 20, 20], [60, 148, 98, 210], [20, 19, 20, 20])
    nz = NRR([134, 111, 172], [20, 14.5, 20], [135, 110, 156], [18.67, 20, 20])
    
    input_data = [float(x) for x in request.form.values()]
    input_data[1] = convert(input_data[1])  
    ind.runs_scored.append(input_data[0])
    ind.overs_faced.append(input_data[1])
    ind.runs_given.append(input_data[2])
    input_data[3] = convert(input_data[3])
    ind.overs_bowled.append(input_data[3])
    
   

    ind_for = sum(ind.runs_scored) / sum(ind.overs_faced) 
    ind_aga = sum(ind.runs_given) / sum(ind.overs_bowled)

    ind_nrr = ind_for - ind_aga

    return render_template('ind.html', ind_nrr=ind_nrr)

@app.route('/southafrica',methods=['POST'])
def southafrica():
    ind = NRR([151, 110, 210, 89], [20, 20, 20, 6.3], [152, 111, 144, 85], [17.83, 14.5, 20, 20])
    afg = NRR([190, 147, 160, 144], [20, 20, 20, 20], [60, 148, 98, 210], [20, 19, 20, 20])
    
    sa = NRR([118, 144, 146, 86], [20, 18.33, 19.83, 13.5], [121, 143, 142, 84], [19.67, 20, 20, 20])
    nz = NRR([134, 111, 172], [20, 14.5, 20], [135, 110, 156], [18.67, 20, 20])
    input_data = [float(x) for x in request.form.values()]
    input_data[1] = convert(input_data[1])  
    sa.runs_scored.append(input_data[0])
    sa.overs_faced.append(input_data[1])
    sa.runs_given.append(input_data[2])
    input_data[3] = convert(input_data[3])
    sa.overs_bowled.append(input_data[3])

    sa_for = sum(sa.runs_scored) / sum(sa.overs_faced) 
    sa_aga = sum(sa.runs_given) / sum(sa.overs_bowled)

    sa_nrr = sa_for - sa_aga

    

    return render_template('sa.html', sa_nrr=sa_nrr)


@app.route('/australia',methods=['POST'])
def australia():
   
    aus = NRR([121, 155, 125, 78], [19.67, 17, 20, 6.34], [118, 154, 126, 73], [20, 20, 11.67, 20])
    input_data = [float(x) for x in request.form.values()]
    input_data[1] = convert(input_data[1])  
    aus.runs_scored.append(input_data[0])
    aus.overs_faced.append(input_data[1])
    aus.runs_given.append(input_data[2])
    input_data[3] = convert(input_data[3])
    aus.overs_bowled.append(input_data[3])

    aus_for = sum(aus.runs_scored) / sum(aus.overs_faced) 
    aus_aga = sum(aus.runs_given) / sum(aus.overs_bowled)

    aus_nrr = aus_for - aus_aga

    

    return render_template('aus.html', aus_nrr=aus_nrr)








if __name__ == "__main__":
    app.run(debug=False)