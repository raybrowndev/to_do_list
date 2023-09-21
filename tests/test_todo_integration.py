from lib.todo_list import *
from lib.todo import *
import pytest 

def test_add_todo():
    errand = Todo("walk the dog")
    thing = TodoList()
    thing.add(errand)
    result = thing.incomplete()

    assert result == ["walk the dog"]

def test_add_multiple_and_return_incomplete_list():
    errand1 = Todo("walk the dog")
    errand2 = Todo("do laundry")
    errand3 = Todo("buy milk")

    thing = TodoList()

    thing.add(errand1)
    thing.add(errand2)
    thing.add(errand3)
    result = thing.incomplete()

    assert result == ["walk the dog", "do laundry", "buy milk"]


def test_return_completed_tasks():
    #return all tasks compete
    #and number of tasks remaining
    errand1 = Todo("walk the dog")
    errand2 = Todo("do laundry")
    errand3 = Todo("buy milk")

    thing = TodoList()

    thing.add(errand1)
    thing.add(errand2)
    thing.add(errand3)
    errand1.mark_complete()
    result = thing.complete()

    assert result == ["walk the dog"]

def test_return_complete_and_remaining():
    #mark as complete
    #return list of complete 
    #return list of remianing 
    errand1 = Todo("walk the dog") #complete
    errand2 = Todo("do laundry") 
    errand3 = Todo("buy milk")
    errand4 = Todo("visit the doctor") #complete

    thing = TodoList()

    thing.add(errand1)
    thing.add(errand2)
    thing.add(errand3)
    thing.add(errand4)

    errand1.mark_complete()
    errand4.mark_complete()
    assert thing.update() == "Task Complete: ['walk the dog', 'visit the doctor'] > Task Remaining: ['do laundry', 'buy milk']"

#Edge Cases
def test_add_to_do_already_added():
    errand1 = Todo("walk the dog")
    errand3 = Todo("walk the dog")

    thing = TodoList()

    thing.add(errand1)
    with pytest.raises(Exception) as e:
        thing.add(errand3)
    alert = str(e.value)
    assert alert == "task already added"

def test_return_list_no_todo():
    thing = TodoList()
    result = thing.incomplete()

    assert result == []

