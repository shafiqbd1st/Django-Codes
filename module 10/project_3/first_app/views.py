from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d = {'name': 'shafiq islam', 'age': 21, 'birthday': datetime.datetime.now(), 'lst': ['my', 'name', 'shaifq'], 'courses': [
        {
            'id': 1,
            'name': 'python',
            'fee': 5000
        },
        {
            'id': 2,
            'name': 'django',
            'fee': 10000
        },
        {
            'id': 3,
            'name': 'c++',
            'fee': 20000
        }]
    }
    return render(request, 'home.html', d)