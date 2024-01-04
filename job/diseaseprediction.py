# Importing the necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk

# For loading dataset into a dataframe
df = pd.read_csv('C:\jupy\dise.csv')
# Extract features and target
X = df.drop('Disease', axis=1)
y = df['Disease']
# Split the data into training and testing sets using pandas bulit in function
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
X_train.columns = ['Fever','Chills','Cough','Sore Throat','Body Aches','Fatigue','Headache','Increased Thirst','Frequent Urination','Unexplained Weight Loss','Shortness of Breath','Loss of Taste/Smell','Joint Pain','Swelling','Stiffness','Chest Pain','Dizziness','Blurred Vision','Weight Loss' ]
X_test.columns = ['Fever','Chills','Cough','Sore Throat','Body Aches','Fatigue','Headache','Increased Thirst','Frequent Urination','Unexplained Weight Loss','Shortness of Breath','Loss of Taste/Smell','Joint Pain','Swelling','Stiffness','Chest Pain','Dizziness','Blurred Vision','Weight Loss' ]
# Create the model using built in function for random forest algorithm
rf = RandomForestClassifier(n_estimators=100)

# Training the model with training dataset
rf.fit(X_train, y_train)

# Create the prediction function
def predict():
    # Get the input values
    values = []
    for symptom in symptoms:
        try:
            values.append(float(inputs[symptom].get()))
        except ValueError:
            messagebox.showerror('Error', 'Please enter a number for ' + symptom)
            return
    
    # To make the prediction
    prediction = rf.predict([values])[0]
    
    # Display the result
    messagebox.showinfo('Result', 'There is a possibility that you may have following disease: {}'.format(prediction))
# Create the GUI window
root = tk.Tk()
root.title('Disease Prediction System')
root.geometry('400x300')
# Change the background color of the root window
root.configure(bg='lavender')

# Create canvas for scrollable content
canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
canvas.configure(bg='lavender')

# Add scrollbar
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Set scrollbar to control canvas scrolling
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Add frame to canvas to hold content
content_frame = tk.Frame(canvas, bg='lavender')
canvas.create_window((0, 0), window=content_frame, anchor="nw")
# Create the bold lavender colored label
label = tk.Label(root, text="Mini-project by Rakshanaa, Subashini, Thirumullai", font=("Arial Bold", 14), fg="#6a5acd")
label.pack()


# Create the input fields
symptoms = ['Fever','Chills','Cough','Sore Throat','Body Aches','Fatigue','Headache','Increased Thirst','Frequent Urination','Unexplained Weight Loss','Shortness of Breath','Loss of Taste/Smell','Joint Pain','Swelling','Stiffness','Chest Pain','Dizziness','Blurred Vision','Weight Loss' ]
inputs = {}
for i in range(len(symptoms)):
    tk.Label(content_frame, text=symptoms[i]).grid(row=i, column=0)
    inputs[symptoms[i]] = tk.StringVar()
    tk.Entry(content_frame, textvariable=inputs[symptoms[i]]).grid(row=i, column=1)
    

# Create the predict button
predict_button = tk.Button(root, text='Predict', command=predict)
predict_button.pack(side=tk.BOTTOM, pady=10)

root.mainloop()