from constants.locators import *
from constants.constants import *

def select_accordion_helper():
    sets = [(BaseLocators.Q0, BaseLocators.A0, Answers.AN0),
            (BaseLocators.Q1, BaseLocators.A1, Answers.AN1),
            (BaseLocators.Q2, BaseLocators.A2, Answers.AN2),
            (BaseLocators.Q3, BaseLocators.A3, Answers.AN3),
            (BaseLocators.Q4, BaseLocators.A4, Answers.AN4),
            (BaseLocators.Q5, BaseLocators.A5, Answers.AN5),
            (BaseLocators.Q6, BaseLocators.A6, Answers.AN6),
            (BaseLocators.Q7, BaseLocators.A7, Answers.AN7)
            ]
    return sets