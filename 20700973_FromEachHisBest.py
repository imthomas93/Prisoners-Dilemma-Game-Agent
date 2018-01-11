from prison import Player
import random

class FromEachHisBest(Player):
    """
    Agent Written by Thomas Lim Jun Wei (20700973)
    """
    def studentID(self):
        return "20700973"
    def agentName(self):
        return "From_Each_His_Best"
    def play(self, myHistory, oppHistory1, oppHistory2):
        '''
        This agent will play nice for the first round, always defect on the last,
        and play with a decision that track if other agents that are playing GRIM or TfT.
        '''
        # Intial round is to coorperate for first round
        if not myHistory:
            return 0;
        # Last round, perform a deflect to increase score
        elif len(myHistory) == 99:
            return 1;
        # In between we will try not to defect twice in a row,
        # this is to allow for us to discover strategies that is forgiving.
        elif len(myHistory) > 1:
            #Suspect GRIM Player - Play defect all the way
            if (oppHistory1[-1] == 1 and oppHistory1[-2] == 1) or (oppHistory2[-1] == 1 and oppHistory2[-2] == 1):
                return 1;
            #Suspect TfT Player - be Forgiving and mutual cooperate.
            elif (oppHistory1[-1] == 1 and oppHistory1[-2] == 0) or (oppHistory2[-1] == 1 and oppHistory2[-2] == 0):
                return 0;
            else:
                return 0;
        # Default move - play nice and return a cooperate to ensure mutual scoring and not to provoke other agents.
        else:
            return 0; 
