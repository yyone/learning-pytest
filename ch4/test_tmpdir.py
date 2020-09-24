def test_tmpdir(tmpdir):
    # tmpdirにはパス名がすでに関連づけられている
    # join()はファイル名を含むようにパスを拡張する
    # ファイルは書き込み時に作成される
    a_file = tmpdir.join("something.txt")

    # ディレクトリを作成する
    a_sub_dir = tmpdir.mkdir("anything")

    # ディレクトリにファイルを作成する
    another_file = a_sub_dir.join("something_else.txt")

    # このコードによりsomething.txtが作成される
    a_file.write("contents may settle during shipping")

    # この書き込みにより、"anything/something_else.txt"が作成される
    another_file.write("something different")

    # ファイルの読み込み
    assert a_file.read() == "contents may settle during shipping"
    assert another_file.read() == "something different"

def test_tmpdir_factory(tmpdir_factory):
    # まず、ディレクトリを作成すべき
    # a_dirはtmpdir fixtureから返されたobjectのように動作する
    a_dir = tmpdir_factory.mktemp("mydir")

    # base_tempは"mydir"の親ディレクトリ
    # getbasetemp()は本来ここで使う必要はない
    # この関数が利用可能であることを示すために使っている
    base_temp = tmpdir_factory.getbasetemp()
    print("base:", base_temp)

    # 以下、tmpdirとほぼ同じ
    a_file = a_dir.join("something.txt")
    a_sub_dir = a_dir.mkdir("anything")
    another_file = a_sub_dir.join("something_else.txt")

    a_file.write("contents may settle during shipping")
    another_file.write("something different")

    assert a_file.read() == "contents may settle during shipping"
    assert another_file.read() == "something different"
