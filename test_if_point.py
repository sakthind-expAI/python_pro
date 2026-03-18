import io
import sys

import pytest

from python_learnings import if_check, Point, where_is


def capture_stdout(fn, *args, **kwargs):
    """Helper to capture stdout output from a function call."""
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        fn(*args, **kwargs)
        return sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout


@pytest.mark.parametrize(
    "user_input, expected",
    [
        ("-5", "Negative changed to zero"),
        ("0", "Zero"),
        ("1", "Single"),
        ("42", "More"),
    ],
)
def test_if_check_outputs(monkeypatch, user_input, expected):
    """if_check() should print the correct message based on input."""
    monkeypatch.setattr("builtins.input", lambda prompt="": user_input)
    output = capture_stdout(if_check)
    assert expected in output


@pytest.mark.parametrize(
    "point, expected",
    [
        (Point(0, 0), "Origin"),
        (Point(0, 5), "Y=5"),
        (Point(7, 0), "X=7"),
        (Point(2, 3), "Somewhere else"),
    ],
)
def test_where_is_point_matches(point, expected):
    output = capture_stdout(where_is, point)
    assert expected in output


def test_func_var_and_for_loop_output():
    """func_var() and for_loop() should run and print their expected content."""
    from python_learnings import func_var, for_loop

    out1 = capture_stdout(func_var)
    assert "Hello, World!" in out1
    assert "Casting:" in out1

    out2 = capture_stdout(for_loop)
    assert "car" in out2
    assert "plane" in out2


def test_read_excel_data_writes_file(tmp_path, monkeypatch):
    """Read_excel_data should read a CSV and write extracted_data.csv."""
    from python_learnings import Read_excel_data

    csv_content = "Id,Status,Severity,State\n1,Open,Critical,NY\n2,Closed,Low,CA\n"
    csv_path = tmp_path / "data.csv"
    csv_path.write_text(csv_content, encoding="utf-8")

    monkeypatch.chdir(tmp_path)
    Read_excel_data(str(csv_path))

    output_file = tmp_path / "extracted_data.csv"
    assert output_file.exists()
    written = output_file.read_text(encoding="utf-8")

    # Verify that the "Critical" severity row is preserved in the output.
    assert "Critical" in written
    assert "Low" in written

#python -m pytest test_if_point.py -vv
#python -m pytest test_if_point.py -vv -s