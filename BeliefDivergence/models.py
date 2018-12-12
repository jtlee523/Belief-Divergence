from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
#pandas>=0.22.0
#import pandas as pd


author = 'Joseph Lee'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'BeliefDivergence'
    players_per_group = None #Single player game

    #df = pd.read_csv('Task1Data.csv') #reads the data and creates a dataframe
    #data = df.values.tolist() #makes a list of lists, ripped off by row.
    #FORMAT: [Black ball for Red, Yellow, Green, Urn prob Red, Urn prob Yellow, Urn Prob G]
    data = [[0.8,0.5,0.2, 0.25, 0.5, 0.25, 0], #7 numbers. add a 0 for black, 1 for white: #task2: same 7, plus other 4 ->point values
    [0.6,0.5,0.4, 0.4, 0.5, 0.1, 1]]
    """data = [[0.8,0.5,0.2], 
    [0.6,0.5,0.4],
    [0.8,0.6,0.2],
    [0.4,0.3,0.1],
    [1.0,0.5,0.5],
    [0.9,0.9,0.4],
    [0.4,0.8,0.2],
    [0.3,0.3,0.3],
    [0.8,0.7,0.6],
    [0.8,0.5,0.8]]"""
    num_rounds = len(data) #as many rounds as there are lines of data



class Subsession(BaseSubsession):

	def creating_session(self):
	
		if self.round_number == 1: #if we are on the first round
			self.session.vars['data'] = Constants.data.copy() #we record the data to something on self.
		
		
		for p in self.get_players():
			task1_data = p.current_data()
			p.Assigned_Red = task1_data[0]
			p.Assigned_Yellow = task1_data[1]
			p.Assigned_Green = task1_data[2]
			p.Red_Urn_Given = task1_data[3]
			p.Yellow_Urn_Given = task1_data[4]
			p.Green_Urn_Given = task1_data[5]
			p.isBlackBall = task1_data[6]


class Group(BaseGroup):
    pass


class Player(BasePlayer):
	Red_Probability_guess = models.IntegerField()
	Green_Probability_guess = models.IntegerField()
	Yellow_Probability_guess = models.IntegerField()
	
	Red_Urn_Given = models.FloatField()
	Yellow_Urn_Given = models.FloatField()
	Green_Urn_Given = models.FloatField()
	
	isGray = models.BooleanField()
	Accuracy = models.FloatField()
	
	#These are the black/white probabilities
	Assigned_Red = models.FloatField()
	Assigned_Yellow = models.FloatField()
	Assigned_Green = models.FloatField()
	
	isBlackBall = models.IntegerField()
	
	def current_data(self):
		return self.session.vars['data'][self.round_number-1] #returns a row of the data
	
    



#https://otree.readthedocs.io/en/latest/misc/tips_and_tricks.html

"""
PLAN!
make 3 apps, one for each task
THEN, in settings, create a main app that calls task 1 then task 2
"""