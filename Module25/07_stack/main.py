class Stack:

    def __init__(self):
        self.__stack_list = []

    def __str__(self):
        return '; '.join(self.__stack_list)

    def adding(self, elem):
        self.__stack_list.append(elem)

    # def deletion(self):
    #     if len(self.__stack_list) == 0:
    #         return None
    #     return self.__stack_list.pop()


class TaskManager:

    def __init__(self):
        self.task = dict()

    def __str__(self):
        info = []
        if self.task:
            for i_key, i_value in sorted(self.task.items()):
                info.append(f'{i_key}   {i_value}\n')
        return ''.join(info)

    def new_task(self, action, priority):
        if priority not in self.task:
            self.task[priority] = Stack()
        self.task[priority].adding(action)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
