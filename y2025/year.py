from puzzle import Event
from .d01 import solution as day1
from .d02 import solution as day2
from .d03 import solution as day3
from .d04 import solution as day4
from .d05 import solution as day5
from .d06 import solution as day6
from .d07 import solution as day7
from .d08 import solution as day8
from .d09 import solution as day9

event = Event([day1.solution, day2.solution, day3.solution, day4.solution, day5.solution, day6.solution, day7.solution,
               day8.solution, day9.solution, ])
