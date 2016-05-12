"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
import random

class Randword(Controller):
    def __init__(self, action):
        super(Randword, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('RandwordModel')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """
        if 'counter' not in session:
            session['counter'] = 0
        if "randItem" not in session:
            session['randItem'] = ""
        return self.load_view('index.html')

    def get_word(self):
        
        options = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
        randItem = ""
        for item in range(0,14):
            randNum = random.randint(0, len(options)-1)
            randItem += options[randNum]
        print randItem
        session['counter'] += 1
        session['randItem'] = randItem
        return redirect('/')

    def reset(self):
        session.clear()
        return redirect('/')



