from otree.api import Currency as c, currency_range, safe_json
from ._builtin import Page, WaitPage
from .models import Constants, Player


#from survey_example_appfolder.HelperFunctions import detect_screenout_age, detect_screenout_eligible, detect_quota




class Welcome(Page):
    form_model = Player
    form_fields = ['device_type', 'operating_system', 'screen_height', 'screen_width','permission','eligible_question']
    
    
        #with the function before_next_page you can can control what should happen. It is a nice feature for filtering
    #or also setting variables
    def before_next_page(self):
        from .HelperFunctions import detect_screenout_eligible
        
        detect_screenout_eligible(self)

        if self.player.screenout:
            return
    
    
    def vars_for_template(self):
        #print("Participant Label on Welcome Page:", self.participant.label)
        return {
            "participant_label": self.participant.label
        }   

class DemoPage(Page):
    form_model = Player
    form_fields = ['gender', 'age', 'Academic_status', 'Marital_status', 'Monthly_income', 'life_satisfaction_score', 'hidden_input']

    def before_next_page(self):
        from .HelperFunctions import detect_screenout_age, detect_quota

        detect_screenout_age(self)
        
        if self.player.screenout:
            #self.player.redirect_url = "/static/ScreenoutLink.html"
            return
        
        detect_quota(self)
        if self.player.quota:
            #self.player.redirect_url = "/static/QuotaFullLink.html"
            return


    def vars_for_template(self):
        return {
            'participant_label': safe_json(self.participant.label),
            'screenout': safe_json(self.player.screenout),
            'quota': safe_json(self.player.quota)
        }



class Html_overview(Page):
    form_model = Player
    
    def is_displayed(self):
        return self.player.group_assignment == 'pic-yes'

class PopoutPage(Page):
    form_model = Player
    form_fields = ['pic', 'popout_yes', 'popout_no', 'time_popout']
    

    def before_next_page(self):
        if self.player.pic == 'pic-yes':
            self.player.group_assignment = 'pic-yes'
            self.player.popout_yes = "Excellent. What is the most important factor affecting your life satisfaction?"
        elif self.player.pic == 'negative_picture':
            self.player.group_assignment = 'pic-no'
            self.player.popout_no = "Sorry to hear that. What is the most important factor affecting your life dissatisfaction?"

class EndPage(Page):
    def vars_for_template(self):
        return {
            "group_assignment": safe_json(self.player.group_assignment),
            "participant_label": self.participant.label if self.participant.label else "N/A",
        }

    
class RedirectPage(Page):
    def vars_for_template(self):
        # Determine the redirect URL based on conditions
        if self.player.screenout:
            redirect_url = '/static/ScreenoutLink.html'
        elif self.player.quota:
            redirect_url = '/static/QuotaFullLink.html'
        else:
            redirect_url = '/static/CompleteLink.html'
        

        return {
            "participant_label": self.participant.label,
            "quota": self.player.quota,
            "screenout": self.player.screenout,
            "redirect_url": redirect_url,  # Use the dynamically determined redirect URL
        }

    form_model = Player

#Here we define in which ordering we want the pages to be shown. We always start with a Welcome page and end with an End page.
page_sequence = [Welcome,
                DemoPage,
                Html_overview,
                PopoutPage,
                EndPage,
                RedirectPage]