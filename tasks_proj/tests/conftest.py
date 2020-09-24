import pytest
import tasks
from tasks import Task

@pytest.fixture(scope="module")
def author_file_json(tmpdir_factory):
    """
    Write some authors to a data file.
    """
    python_author_data = {
        "Ned": {"City": "Boston"},
        "Brian": {"City": "Portland"},
        "Luciano": {"City": "San Paulo"}
    }

    file = tmpdir_factory.mktemp("data").join("author_file.json")
    print("file:{}".format(str(file)))

    with file.open("w") as f:
        json.dump(python_author_data, f)
    return file

@pytest.fixture(scope="session")
def tasks_db_session(tmpdir_factory):
    """
    Connect to db before tests, disconnect after.
    """
    # セットアップ：DBへ接続
    temp_dir = tmpdir_factory.mktemp("temp")
    tasks.start_tasks_db(str(temp_dir), "tiny")

    # ここでテストを実行
    yield

    # ティアダウン：DBの接続を終了
    tasks.stop_tasks_db()

@pytest.fixture()
def tasks_db(tasks_db_session):
    """
    An empty tasks db.
    """
    tasks.delete_all()

# Taskコンストラクタのインターフェースについて
# Task(summary=None, owner=None, done=False, id=None)
# summaryは必須パラメータ
# ownerとdoneはオプション
# idはデータベースによって設定

@pytest.fixture(scope="session")
def tasks_just_a_few():
    """
    All summaries and owners are unique.
    """
    return(
        Task("white some code", "Brian", True),
        Task("Code review Brian's code", "Katie", False),
        Task("Fix what Brian did", "Michelle", False)
    )

@pytest.fixture(scope="session")
def tasks_mult_per_owner():
    """
    Several owners with several tasks each.
    """
    return(
        Task("Make a cookie", "Raphael"),
        Task("Use an emoji", "Raphael"),
        Task("Move to Berlin", "Raphael"),

        Task("Create", "Michelle"),
        Task("inspire", "Michelle"),
        Task("Encourage", "Michelle"),

        Task("Do a handstand", "Daniel"),
        Task("White some books", "Daniel"),
        Task("Eat ice cream", "Daniel")
    )

@pytest.fixture()
def db_with_3_tasks(tasks_db, tasks_just_a_few):
    """
    Connected db with 3 tasks, all unique.
    """
    for t in tasks_just_a_few:
        tasks.add(t)

@pytest.fixture()
def db_with_multi_per_owner(tasks_db, tasks_mult_per_owner):
    """
    Connected db with 9 tasks, 3 owners, all with 3 tasks.
    """
    for t in tasks_mult_per_owner:
        tasks.add(t)
