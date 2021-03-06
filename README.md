# 👨Ling-Gender👩

## 📌 Introduction:-

A Natural Language Processing model trained with over 1,00,000 (1 Lakh) names is used to predict a gender of a person based on the first name of the person.This model is created using Long Short Term Memory(LSTM) a variant of Recurrent Nueral Network which has training accuracy of 99.35% and tested over 11,000 samples with a test accuracy of 89.08% which is quite high in nlp for out of sample test cases.


<p align="center">
  <a href="https://github.com/ksdkamesh99/Ling">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Combotrans.svg/1200px-Combotrans.svg.png" alt="Logo" width="300px" height="300px">
  </a>
</p>

## 🏃‍♂️ Local Installation
1. Drop a ⭐ on the Github Repository.  


2. Clone the Repo by going to your local Git Client and pushing in the command: 

```sh
https://github.com/ksdkamesh99/Ling.git
```

3. Install the Packages: 
```sh
pip install -r requirements.txt
```

4. At  last, Go to 3.7.7 Python interpreter(Make Sure to create virtual env).
```sh
#Import Ling as l in any python file/Interpreter(note it is present in the same directory)
import Ling as l
print(l.gender("kamesh"))
# Output will be 1 which means male
print(l.gender("sudha"))
#Output will be 0 which means female
```

5. Screenshots will be updated below.



## 📧Contact:-
For any kind of suggesstions/ help in package regarding improving accuracy of model. Please mail me at ksdkamesh99@gmail.com.


## 📜 LICENSE
[MIT](https://github.com/ksdkamesh99/Ling/blob/master/LICENSE)
