class Sequence:

    def __init__(self, Q_list):
        self.Q_list = Q_list

    def __iter__(self):
        return self

    def __next__(self):
        Q = self.Q_list[-self.Q_list[-1]] + self.Q_list[-self.Q_list[-2]]
        self.Q_list.append(Q)
        return Q

    def current_state(self):
        return self.Q_list


Q_sequence = Sequence([1, 1])
[next(Q_sequence) for _ in range(10)]
print(Q_sequence.current_state())

