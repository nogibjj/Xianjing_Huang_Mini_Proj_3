import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF


def read_data(file):
    """read .csv dataset by pandas"""
    return pd.read_csv(file)


def generate_summary_statistics(df, col):
    """compute mean, median, standard deviation"""
    mean = df[col].mean()
    median = df[col].median()
    std = df[col].std()

    return mean, median, std


def draw_histogram(df):
    """create histogram for df and save fig"""
    plt.figure(figsize=(13, 6))
    plt.bar(df["Country"], df["Gold"], label="Gold", alpha=0.7, color="gold")
    plt.bar(
        df["Country"],
        df["Silver"],
        label="Silver",
        alpha=0.7,
        bottom=df["Gold"],
        color="silver",
    )
    plt.bar(
        df["Country"],
        df["Bronze"],
        label="Bronze",
        alpha=0.7,
        bottom=[i + j for i, j in zip(df["Gold"], df["Silver"])],
        color="brown",
    )
    plt.title("Paris 2024 Olympics Medals by Country--top 10")
    plt.xlabel("Country")
    plt.ylabel("Number of Medals")
    plt.legend()
    plt.savefig("medals_histogram_plot.png")


#     plt.show()


def draw_pie_chart(df):
    """create pie chart for df and save fig"""
    plt.figure(figsize=(8, 8))
    plt.pie(df["Total"], labels=df["Country"], autopct="%1.1f%%", startangle=140)
    plt.title("Total Medals Distribution")
    plt.savefig("medals_pie_chart_plot.png")


#     plt.show()


def generate_PDF(stored_stat):
    """create PDF and save"""
    pdf = FPDF()
    pdf.add_page()
    # add title
    pdf.set_font("Arial", "B", 16)
    title = "Report " "for Paris 2024 Olympics Medals by Country--top 10"
    pdf.cell(200, 10, txt=title, ln=True, align="C")

    pdf.ln(10)

    # part1: dataset introduction
    pdf.set_font("Arial", "B", 14)
    title_part1 = "1. Dataset Introduction"
    pdf.cell(200, 10, txt=title_part1, ln=True, align="L")
    pdf.set_font("Arial", "", 10)
    content_part1 = (
        "The 2024 Summer Olympics, officially the Games of the XXXIII Olympiad"
        " and branded as Paris 2024, were an international multi-sport event"
        " that occurred from 26 July to 11 August 2024 in France, "
        "with the opening ceremony having taken place on 26 July. "
        "The dataset used selected the top 10 countries in the medal "
        "table and their gold, silver, "
        "bronze, and total medal counts. \n"
        "Data source: "
    )
    pdf.multi_cell(0, 10, txt=content_part1)
    x = pdf.get_x()
    y = pdf.get_y()
    pdf.set_y(y - 10)
    pdf.set_x(x + 30)
    #     pdf.cell(200, 10, txt=content_part1, ln=0, align="L")
    pdf.set_text_color(0, 0, 255)
    pdf.set_font("Arial", "I", 10)
    link_txt = "https://olympics.com/en/paris-2024/medals"
    pdf.cell(
        200,
        10,
        txt=link_txt,
        ln=True,
        align="L",
        link="https://olympics.com/en/paris-2024/medals",
    )
    x = pdf.get_x()
    y = pdf.get_y()
    pdf.image("data_intro.png", x=x + 30, y=y, h=100)

    pdf.ln(110)

    # part2: descriptive statistics
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", "B", 14)
    title_part2 = "2. Descriptive Statistics"
    pdf.cell(200, 10, txt=title_part2, ln=True, align="L")
    pdf.set_font("Arial", "", 10)
    content_part2 = (
        f"Mean of Gold: {stored_stat[0][0]:.2f}   "
        f"Median of Gold: {stored_stat[0][1]:.2f}   "
        f"Standard Deviation of Gold: {stored_stat[0][2]:.2f} \n"
        f"Mean of Silver: {stored_stat[1][0]:.2f}   "
        f"Median of Silver: {stored_stat[1][1]:.2f}   "
        f"Standard Deviation of Silver: {stored_stat[1][2]:.2f} \n"
        f"Mean of Bronze: {stored_stat[2][0]:.2f}   "
        f"Median of Bronze: {stored_stat[2][1]:.2f}   "
        f"Standard Deviation of Bronze: {stored_stat[2][2]:.2f} \n"
        f"Mean of Total: {stored_stat[3][0]:.2f}   "
        f"Median of Total: {stored_stat[3][1]:.2f}   "
        f"Standard Deviation of Total: {stored_stat[3][2]:.2f} \n"
    )
    pdf.multi_cell(200, 10, txt=content_part2)

    pdf.ln(10)

    # part3: data visualization
    pdf.add_page()
    pdf.set_font("Arial", "B", 14)
    title_part3 = "3. Data Visualization"
    pdf.cell(200, 10, txt=title_part3, ln=True, align="L")
    # add histogram
    pdf.set_font("Arial", "B", 12)
    pdf.cell(40, 10, "a. Medals by Country  [histogram]", ln=1)
    x = pdf.get_x()
    y = pdf.get_y()
    pdf.image("medals_histogram_plot.png", x=x, y=y, w=190)
    pdf.ln(90)
    # add Pie Chart
    pdf.cell(40, 10, "b. Total Medals Distribution  [pie chart]", ln=1)
    x = pdf.get_x()
    y = pdf.get_y()
    pdf.image("medals_pie_chart_plot.png", x=x + 20, y=y, w=140)

    # save PDF
    pdf.output("report.pdf")


def main():
    df = read_data("olympics2024.csv")
    cols = ["Gold", "Silver", "Bronze", "Total"]
    stored_stat = []
    for col in cols:
        mean, median, std = generate_summary_statistics(df, col)
        print(f"Mean of {col}: {mean:.2f}")
        print(f"Median of {col}: {median:.2f}")
        print(f"Standard Deviation of {col}: {std:.2f}")
        stored_stat.append([mean, median, std])
        print("-----------")

    draw_histogram(df)
    draw_pie_chart(df)
    generate_PDF(stored_stat)


# if __name__ == "__main__":
#     main()
