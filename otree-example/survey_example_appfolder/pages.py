from otree.api import Currency as c, currency_range, safe_json
from ._builtin import Page, WaitPage
from .models import Constants, Player



class Welcome(Page):
    form_model = Player
    form_fields = ['device_type', 'operating_system', 'screen_height', 'screen_width','permission']
    def before_next_page(self):
        
        self.group.counter += 1


class DemoPage(Page):
    form_model = Player
<<<<<<< HEAD
    form_fields = ['Gender', 'Age', 'Academic_status', 'Marital_status','Monthly_income','life_satisfaction_score','hidden_input' ]


class Html_overview(Page):
    form_model = Player
    def is_displayed(self):
        return self.player.group_assignment == 1

class PopoutPage(Page):
    form_model = Player
    form_fields = ['pic', 'popout_yes', 'popout_no', 'time_popout']


class EndPage(Page):
    def vars_for_template(self):
        
        return {"group_assignment": safe_json(self.player.group_assignment)}
    
    form_model = Player

#Here we define in which ordering we want the pages to be shown. We always start with a Welcome page and end with an End page.
page_sequence = [Welcome,
                DemoPage,
                Html_overview,
                PopoutPage,
                EndPage]
=======
    form_fields = ['Gender', 'Age', 'Academic_status', 'Marital_status','Monthly_income','life_satisfaction_score','Idea' ]

class EndPage(Page):
    #style: this is a good example of the style 'CamelCase' that one normally uses for classes
    form_model = Player


    def vars_for_template(self):
        return {'message': " You can now close the window.",}


#Here we define in which ordering we want the pages to be shown. We always start with a Welcome page and end with an End page.
page_sequence = [Welcome,
                DemoPage,           
                EndPage]
>>>>>>> d29909c232463cb393f70c63ba4de0b5edfa5f54
