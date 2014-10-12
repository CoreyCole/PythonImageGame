'''
Created on Sep 9, 2013

@author: ccole
'''

from javax.swing import JFrame
from src import MainPanel

f = JFrame('Python Image Game')
f.setDefaultCloseOperation(JFrame.HIDE_ON_CLOSE)
f.setSize(300, 300)
f.setLocationRelativeTo(None)
f.setVisible(True)

f.add(MainPanel())