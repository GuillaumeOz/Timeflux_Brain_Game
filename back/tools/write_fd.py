import pandas as pb
import numpy as np
from timeflux.core.node import Node


class Insert(Node):

    """ Write the score in a file

    Attributes: i (port): DataFrame
                o (port): Dataframe
    """
    def __init__(self, path=None):
        self.path = path

    def update(self):
        if self.path == None:
            return
        if self.i.ready() == False:
            return
        print(self.path)
        fd = open(str( self.path), 'w')
        fd.write(str(self.i.data['diff_p1_p2'].values[0]))
        self.o.data = self.i.data

