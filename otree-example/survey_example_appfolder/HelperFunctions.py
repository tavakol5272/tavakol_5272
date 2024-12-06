import random

def random_number(x, y):
    '''
    method for random integers
    '''  
    rng = random.Random()
    number = rng.randint(x, y)
    return number



'''
we also want to implement some functions to help with the quota checking and 
to have an overwview (counting) who is taking part in our survey.

Generally when it comes to redirecting we distinguish between people who: 
1. took part in the whole survey (and get redirected as success to the provider)
2. people who get screened-out (meaning they did not fulfill a characteristic one agreed upon previously)
3. people who get redirected because the quota is already full

We encode those three different event in three different variables (booleans) to use for redirecting

'''

def detect_screenout_eligible(self):
    
    if self.player.eligible_question == 2: 
        self.player.screenout = 1

def detect_screenout_age(self):
    
    if self.player.age is not None and self.player.age > 40: 
        self.player.screenout = 1


def detect_quota(self):
    '''Check if a quota is already filled and set redirect URL.'''
    gender_counts = self.session.vars['gender_counts']
    gender_quota = self.session.vars['gender_quota']
    gender = self.player.gender

    # Directly use counts and quotas since genders are validated
    if gender_counts[gender] >= gender_quota[gender]:
        self.player.quota = 1
    else:
        gender_counts[gender] += 1
 

def set_participant_label(self, label):
    
    self.player.participant_label = label



# def participant_count(self):
#     '''if we want to count different things we might also implement a function here.
#     For now we are just using the counter we implemented before'''
#     return None