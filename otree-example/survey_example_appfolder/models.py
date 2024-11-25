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
import random
from survey_example_appfolder.HelperFunctions import random_number

author = 'Nafiseh Tavakol in group 2'
doc = 'Goal: life satisfaction survey'

class Constants(BaseConstants):
    name_in_url = 'survey-example-group2'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.group_assignment = random.choice(['pic-yes', 'pic-no'])
            if p.group_assignment == 'pic-yes':
                p.popout_yes = "Excellent. What is the most important factor affecting your life satisfaction?"
            else:
                p.popout_no = "Sorry to hear that. What is the most important factor affecting your life dissatisfaction?"

class Group(BaseGroup):
    counter = models.IntegerField(initial=0)
    life_satis_group = models.StringField(choices=['satisfied', 'dissatisfied'])
    
    def assign_satisfaction_group(self, player, pic):
        if pic == "pic-yes":
            self.life_satis_group = "satisfied"
        else:
            self.life_satis_group = "dissatisfied"
        player.group_assignment = self.life_satis_group
        return f"Player assigned to {self.life_satis_group} group."
    

class Player(BasePlayer):
<<<<<<< HEAD
    # Welcome
    device_type = models.StringField()
    operating_system = models.StringField()
    screen_height = models.IntegerField(initial=0)
    screen_width = models.IntegerField(initial=0)
    permission = models.StringField(
        label="If you are sure that you want to participate in this survey, please type: OK",
    )

    # Demo page
    Gender = models.StringField(
        label="1- What is your gender?",
        choices=["Male", "Female", "Non-binary", "Prefer not to say"],
        widget=widgets.RadioSelect,
    )
    Age = models.IntegerField(label="2- How old are you?", max=110, min=1)
    Academic_status = models.StringField(
        label="3- What is your level of education?",
        choices=["Undergraduate", "Diploma", "Bachelor", "Master", "PhD", "Other"],
        widget=widgets.RadioSelect,
    )
    Marital_status = models.StringField(
        label="4- What is your marital status?",
        choices=["Married", "Single", "Have partner", "Prefer not to say"],
        widget=widgets.RadioSelect,
    )
    Monthly_income = models.IntegerField(
        label="5- What is your net monthly income (Euro)?", max=20000, min=1
    )
    life_satisfaction_score = models.IntegerField(
        label="6- How would you rate your level of satisfaction with your life (1-100)?",
        max=100,
        min=1,
    )

    hidden_input = models.IntegerField(initial=50, blank=True)

    # Popout Page
    pic = models.StringField(
        label="7- Life satisfaction - please select one picture.",
        choices=["pic-yes", "pic-no"],
        widget=widgets.RadioSelect,
    )
    popout_yes = models.StringField(blank=True)
    popout_no = models.StringField(blank=True)
    time_popout = models.StringField(initial='-999')

    # End Page
    group_assignment = models.StringField()
=======
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
    

    
                        
>>>>>>> d29909c232463cb393f70c63ba4de0b5edfa5f54
