import pytest
import tasks
from tasks import Task


@pytest.mark.usefixtures("tasks_db")
class TestAdd():
    """
    Test related to tasks.add().
    """

    def test_missing_summary(self):
        """
        Should raise an exception if summary missing.
        """
        with pytest.raises(ValueError):
            tasks.add(Task(owner="bob"))
    
    def test_done_not_bool(self):
        """
        Should raise an exception if done is not a bool.
        """
        with pytest.raises(ValueError):
            tasks.add(Task(summary="summary", done="True"))
