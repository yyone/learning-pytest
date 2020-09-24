import pytest
import tasks
from tasks import Task


# parametrizeを使って同じテスト内容に書き換える
@pytest.mark.parametrize("tasks_in_db, expected",
    [
        pytest.param(
            [Task("起きる", "yattom")],
            "起きる",
            id="1件だけの場合"
        ),
        pytest.param(
            [
                Task("起きる", "yattom"),
                Task("食べる", "yattom"),
                Task("寝る", "yattom")
            ],
            "起きる",
            id="複数件の場合"
        ),
        pytest.param(
            [
                Task("起きる", "yattom", True),
                Task("食べる", "yattom"),
                Task("寝る", "yattom")
            ],
            "食べる",
            id="終了タスクは無視する"
        ),
    ])


def test_get_most_urgent(tasks_db, tasks_in_db, expected):
    for t in tasks_in_db:
        tasks.add(t)
    urgent_task = tasks.get_most_urgent()
    assert urgent_task.summary == expected


def test_get_most_urgent_when_none(tasks_db):
    urgent_task = tasks.get_most_urgent()
    assert urgent_task is None
