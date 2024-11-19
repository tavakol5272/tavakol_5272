from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
author = 'Nafiseh Tavakol in group 2'
doc = 'goal: life satisfiction'

class Constants(BaseConstants):
    name_in_url = 'survey-example-group2'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    #we will only come to the group class when we look at advanced methods
    pass


class Player(BasePlayer):
    #this is the most important feature of this file. We can collect all the variables used on the html pages here
    
#The Variables are structured on the base of pages
    permission = models.StringField(label="if you are sure that you want to participate in this survey please type: OK ",blank=True,)
    Gender = models.StringField(label="1- What is your gender? ",
        choices=["Male", "Female", "Non-binary", "prefer not to say "],
        widget=widgets.RadioSelect,)
    
    Age = models.IntegerField(label="2- How old are you? ", max=110, min=1, )  

    Academic_status = models.StringField(label="3- What is your level of education? ",
        choices=["Undergraduate","Diploma","Bachelor", "Master", "PHD", "Other"]
        , widget=widgets.RadioSelect,)
    
    Marital_status =   models.StringField(label="4- What is your Marital Status? ",
        choices=["Married", "Single", "Have partner", "prefer not to say"]
        , widget=widgets.RadioSelect,)
    
    Monthly_income = models.IntegerField(label="5- What is your net monthly income(Euro)? ", max=20000, min=1, )
    
    life_satisfaction_score= models.IntegerField(label="6- How satisfied are you with your overall life?(1-100)? <br>", max=100, min=1, )
    
    Idea = models.StringField(label="7- What is your idea about this survey? ",blank=True,)
    

    
                        
