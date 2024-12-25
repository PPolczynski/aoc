class Gates:
    def __init__(self, known, graph):
        self._known_gates = dict()
        for k in known:
            gate, value = k.split(": ")
            self._known_gates[gate] = int(value)
        # x00 AND y00 -> z00
        self._z_gates = []
        self._gates_graph = dict()
        for graph_node in graph:
            gate_left, operation, gate_right, _, out_gate = graph_node.split(" ")
            self._gates_graph[out_gate] = (gate_left, gate_right, operation)
            if out_gate.startswith("z"):
                self._z_gates.append(out_gate)
        self._z_gates.sort(reverse=True)

    def get_z_gets_decimal(self):
        return int("".join([str(self._dfs(z_gates)) for z_gates in self._z_gates]), 2)

    def _dfs(self, gate):
        if gate in self._known_gates:
            return self._known_gates[gate]
        else:
            gate_left, gate_right, operation = self._gates_graph[gate]
            left_value = self._dfs(gate_left)
            right_value = self._dfs(gate_right)
            out_value = 0
            if operation == "AND":
                out_value = left_value & right_value
            elif operation == "OR":
                out_value = left_value | right_value
            elif operation == "XOR":
                out_value = left_value ^ right_value
            self._known_gates[gate] = out_value
            return out_value

    def part2(self):
        fixes = []
        while True:
            is_valid, fail_idx = self.validate()
            if is_valid:
                break
            print(f"fails at bit: {fail_idx}")
            print(f"gate z{fail_idx:0>2}")
            self.bfs(f"z{fail_idx:0>2}")
            print(f"next gate z{fail_idx + 1:0>2}")
            self.bfs(f"z{fail_idx + 1:0>2}")
            a,b = input("give , separated pair to switch\n").strip().split(",")
            self.swap(a,b)
            is_valid, new_fail_idx = self.validate()
            if not is_valid and new_fail_idx <= fail_idx:
                print("wrong gates, reverting...")
                self.swap(a, b)
            else:
                fixes.append(a)
                fixes.append(b)
        return ",".join(sorted(fixes))


    def validate(self):
        if (not self.validate_for_input(1, 0)
            or not self.validate_for_input(0, 1)
            or not self.validate_for_input(1,1)):
            return False, 0
        else:
            bits_input = len(self._z_gates) - 1
            for idx in range(1, bits_input):
                combinations = [
                    (2**idx, 0), #10  00 -> 10
                    (0, 2 ** idx), #00 10 -> 10
                    (2**idx, 2**idx), #10 10 ->100
                    (2**idx + 2**(idx - 1), 2**(idx - 1)), #11 01 -> 100 first two cases should cover reverse situation
                    (2**idx + 2**(idx - 1), 2**idx + 2**(idx - 1))  #11 11 -> 110
                ]
                for x, y in combinations:
                    if not self.validate_for_input(x, y):
                        return False, idx + 1
        return True, 0

    def validate_for_input(self, x, y):
        self.set_known(x, y)
        result = int("".join([str(self._dfs(z_gates)) for z_gates in self._z_gates]), 2)
        return x + y == result

    def swap(self, gate_a, gate_b):
        tmp = self._gates_graph[gate_a]
        self._gates_graph[gate_a] = self._gates_graph[gate_b]
        self._gates_graph[gate_b] = tmp

    def set_known(self, x, y):
        bits_input = len(self._z_gates) - 1
        new_input = dict()
        for idx, bit in enumerate(f"{x:b}".rjust(bits_input, "0")):
            new_input[f"x{bits_input - idx - 1:0>2}"] = int(bit)
        for idx, bit in enumerate(f"{y:b}".rjust(bits_input, "0")):
            new_input[f"y{bits_input - idx - 1:0>2}"] = int(bit)
        self._known_gates = new_input

    def bfs(self, gate):
        queue = [(gate, self._gates_graph[gate])]
        while queue:
            print(queue)
            tmp = []
            while queue:
                gate, node = queue.pop()
                gate_left, gate_right, operation = node
                if gate_left in self._gates_graph:
                    tmp.append((gate_left, self._gates_graph[gate_left]))
                if gate_right in self._gates_graph:
                    tmp.append((gate_right, self._gates_graph[gate_right]))
            queue = tmp
