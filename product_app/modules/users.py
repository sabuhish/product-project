from django.shortcuts import render,redirect

users = [
    {
        'ID' : 1,
        'Name' : 'Sebuhi',
        'Surname': 'Shukurov',
        'Age' : 27,
        'Username': 'Sebuhi',
        'Password': '12345'
    },
    {
        'ID' : 2,
        'Name' : 'Elshad',
        'Surname': 'Agayev',
        'Age' : 18,
        'Username': 'Elshad_A',
        'Password': '123'
    }
]

def get_user(username,password) :
    if not username.strip() or not password.strip():
        return False
    for i in users:
        if username == i['Username'] and password == i['Password']:
            return i['ID']
    else :
        return False
