from django.shortcuts import render
import csv
from pathlib import Path
# Create your views here.
def home():
    mylist = []
    #file_name = open(,"r")
    """path = Path('instances.csv')
    file_name = path.open(mode='rb')
    with open('instances.csv') as datas :
        data_row = csv.reader(datas, delimiter=',')
        next(data_row)
        for rows in data_row:
            mylist.append(rows)
        print(mylist)
    # return render(request, 'files/index.html')"""

home()