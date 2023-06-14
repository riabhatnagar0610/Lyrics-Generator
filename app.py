from flask import Flask, render_template, request
# import joblib
import pickle
import tensorflow as tf
import numpy as np

app = Flask(__name__)
# model = joblib.load('lyrics-final.pkl')
model = tf.keras.models.load_model('model_lyrics.h5')

app.static_folder = 'static'

with open('mapping.pkl', 'rb') as fp:
    mapping = pickle.load(fp)

with open('reverse_mapping.pkl', 'rb') as fp:
    reverse_mapping = pickle.load(fp)

# @app.route('/')
# def test():
#    return render_template('test_flask.html')

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/generic')
def generic():
   return render_template('generic.html')

def Lyrics_Generator(starter,Ch_count=500): #,temperature=1.0):
    generated= ""
    starter = starter 
    global seed
    L_symb = 47
    
    seed=[mapping[char] for char in starter]
    generated += starter 
    # Generating new text of given length
    for i in range(Ch_count):

        seed=[mapping[char] for char in starter]
        x_pred = np.reshape(seed, (1, len(seed), 1))
        x_pred = x_pred/ float(L_symb)
        prediction = model.predict(x_pred, verbose=0)[0]  
        # Getting the index of the next most probable index
        prediction = np.asarray(prediction).astype('float64')
        prediction = np.log(prediction) / 1.0 
        exp_preds = np.exp(prediction)
        prediction = exp_preds / np.sum(exp_preds)
        probas = np.random.multinomial(1, prediction, 1)
        index = np.argmax(prediction)
        next_char = reverse_mapping[index]  
        # Generating new text
        generated += next_char
        starter = starter[1:] + next_char
       
    return generated

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      lyrics = str(request.form.get('text-enter'))
      prediction = Lyrics_Generator(lyrics)
      # prediction = "{:,}".format(prediction)
      return render_template('elements.html', prediction = prediction)

if __name__ == '__main__':
   app.run(debug = True)
