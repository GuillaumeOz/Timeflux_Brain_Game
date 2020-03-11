import numpy as np
import pandas as pd
from timeflux.core.node import Node

class ConcatResult(Node):

    """ Concat p1 and p2 score and add the diff
        [{score_p1: (float), score_p2: (float), diff_p1_p2: (float)]
    

    Attributes:
        i_p1 (port): score player_1, expects Dataframe
        i_p2 (port): score player_2, expects Dataframe
        o (port): Dataframe
    """

    def __init__(self):
        pass

    def update(self):

        print("---------------------")
#        print(self.i_p1.data)
#        print(self.i_p2.data)
        print(self.i_p1.ready())
        print(self.i_p2.ready())
        print("---------------------")
        if not (self.i_p1.ready() & self.i_p2.ready()):
            return
        p1 = pd.DataFrame(self.i_p1.data).rename(columns={"score": "score_p1"})
        p2 = pd.DataFrame(self.i_p2.data).rename(columns={"score": "score_p2"})
        diff = p1['score_p1'].values[0] - p2['score_p2'].values[0]
        result = pd.DataFrame([{'diff_p1_p2': diff}])
        frames = [p1, p2, result]
        self.o.data = pd.concat(frames, axis=1)
    
