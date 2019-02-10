from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = { 'my_list':[
    {
    'resturant_name': 'Latavolla',
    'food_type':'Italian Food'
    },
    {
    'resturant_name': 'Simple But Dynamic',
    'food_type' :'Amrican Food'
    },
    {
    'resturant_name': 'Shormer',
    'food_type': 'Arbian Food'
    }
    ],

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = { 'my_object':{
    'resturant_name': 'Herfi',
    'food_type': 'Fast food'
    },

    }
    return render(request, 'detail.html', context)
