class Secrets:
    def __init__(self):
        pass

    @staticmethod
    def calculate_next_secret(number):
        # 2^6 64
        # 2^5 32
        # 2^11 2024
        # 16777216 = 2 ^ 24
        #  x % 2 ^ n == x & (2 ^n-1)
        new_number = (number ^ (number << 6)) & 16777215 #0b1000000000000000000000000
        new_number = (new_number ^ (new_number >> 5) ) & 16777215
        new_number = (new_number ^ (new_number << 11) ) & 16777215
        return new_number

    @staticmethod
    def get_nth_secret_number(secret_number, iterations):
        nth_number = secret_number
        for _ in range(iterations):
            nth_number = Secrets.calculate_next_secret(nth_number)
            # print(f"{_} {nth_number}")
        return nth_number

    @staticmethod
    def get_nth_changes_and_prices(secret_number, iterations):
        nth_number = secret_number
        previous_price = secret_number % 10
        out = []
        for _ in range(iterations):
            nth_number = Secrets.calculate_next_secret(nth_number)
            current_price = nth_number % 10
            out.append((current_price, current_price - previous_price))
            previous_price = current_price

        return out

    @staticmethod
    def changes_and_prices_to_dict(bit_changes):
        candidates = dict()
        for i, value in enumerate(bit_changes[3:]):
            price, change = value
            key = tuple(change for _, change in bit_changes[i : i + 4])
            if key not in candidates:
                candidates[key] = price
        return candidates

    @staticmethod
    def get_max_bananas_sum_after_n_secrets(secret_numbers, iterations):
        change_logs = []
        for secret_number in secret_numbers:
            change_logs.append(Secrets.changes_and_prices_to_dict(Secrets.get_nth_changes_and_prices(secret_number, iterations)))
        keys = set()
        for change_log in change_logs:
            keys |= set(change_log.keys())
        max_bananas = float("-Inf")
        for key in keys:
            max_bananas = max(max_bananas, sum([change_log.get(key, 0) for change_log in change_logs]))
        return max_bananas

    @staticmethod
    def get_nth_secret_number_sum(secret_numbers, iterations):
        return sum([Secrets.get_nth_secret_number(secret_number, iterations) for secret_number in secret_numbers])
