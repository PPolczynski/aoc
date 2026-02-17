from puzzle import Event
from .d01 import solution as day1
from .d02 import solution as day2
from .d03 import solution as day3
from .d04 import solution as day4
from .d05 import solution as day5

event = Event([day1.solution,
               day2.solution,
               day3.solution,
               day4.solution,
               day5.solution])
