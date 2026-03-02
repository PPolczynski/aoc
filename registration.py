import y2023
import y2024
import y2025
from puzzle import Solver


def register_all(solver: Solver):
    solver.register(y2023.event)
    solver.register(y2024.event)
    solver.register(y2025.event)
