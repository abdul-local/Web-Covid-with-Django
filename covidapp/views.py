from django.shortcuts import render
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "ddc00265a0mshb036428894c0d1cp121079jsn6276303b6233",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

# Create your views here.
def hellowordview(request):
    noofresults=int(response['results'])
    mylist=[]
    for x in range(0,noofresults):
        mylist.append(response['response'][x]['country'])

    if request.method=='POST':
        selectcontry=request.POST['selectcontry']
        maximum=int(response['results'])
        for x in range(0,maximum):
            if selectcontry==response['response'][x]['country']:
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical= response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deaths=int(total)-int(active)-int(recovered)
                context={'selectcontry':selectcontry,'mylists':mylist,'new':new,'active':active, 'critical':critical, 'recovered':recovered,'deaths':deaths,'total':total}
                return render(request,'helloword.html',context)
    
    mylists={'mylists':mylist}
    return render(request,'helloword.html',mylists)

