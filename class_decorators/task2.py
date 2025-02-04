class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    def add_worker(self, worker):
        if not isinstance(worker, Worker):
            raise ValueError("Only instances of Worker can be added.")
        if worker not in self._workers:
            self._workers.append(worker)

    @property
    def workers(self):
        return self._workers


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None
        self.boss = boss  # Setter is used here

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if not isinstance(new_boss, Boss):
            raise ValueError("Boss must be an instance of Boss class.")
        if self._boss is not None:
            self._boss.workers.remove(self)
        self._boss = new_boss
        new_boss.add_worker(self)
    