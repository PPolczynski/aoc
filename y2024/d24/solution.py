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

