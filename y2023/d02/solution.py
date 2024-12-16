class CubeGame:
    def __init__(self, cubes: list[tuple[str, int]]):
        self._cubes = dict()
        for color, cnt in cubes:
            self._cubes[color] = cnt

    def get_sum_possible_id(self, game_records: list[str]) -> int:
        sum_id = 0
        for game_record in game_records:
            game_id, game = self._parse_game_record(game_record)
            if self._get_is_game_possible(game):
                sum_id += game_id
        return sum_id

    def get_sum_of_power(self, game_records: list[str]) -> int:
        sum_power = 0
        for game_record in game_records:
            game_id, game = self._parse_game_record(game_record)
            min_set = self._get_minimal_possible_set(game)
            power_of_min_set = 1
            for _, cnt in min_set:
                power_of_min_set *= cnt
            sum_power += power_of_min_set
        return sum_power

    def _get_minimal_possible_set(self, draws: list[list[tuple[str, int]]]) -> list[tuple[str, int]]:
        min_set_dict = dict()
        for color in self._cubes.keys():
            min_set_dict[color] = 0
        for draw in draws:
            for color, cnt in draw:
                min_set_dict[color] = max(min_set_dict[color], cnt)
        min_set = []
        for color, cnt in min_set_dict.items():
            min_set.append((color, cnt))
        return min_set

    def _get_is_game_possible(self, draws: list[list[tuple[str, int]]]) -> bool:
        return all([all([cnt <= self._cubes[color] for color, cnt in draw]) for draw in draws])

    @staticmethod
    def _parse_game_record(game_record) -> tuple[int, list[list[tuple[str, int]]]]:
        game_record_split = game_record.split(": ")
        game_id = int(game_record_split[0].replace("Game ", ""))
        draw_list = []
        for single_draw in game_record_split[1].split("; "):
            pairs = []
            for pair in single_draw.split(", "):
                cnt, color = pair.split(" ")
                pairs.append((str(color), int(cnt)))
            draw_list.append(pairs)
        return game_id, draw_list