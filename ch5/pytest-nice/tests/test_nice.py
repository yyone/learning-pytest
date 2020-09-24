import pytest


def test_pass_fail(testdir):

    # 一次的に使用するpytestテストモジュールを作成
    testdir.makepyfile("""
        def test_pass():
            assert 1 == 1
        def test_fail():
            assert 1 == 2
    """)

    # pytestを実行
    result = testdir.runpytest()

    # fnmatch_linesは内部でアサーションを実行
    result.stdout.fnmatch_lines(["*.F*",])  # .は成功を表し、Fは失敗を表す

    # テストスイートの終了コードが「1」であることを確認
    assert result.ret == 1


@pytest.fixture()
def sample_test(testdir):
    testdir.makepyfile("""
        def test_pass():
            assert 1 == 1
        def test_fail():
            assert 1 == 2
    """)
    return testdir


def test_with_nice(sample_test):
    result = sample_test.runpytest("--nice")
    result.stdout.fnmatch_lines(["*.O*",])  # .は成功を表し、Fは失敗を表す
    assert result.ret == 1


def test_with_nice_verbose(sample_test):
    result = sample_test.runpytest("-v", "--nice")
    result.stdout.fnmatch_lines([
        "*::test_fail OPPORTUNITY for improvement*",
    ])
    assert result.ret == 1


def test_not_nice_verbose(sample_test):
    result = sample_test.runpytest("-v")
    result.stdout.fnmatch_lines(["*::test_fail FAILED*"])
    assert result.ret == 1


def test_header(sample_test):
    result = sample_test.runpytest("--nice")
    result.stdout.fnmatch_lines(["Thanks for running the tests."])


def test_header_not_nice(sample_test):
    result = sample_test.runpytest()
    thanks_message = "Thanks for running the tests."
    assert thanks_message not in result.stdout.str()


def test_help_message(testdir):
    result = testdir.runpytest("--help")

    # fnmatch_linesは内部でアサーションを実行
    result.stdout.fnmatch_lines([
        "nice:",
#        "*--nice*nice: turn FAILED into OPPORTUNITY for improvement",
        "*--nice*nice: turn failures into opportunities",  # pytest.addoption()で追加したメッセージ
    ])
