from collections import deque, defaultdict


class Solution:

    @staticmethod
    def calculate_next_secret(number):
        # 2^6 64
        # 2^5 32
        # 2^11 2024
        # 16777216 = 2 ^ 24
        #  x % 2 ^ n == x & (2 ^n-1)
        new_number = (number ^ (number << 6)) & 16777215
        new_number = (new_number ^ (new_number >> 5) ) & 16777215
        new_number = (new_number ^ (new_number << 11) ) & 16777215
        return new_number

    @staticmethod
    def get_nth_secret_number(secret_number, iterations):
        nth_number = secret_number
        for _ in range(iterations):
            nth_number = Solution.calculate_next_secret(nth_number)
        return nth_number

    @staticmethod
    def get_nth_changes_and_prices(secret_number, iterations):
        nth_number = secret_number
        previous_price = secret_number % 10
        out = dict()
        key_queue = deque()
        for _ in range(iterations):
            nth_number = Solution.calculate_next_secret(nth_number)
            current_price = nth_number % 10
            key_queue.append(current_price - previous_price)
            previous_price = current_price
            if len(key_queue) == 4:
                key = tuple(key_queue)
                if key not in out:
                    out[key] = current_price
                key_queue.popleft()
        return out

    @staticmethod
    def get_max_bananas_sum_after_n_secrets(secret_numbers, iterations):
        sequence_max_bananas = defaultdict(int)
        for secret_number in secret_numbers:
            changes = Solution.get_nth_changes_and_prices(secret_number, iterations)
            for key, bananas in changes.items():
                sequence_max_bananas[key] += bananas
        return max(sequence_max_bananas.values())

    @staticmethod
    def get_nth_secret_number_sum(secret_numbers, iterations):
        return sum([Solution.get_nth_secret_number(secret_number, iterations) for secret_number in secret_numbers])
