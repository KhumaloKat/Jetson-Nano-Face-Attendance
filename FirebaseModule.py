from firebase import firebase
import datetime

fb = firebase.FirebaseApplication('Use your own database link ',None)


def postData(name, time):
    
    data = {
        'Name': name,
        'Time': time
    }

    dateToday = datetime.date.today().strftime('%Y-%m-%d')
    fb.post(f'/{dateToday}',data)

if __name__ == "__main__":
    postData('Kat', '30')
