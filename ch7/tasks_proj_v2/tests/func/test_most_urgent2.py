import pytest
import tasks
from tasks import Task


@pytest.fixture
def タスク1つ(tasks_db):
    tasks.add(Task("起きる", "yattom"))


@pytest.fixture
def タスク3つ(tasks_db):
    tasks.add(Task("起きる", "yattom"))
    tasks.add(Task("食べる", "yattom"))
    tasks.add(Task("寝る", "yattom"))


@pytest.fixture
def タスクを1つ終了(tasks_db):
    t = tasks.list_tasks()[0]
    done = t._replace(done=True)
    tasks.update(done.id, done)


@pytest.fixture
def タスクをすべて終了(tasks_db):
    for t in tasks.list_tasks():
        done = t._replace(done=True)
        tasks.update(done.id, done)


@pytest.mark.usefixtures("tasks_db")
class TestGetMostUrgent:
    class Testタスクがない:
        def test_1件もない(self):
            urgent_task = tasks.get_most_urgent()
            assert urgent_task is None


    class Testタスクが1つ:
        @pytest.mark.usefixtures("タスク1つ")
        def test_終了していない(self):
            urgent_task = tasks.get_most_urgent()
            assert urgent_task.summary == "起きる"


        @pytest.mark.usefixtures("タスク1つ", "タスクをすべて終了")
        def test_終了している(self):
            urgent_task = tasks.get_most_urgent()
            assert urgent_task is None


    class Testタスクが3つ:
        @pytest.mark.usefixtures("タスク3つ")
        def test_終了していない(self):
            urgent_task = tasks.get_most_urgent()
            assert urgent_task.summary == "起きる"


        @pytest.mark.usefixtures("タスク3つ", "タスクを1つ終了")
        def test_1件終了している(self):
            urgent_task = tasks.get_most_urgent()
            assert urgent_task.summary == "食べる"


        @pytest.mark.usefixtures("タスク3つ", "タスクをすべて終了")
        def test_すべて終了している(self):
            urgent_task = tasks.get_most_urgent()
            assert urgent_task is None
