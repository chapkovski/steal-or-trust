from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'steal_or_trust'
    players_per_group = None
    num_rounds = 1
    treatments = ['trust', 'steal']


class Subsession(BaseSubsession):
    def creating_session(self):
        assert self.session.config.get('treatment', 'trust') in Constants.treatments, 'No such treatment'
        for g in self.get_groups():
            g.treatment = self.session.config.get('treatment', 'trust')


class Group(BaseGroup):
    treatment = models.StringField(doc='trust or stealin framing of PG')


class Player(BasePlayer):
    pass
