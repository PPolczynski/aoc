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
        y_gates = []
        x_gates = []
        for gate in self._known_gates.keys():
            if gate.startswith("y"):
                y_gates.append(gate)
            elif gate.startswith("x"):
                x_gates.append(gate)
        y_gates.sort(reverse=True)
        x_gates.sort(reverse=True)
        print("0"+ "".join([str(self._known_gates[gate]) for gate in x_gates]))
        print("0" + "".join([str(self._known_gates[gate]) for gate in y_gates]))
        print("".join([str(self._dfs(z_gates)) for z_gates in self._z_gates]))
        a = int("0"+ "".join([str(self._known_gates[gate]) for gate in x_gates]), 2)
        b = int("0" + "".join([str(self._known_gates[gate]) for gate in y_gates]), 2)
        print(a + b)
        print(int("".join([str(self._dfs(z_gates)) for z_gates in self._z_gates]),2))
        # print(self.bfs("z11"))
        # print(self.bfs("z17"))
        # print(self.bfs("z26"))
        print(self.bfs("z39"))

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
