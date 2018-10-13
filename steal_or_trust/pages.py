from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

def vars_for_all_templates(self):
    return {'instructions': '/Instructions.html'.format(self.group.treatment),
            'belief_instructions': '/BeliefInstructions.html'.format(self.group.treatment)
            }


class Intro(Page):
    ...

class BeliefIntro(Page):
    ...

class SenderDecision(Page):
    ...


class BeforeReceiverWP(WaitPage):
    ...


class ReceiverDecision(Page):
    ...


class BeliefElicitation(Page):
    ...


class BeforeResultsWP(WaitPage):
    ...


class Results(Page):
    pass


page_sequence = [
    Intro,
    BeliefIntro,
    SenderDecision,
    BeforeReceiverWP,
    ReceiverDecision,
    BeliefElicitation,
    BeforeResultsWP,
    Results,
]
