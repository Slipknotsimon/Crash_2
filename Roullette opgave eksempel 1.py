# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 09:46:22 2019

@author: Bruger
"""

#Simon Hasselflug

#Roullette opgave eksempel 1

#Class definition
class Outcome:
    def __init__(self, name, odds):
        self.name = name
        self.odds = odds
    
    
#Udfald, fejl kast
oc1 = Outcome ("Any Craps", 8)
oc2 = Outcome ("Any Craps", 8)
oc1 == oc2
False
id(oc1)
4334572936
id(oc2)
4334573272


#hash code fejl kast
hash(oc1)
270386794
hash(oc2)
270392959

#Besked
def __str__( self ):
    return "{name:s} ({odds:d}:1)".format_map(vars(self) )

def __repr__( self ):
    return "{class_:s} ({odds!r})".format(
            class_=type(self).__name__,**vars(self) )
    
#Wrap an Extrend collection
class Bin:
    def __init__(self, outcomes):
        self.outcomes = frozenset (outcomes)

class Bin (frozenset):
    pass
    
        
            
#Struktur metoder
five= Outcome("00-0-1-2-3", 6)
zero= Bin( [Outcome ("0",35), five] )
zerozero= Bin( [Outcome("00,35"), five] )

#Methods
bin1 = Bin( {outcome1, outcome2, outcome3} )

#Test setup
class Given_wheel_WHEN_next_THEN_random_choice(unittest.TestCase):
    def setUp(self):
        self.wheel= Wheel()
        self.wheel.rng.seed(1)
    def runTest(self):
        etc
        x = random.Random()
        x.seed(1)
        [x.randint(0,37) for i in range(10)]
        [8,36,4,16, 7,31,28,30,24,13]

#Bad idea
my_bet= Bet(Outcome("red", 1), 25)

#Global mapping
some_map["Red"]
Outcome('Red', 1)

#Factory function
some_factory("Red")
Outcome('Red', 1)

#Class Method
Outcome.getInstance("Red")
Outcome('Red', 1)

#Binbuilder as Factory
theBinBuilder.getOutcome("Red")
Outcome('Red', 1)

#wheel as Factory
theWheel.getOutcomes("Red")
Outcome('Red', 1)

class BinBuilder(object):
    #...
    def apply(self, outcome, bin, wheel):
        self.all_outcomes.add(outcome)
        wheel.add(bin, outcome)
    def getOutcome(self, name):
        #...
    
class wheel(object):
    #...
    def add(self, bin, outcome):
        self.all_outcomes.add(outcome)
        #...
    def getOutcomes(self, name):
        return set( [oc for oc in self.all_outcomes if oc.name.lower().contains(name.lower())

#Default initialization
class Wheel:
    def __init__(self, rng=None):
        self.rng= rng if rng is not None else random.Random()
        #...rest of wheel construction...
        
#Mock Object Testing       
from unittest.mock import MagicMock, Mock
import unittest

class GIVEN_Wheel_WHEN_spin_THEN_return_bin(unittest-TestCase):
    def setUp(self):
        self.bins = [ "bin1", "bin2" ]
        self.wheel = Wheel (self.bins)
        #Patch the  random number generator
        self.wheel.rng= Mock()
        self.wheel.rng.choice = Mock( return_value="bin1")
        
    def runTest(self):
        value = self.wheel.next()
        self.assertEqual( value, "bin1")
        self.wheel.rng.choice.assert_called_with(self.bins)
        
unittest.main()

#Soapbox on Composition
thewheel = wheel()
thetTable =  Table()
theGame = Game(thewheel, theTable)
thePlayer = sevenReds (theTable)
sim = new Simulator( theGame, thePlayer)
sim.gather()

#Some Foundations
s = sum(theList)
n = len(theList)

s = sum( f(x) for x in theList)
n = len(theList)

#Mean
sum(self)/len(self)

#Sum Devlation
m = mean(x)
math.sqrt( sum((x-m**2 for x in self) / (len(self)-1) )

#Pretty Poor Polymorphism
class SomeClient(object):
    def someMethod(self):
        if isinstance (x, Aclass):
            Special Case that should have been part of AClass
                     
    
    

        