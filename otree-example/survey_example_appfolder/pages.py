from otree.api import Currency as c, currency_range, safe_json
from ._builtin import Page, WaitPage
from .models import Constants, Player


from survey_example_appfolder.HelperFunctions import detect_screenout, detect_quota




class Welcome(Page):
    form_model = Player
    form_fields = ['device_type', 'operating_system', 'screen_height', 'screen_width','permission','eligible_question']
    
    #with the function before_next_page you can can control what should happen. It is a nice feature for filtering
    #or also setting variables
    def before_next_page(self):
        self.group.counter += 1

#we want to detect all the screenouts and the quota reached right away
        detect_screenout(self)
        detect_quota(self)

class DemoPage(Page):
    form_model = Player
    form_fields = ['gender', 'age', 'Academic_status', 'Marital_status','Monthly_income','life_satisfaction_score','hidden_input' ]
    
    def before_next_page(self):
    # Check age and set screenout if 40 or older
        if self.player.age >= 40:
           self.player.screenout = True

    # Check quota for gender
        gender = self.player.gender
        if gender not in self.session.vars['gender_quota']:
          self.player.quota = True
        elif self.session.vars['gender_counts'][gender] >= self.session.vars['gender_quota'][gender]:
            self.player.quota = True
        else:
           self.session.vars['gender_counts'][gender] += 1


    def vars_for_template(self):
        return {'participant_label': safe_json(self.participant.label),
                'screenout': safe_json(self.player.screenout),
                'quota': safe_json(self.player.quota)
                }


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
    
    
class RedirectPage(Page):
    def vars_for_template(self):
        # Determine the redirect URL based on conditions
        if self.player.screenout:
            redirect_url = '/static/ScreenoutLink.html'
        elif self.player.quota:
            redirect_url = '/static/QuotaFullLink.html'
        else:
            redirect_url = '/static/CompletionLink.html'

        # Pass necessary variables to the template
        return {
            'redirect_url': redirect_url,
            'participant_label': safe_json(self.participant.label),
            'screenout': self.player.screenout,  # Add screenout variable
            'quota': self.player.quota,          # Add quota variable
        }



    form_model = Player
#Here we define in which ordering we want the pages to be shown. We always start with a Welcome page and end with an End page.
page_sequence = [Welcome,
                DemoPage,
                Html_overview,
                PopoutPage,
                EndPage,
                RedirectPage]