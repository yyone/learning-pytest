import pytest
import tasks
from tasks import Task

def test_add_returns_valid_id(tasks_db):
    """
    tasks.add(<vaild task>) should return an integer.
    """
    # GIVEN an initialized db
    # WHEN a new task is added
    # THEN returned task_id is of type int
    new_task = Task("do something")
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)

def test_added_task_has_id_set(tasks_db):
    """
    Make sure the task_id field is set by tasks.add().
    """
    # GIVEN an initialized tasks db
    #  AND a new task is added
    new_task = Task("sit in chair", owner="me", done=True)
    task_id = tasks.add(new_task)

    # WHEN task is retrieved
    task_from_db = tasks.get(task_id)

    # THEN task_id matched id field
    assert task_from_db.id == task_id

def test_add_increases_count(db_with_3_tasks):
    """
    Test tasks.add() affect on tasks.count().
    """
    tasks.add(Task("throw a party"))

    # countの値が増える
    assert tasks.count() == 4
