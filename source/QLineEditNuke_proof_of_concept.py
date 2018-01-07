# -----------------------------------------------------------------------------#
#
# @ File: QLineEditNuke_proof_of_concept.py
# @ Author: Stefan Muller
#
# -----------------------------------------------------------------------------#
#
# QLineEditNuke_proof_of_concept
# just copy and paste to nuke's script editor and run...
#
# -----------------------------------------------------------------------------#

# -----------------------------------------------------------------------------#
# import
# -----------------------------------------------------------------------------#

# encoding=utf8

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import nuke

# -----------------------------------------------------------------------------#
# classes
# -----------------------------------------------------------------------------#

class QLineEditNuke(QLineEdit):
    '''
    subclass QLineEdit for nuke
    __init__(): default behaviour, plus it creates a native nuke String_Knob
    to store the QlineEdit value and puts it back into the Widget
    keyPressEvent(): default behaviour, plus the widget's value gets stored
    in the native nuke knob while typing
    '''

    def __init__(self, node, name):
        super(self.__class__, self).__init__()

        self.node = node
        self.name = name

        if self.name not in self.node.knobs():
            hidden_knob = nuke.String_Knob(self.name, self.name)
            self.node.addKnob(hidden_knob)
            hidden_knob.setVisible(False)
        else:
            hidden_knob = self.node.knob(self.name).getValue()
            self.setText(hidden_knob)

    def keyPressEvent(self, e):
        super(self.__class__, self).keyPressEvent(e)
        self.node.knob(self.name).setValue(self.text())


class MyWidget(QWidget):
    def __init__(self, node):
        super(self.__class__, self).__init__()

        self.node = node

        self.my_label = QLabel('this QLineEdit is able to remember values')

        # we need to pass two arguments for our QLineEditNuke
        # the node, so that we can create a knob on that node
        # and some arbitrary, unique name, so we can find our knob later
        self.my_lineEdit = QLineEditNuke(self.node, 'my_line_edit')

        my_layout = QHBoxLayout()
        my_layout.addWidget(self.my_label)
        my_layout.addWidget(self.my_lineEdit)

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)
        self.setLayout(main_layout)
        main_layout.addLayout(my_layout)

    def makeUI(self):
        return self

    def updateValue(self):
        pass


# -----------------------------------------------------------------------------#
# run
# -----------------------------------------------------------------------------#

if __name__ == "__main__":
    node = nuke.createNode('NoOp')
    node.knob('name').setValue('PySideTestNode')
    knob = nuke.PyCustom_Knob("MyWidget", "", "MyWidget(nuke.thisNode())")
    node.addKnob(knob)
