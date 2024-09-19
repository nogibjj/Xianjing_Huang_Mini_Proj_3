from main import read_data, generate_summary_statistics, draw_histogram
from main import draw_pie_chart, generate_PDF, main
import pandas as pd


def test_read_data():
    df = read_data("olympics2024.csv")
    assert isinstance(df, pd.DataFrame), "Failed to read CSV dataset"


def test_generate_summary_statistics():
    df = read_data("olympics2024.csv")
    cols = ["Gold", "Silver", "Bronze", "Total"]
    for col in cols:
        mean, median, std = generate_summary_statistics(df, col)
        assert mean is not None
        assert median is not None
        assert std is not None


def test_draw_histogram():
    df = read_data("olympics2024.csv")
    res = draw_histogram(df)
    assert res is None


def test_draw_pie_chart():
    df = read_data("olympics2024.csv")
    res = draw_pie_chart(df)
    assert res is None


def test_generate_PDF():
    df = read_data("olympics2024.csv")
    cols = ["Gold", "Silver", "Bronze", "Total"]
    stored_stat = []
    for col in cols:
        mean, median, std = generate_summary_statistics(df, col)
        stored_stat.append([mean, median, std])

    res = generate_PDF(stored_stat)
    assert res is None


def test_main():
    res = main()
    assert res is None


if __name__ == "__main__":
    test_read_data()
    test_generate_summary_statistics()
    test_draw_pie_chart()
    test_generate_PDF()
    test_main()
