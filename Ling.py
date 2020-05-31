import numpy as np
from keras.preprocessing.sequence import pad_sequences

import pickle


tokenizer=pickle.load(open('tokenizer.pkl','rb+'))
from keras.models import load_model


model=load_model(open('model.h5','rb+'))


def inp(name):
  q=tokenizer.texts_to_sequences(name)
  q=[i[0] for i in q]
  q1=[]
  q1.append(q)
  s=pad_sequences(q1,maxlen=15,padding='post')
  return s


def decoder(ans):
    decode=np.argmax(ans,axis=1)[0]
    return decode



def gender(name):
    sequences=inp(name)
    predict=model.predict(sequences)
    result=decoder(predict)
    if result==1:
        print(name," is a male")
    if result==0:
        print(name," is a female")
    return result
    
