from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

texts=[
    "good product",
    "bad service",
    "excellent",
    "terrible",
    'good_service',
    'happy',
    'bad movie',
    'very bad'
]
labels=[1,0,1,0,1,1,0,0]

vectorizer=CountVectorizer()
x=vectorizer.fit_transform(texts)
model=LogisticRegression()
model.fit(x,labels)

def predict(text:str):
    x=vectorizer.transform([text])
    result=model.predict(x)[0]
    return "positive" if result==1 else "negative"