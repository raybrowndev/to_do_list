# File: lib/todo_list.py
class TodoList:
    def __init__(self):
        self._all_things = []

    def add(self, todo):
        for existing_todo in self._all_things:
            if existing_todo.task == todo.task:
                raise Exception("task already added")
        self._all_things.append(todo)
        
        
    def incomplete(self):
        incomplete = []
        for item in self._all_things:
            if item.complete == False:
                incomplete.append(item.task)
        return incomplete



    def complete(self):
        complete = []
        for item in self._all_things:
            if item.complete == True:
                complete.append(item.task)
        return complete

    def update(self):
        completed_tasks = [item for item in self.complete()]
        incomplete_tasks = [str(item) for item in self.incomplete()]
        deli = ", "
        

        return f"Task Complete: {completed_tasks} > Task Remaining: {incomplete_tasks}"



    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        pass

