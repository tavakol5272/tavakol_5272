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
        # Initialize gender quotas and counts
        self.session.vars['gender_quota'] = {'Male': 2, 'Female': 2, 'Other': 1}
        self.session.vars['gender_counts'] = {'Male': 0, 'Female': 0, 'Other': 0}

        # Iterate over players and assign groups
        for p in self.get_players():
           
    # Check the participant's selected picture
            if p.pic == 'pic-yes':
                p.group_assignment = 'pic-yes'
                p.popout_yes = "Excellent. What is the most important factor affecting your life satisfaction?"
            elif p.pic == 'pic-no':
                p.group_assignment = 'pic-no'
                p.popout_no = "Sorry to hear that. What is the most important factor affecting your life dissatisfaction?"
        for p in self.get_players():
             p.group_assignment = ''  # Initialize with an empty string


class Group(BaseGroup):
    counter = models.IntegerField(initial=0)
    life_satis_group = models.StringField(choices=['satisfied', 'dissatisfied'])
    
    def assign_satisfaction_group(self, player, pic):
        if pic == "pic-yes":
            self.life_satis_group = 'satisfied'
        else:
            self.life_satis_group = 'dissatisfied'
        player.group_assignment = self.life_satis_group
        return f"Player assigned to {self.life_satis_group} group."
    

class Player(BasePlayer):
    
    #variables on the HelperFunctions.py
    screenout = models.BooleanField(initial=0,blank=True)
    quota = models.BooleanField(initial=0,blank=True)
    redirect_url = models.StringField(blank=True)

    # Welcome
    device_type = models.StringField(blank=True)
    operating_system = models.StringField(blank=True)
    screen_height = models.IntegerField(initial=0,blank=True)
    screen_width = models.IntegerField(initial=0,blank=True)
    permission = models.StringField(
        label="If you are sure that you want to participate in this survey, please type: OK", blank=True,
    )
    eligible_question = models.IntegerField(blank=True)

    # Demo page
    gender = models.StringField(
        label="1- What is your gender?",
        choices=["Male", "Female", "Other"],
        widget=widgets.RadioSelect, blank=True,
    )
    age = models.IntegerField(label="2- How old are you?", max=110, min=1,blank=True,)
    
    
    Academic_status = models.StringField(
        label="3- What is your level of education?",
        choices=["Undergraduate", "Diploma", "Bachelor", "Master", "PhD", "Other"],
        widget=widgets.RadioSelect,blank=True,
    )
    Marital_status = models.StringField(
        label="4- What is your marital status?",
        choices=["Married", "Single", "Have partner", "Prefer not to say"],
        widget=widgets.RadioSelect,blank=True,
    )
    Monthly_income = models.IntegerField(
        label="5- What is your net monthly income (Euro)?", max=20000, min=1,blank=True,
    )
    life_satisfaction_score = models.IntegerField(
        label="6- How would you rate your level of satisfaction with your life (1-100)?",
        max=100,
        min=1,blank=True,
    )

    hidden_input = models.IntegerField(initial=50, blank=True)
       

        

    # Popout Page
    pic = models.StringField(
        label="7- Life satisfaction - please select one picture.",
        choices=["pic-yes", "pic-no"],
        widget=widgets.RadioSelect, blank=True,
    )
    popout_yes = models.StringField(blank=True)
    popout_no = models.StringField(blank=True)
    time_popout = models.StringField(initial='-999',blank=True)
    
    # End Page
    group_assignment = models.StringField(blank=True)

