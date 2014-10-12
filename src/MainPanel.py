'''
Created on Sep 10, 2013

@author: ccole
'''

from javax.swing import JPanel
from java.awt import BorderLayout

class MainPanel(JPanel):
    def __init__ (self):
        self.panel = JPanel(BorderLayout())
        model = Model()
        view = View(model)