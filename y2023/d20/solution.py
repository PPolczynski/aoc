import re
from abc import abstractmethod
from collections import deque

from puzzle import Solution
from enum import Enum


class Pulse(Enum):
    LOW = 0
    HIGH = 1


class ModuleType(Enum):
    FLIPFLOP = "FLIP FLOP"
    BROADCASTER = "BROADCASTER"
    BUTTON = "BUTTON"
    CONJUNCTION = "CONJUNCTION"
    OUTPUT = "OUTPUT"


_BROADCASTER_LABEL = "broadcaster"
_BUTTON_LABEL = "button"
_OUTPUT_LABEL = "output"
_FLIPFLOP_PREFIX = "%"
_CONJUNCTION_PREFIX = "&"


class Module:
    def __init__(self, label: str, module_type: ModuleType, targets: list[str], transmitter: "Transmitter"):
        self._transmitter = transmitter
        self.label = label
        self._type = module_type
        self.targets = targets
        self._transmitter.register(self)

    @abstractmethod
    def receive(self, sender: str, pulse_tye: Pulse):
        pass

    def _send(self, target: str, pulse: Pulse):
        self._transmitter.transmit(self.label, target, pulse)

    def consume_announcement(self, sender: str):
        return


class FlipFlop(Module):
    def __init__(self, label: str, targets: list[str], transmitter: "Transmitter"):
        super().__init__(label, ModuleType.FLIPFLOP, targets, transmitter)
        self._is_on = False

    def receive(self, sender: str, pulse_type: Pulse):
        if pulse_type == Pulse.HIGH:
            return
        else:
            pulse_to_send = Pulse.LOW if self._is_on else Pulse.HIGH
            self._is_on = not self._is_on
            for target in self.targets:
                self._send(target, pulse_to_send)


class Broadcaster(Module):
    def __init__(self, label: str, targets: list[str], transmitter: "Transmitter"):
        super().__init__(label, ModuleType.BROADCASTER, targets, transmitter)

    def receive(self, sender: str, pulse_type: Pulse):
        for target in self.targets:
            self._send(target, pulse_type)


class Button(Module):
    def __init__(self, label: str, targets: list[str], transmitter: "Transmitter"):
        super().__init__(label, ModuleType.BUTTON, targets, transmitter)

    def receive(self, sender: str, pulse_type: Pulse):
        raise RuntimeError(f"{str(self._type)} Module cannot receive")

    def send(self):
        for target in self.targets:
            self._send(target, Pulse.LOW)


class Conjunction(Module):
    def __init__(self, label: str, targets: list[str], transmitter: "Transmitter"):
        super().__init__(label, ModuleType.CONJUNCTION, targets, transmitter)
        self._memory = dict()

    def receive(self, sender: str, pulse_type: Pulse):
        self._memory[sender] = pulse_type
        all_high = all([last_input == Pulse.HIGH for last_input in self._memory.values()])
        pulse_to_send = Pulse.LOW if all_high else Pulse.HIGH
        for target in self.targets:
            self._send(target, pulse_to_send)

    def consume_announcement(self, sender: str):
        self._memory[sender] = Pulse.LOW


class Output(Module):
    def __init__(self, label: str, _: list[str], transmitter: "Transmitter"):
        super().__init__(label, ModuleType.OUTPUT, [], transmitter)

    def receive(self, sender: str, pulse_type: Pulse):
        # print(f"output {self.label} received {pulse_type} from {sender}")
        return


class Transmitter:
    def __init__(self):
        self._modules = dict()
        self.queue = deque()
        self.lock = False
        self.low_cnt = 0
        self.high_cnt = 0

    def register(self, module: Module):
        self._modules[module.label] = module

    def announce_senders(self):
        missing_targets = []
        for module in self._modules.values():
            for target in module.targets:
                if target not in self._modules:
                    missing_targets.append(target)
                    continue
                self._modules[target].consume_announcement(module.label)
        for target in missing_targets:
            Output(target, [], self)

    def transmit(self, sender: str, target: str, pulse: Pulse):
        self.queue.append((sender, target, pulse))
        self._transmit()

    def _transmit(self):
        if self.lock:
            return
        self.lock = True
        while len(self.queue):
            sender, target, pulse = self.queue.popleft()
            # print(f"{sender} {str(pulse)} -> {target}")
            self._modules[target].receive(sender, pulse)
            if pulse == Pulse.LOW:
                self.low_cnt += 1
            else:
                self.high_cnt += 1
        self.lock = False


def _preprocess(input_data: str) -> Transmitter:
    transmitter = Transmitter()
    lines = input_data.splitlines()
    modules = []
    for line in lines:
        labels = re.findall(r"\w+", line)
        label, targets = labels[0], labels[1:]
        if labels[0] == _BROADCASTER_LABEL:
            modules.append(Broadcaster(label, targets, transmitter))
        elif labels[0] == _OUTPUT_LABEL:
            modules.append(Output(label, [], transmitter))
        elif line[0] == _FLIPFLOP_PREFIX:
            modules.append(FlipFlop(label, targets, transmitter))
        elif line[0] == _CONJUNCTION_PREFIX:
            modules.append(Conjunction(label, targets, transmitter))
    modules.append(Output(_OUTPUT_LABEL, [], transmitter))
    return transmitter


def _part1(transmitter: Transmitter) -> any:
    button = Button(_BUTTON_LABEL, [_BROADCASTER_LABEL], transmitter)
    transmitter.announce_senders()
    for _ in range(1000):
        button.send()
    return transmitter.low_cnt * transmitter.high_cnt


def _part2(document: list[str]) -> any:
    pass


solution = Solution(
    "Pulse Propagation",
    "20",
    "2023",
    part1=_part1,
    part2=_part2,
    part1_preprocess=_preprocess,
    part2_preprocess=_preprocess
)
