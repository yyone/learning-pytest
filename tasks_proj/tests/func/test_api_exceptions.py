import pytest
import tasks

@pytest.mark.smoke
def test_list_tasks_raises():
    """
    list_tasks() should raise an exception with wrong type param.
    """
    with pytest.raises(TypeError):
        tasks.list_tasks(owner=123)

@pytest.mark.get
@pytest.mark.smoke
def test_get_raises():
    """
    get() should raise an exception with wrong type param.
    """
    with pytest.raises(TypeError):
        tasks.get(task_id="123")

class TestUpdate():
    """
    Test expected exceptions with tasks.update().
    """

    def test_bad_id(self):
        """
        A non-int id should raises an exceptions.
        """
        with pytest.raises(TypeError):
            tasks.update(task_id={"dict insted": 1},
                         task=tasks.Task())

    def test_bad_task(self):
        """
        A non-Task task should raise an exception.
        """
        with pytest.raises(TypeError):
            tasks.update(tasks_id=1, task="not a task")
