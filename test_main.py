from main import read_data, generate_summary_statistics, compute_summary_statistics
from main import draw_scatter_line_plot, generate_PDF, read_data_pd
from pyinstrument import Profiler
import polars as pl
import pandas as pd


def test_read_data():
    df = read_data("Salary_dataset.csv")
    assert isinstance(df, pl.DataFrame), "Failed to read CSV dataset"


def test_read_data_pd():
    df = read_data_pd("Salary_dataset.csv")
    assert isinstance(df, pd.DataFrame), "Failed to read CSV dataset"


def test_generate_summary_statistics():
    df = read_data("Salary_dataset.csv")
    res = generate_summary_statistics(df)
    assert res is not None


def test_compute_summary_statistics():
    df = read_data("Salary_dataset.csv")
    res = compute_summary_statistics(df)
    assert res is None


def test_draw_scatter_line_plot():
    df = read_data("Salary_dataset.csv")
    res = draw_scatter_line_plot(df)
    assert res is None


def test_generate_PDF():
    df = read_data("Salary_dataset.csv")
    res = generate_PDF(df)
    assert res is None


if __name__ == "__main__":
    test_read_data()
    test_generate_summary_statistics()
    test_compute_summary_statistics()
    test_draw_scatter_line_plot()
    test_generate_PDF()
    with Profiler(interval=0.1) as profiler:
        df = read_data("Salary_dataset.csv")
        print(df.shape)
        print(df.describe())
    profiler.print()
    with Profiler(interval=0.1) as profiler:
        df = read_data_pd("Salary_dataset.csv")
        print(df.shape)
        print(df.describe())
    profiler.print()
