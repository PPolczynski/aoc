from collections import defaultdict


class LanParty:
    def __init__(self, lines: list[str]):
        self._connections = defaultdict(list)
        for line in lines:
            c1, c2 = line.split("-")
            self._connections[c1].append(c2)
            self._connections[c2].append(c1)

    def get_group_connection_filtered(self):
        list_connections = set()
        for computer in self._connections.keys():
            if computer.startswith("t"):
                for idx, connection in enumerate(self._connections[computer]):
                    for other_connections in  self._connections[computer][idx + 1:]:
                        if other_connections in  self._connections[connection]:
                            list_connections.add(tuple(sorted([computer, connection, other_connections])))
        return len(list_connections)

    def get_largest_set(self):
        largest = set()
        for computer in self._connections.keys():
            network = set()
            self._dfs(computer, network)
            if len(network) > len(largest):
                largest = network
        return ",".join(sorted(list(largest)))


    def _dfs(self, computer, network):
        if computer in network:
            return
        elif all([computer in self._connections[other] for other in network]):
            network.add(computer)
            for connection in self._connections[computer]:
                self._dfs(connection, network)

