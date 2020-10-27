from flask import Flask
app = Flask(__name__)
# import the Flask library and set up our app variable so  
# we can start writting routes

@app.route('/') #indicates the (url)page well need to visit to see our result. here / is the homepage
def homepage(): #defines the route function. Whatever this function returns will show up in the browser (appropriate url)
    """Shows a greeting to the user.""" #optional dockstring - describes the route in a human language way
    return 'Are you there, world? It\'s me, Ducky!' #returns the page contents

@app.route('/penguins')
def animal():
    return "Penguins are cute!"
    #on local host remember to put/penguins after the 5000

# route variable
@app.route('/animal/<users_animal>')  #first line URL of page youll need to visit; <>denote the route variable= user can type anything at all. the value the user types into the url will be avail in a variable called users_animal
def favorite_animal(users_animal):#second is the function signature for the route function takes the variable users_animal
    return f'Wow, {users_animal} is my favorite animal too!' # uses the available users_animal to construct a response


@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def funny_story(adjective, noun):
    return f'The only thing he wanted was {adjective}ness and three {noun}s'

@app.route('/multiply/<number1>/<number2>')
def lets_multiply(number1, number2):
    mult=int((number1*number2))
    return 









if __name__=='__main__':
    app.run(debug=True) #tells python how to run the server
