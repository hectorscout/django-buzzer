from django.template import Context, loader
from django.http import HttpResponse

## -------------Game Host Views------------
def trebek(request):
    
    return HttpResponse("Suck it, Trebek")
    #template = loader.get_template('trebek.html')
    #return HttpResponse(template.render())

## -------------Board Views------------
def board(request):
    return HttpResponse("Hector Scout, come on down!")

## -------------Player Views------------
# return the registration page
def player(request):
    return HttpResponse("All your base are belong to us")

# post your player name to register for the game
def register(request):
    # add the person to the list of players
    return HttpResponse("All your base are belong to us")

# buzz in with your player name
def buzz(request):
    # register a buzz
    return HttpResponse("All your base are belong to us")
