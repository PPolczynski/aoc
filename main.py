import argparse
import configparser
from typing import Optional

import registration
from puzzle import Solver, Client

def get_config_value(key: str, arg_value: Optional[str] = None) -> Optional[str]:
    """Consolidated configuration lookup: Args > Env > config.ini > .env"""
    if arg_value:
        return arg_value

    config = configparser.ConfigParser()
    if config.read("config.ini") and "AOC" in config:
        if key in config["AOC"]:
            return config["AOC"][key]
            
    return None

def main():
    parser = argparse.ArgumentParser(description="Advent of Code runner")
    parser.add_argument("-y", "--year", help="Year to run")
    parser.add_argument("-d", "--day", help="Day to run")
    parser.add_argument("-token", "--token", help="AOC session token")
    parser.add_argument("-refresh", "--refresh", action="store_true", help="Refresh input data")
    
    args = parser.parse_args()
    
    token = get_config_value("AOC_SESSION_TOKEN", args.token)
        
    client = Client(token, refresh=args.refresh, path="./tmp")
    solver = Solver(client)

    registration.register_all(solver)
                
    solver.solve(args.year, args.day)

if __name__ == "__main__":
    main()
