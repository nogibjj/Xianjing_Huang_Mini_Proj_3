import polars as pl
import matplotlib.pyplot as plt
from fpdf import FPDF


def read_data(file):
    """read .csv dataset by polars"""
    return pl.read_csv(file)

df = read_data("Salary_dataset.csv")

def generate_summary_statistics(df):
    return df.describe()

print(generate_summary_statistics(df))

def compute_summary_statistics(df):
    """compute mean, median, standard deviation"""
    col_len = df.shape[1]

    for i in range(1, col_len):
        name = df.columns[i]
        mean = df[name].mean()
        print(f"Mean of {name}: {mean:.2f}")
    print("-------------")
    for i in range(1, col_len):
        name = df.columns[i]
        median = df[name].median()
        print(f"Median of {name}: {median:.2f}")
    print("-------------")
    for i in range(1, col_len):
        name = df.columns[i]
        std = df[name].std()
        print(f"Standard Deviation of {name}: {std:.2f}")
    print("-------------")
    return

compute_summary_statistics(df)

def draw_scatter_line_plot(df):
    """create scatter_line_plot for df and save fig"""
    plt.figure(figsize=(8, 6))
    plt.scatter(df['YearsExperience'], df['Salary'], color='blue', label='Data Points')
    plt.plot(df['YearsExperience'], df['Salary'], color='orange', label='Trend Line')
    plt.title('Years of Experience vs Salary')
    plt.xlabel('Years of Experience')
    plt.ylabel('Salary')
    plt.grid(True)
    plt.legend()
    # plt.show()
    plt.savefig("scatter_line_plot.png")

draw_scatter_line_plot(df)

def generate_PDF(df):
    """create PDF and save"""
    pdf = FPDF()
    pdf.add_page()
    # add title
    pdf.set_font("Arial", "B", 16)
    title = "Report " "for Salary Dataset Simple Linear Regression"
    pdf.cell(200, 10, txt=title, ln=True, align="C")

    pdf.ln(10)

    # part1: dataset introduction
    pdf.set_font("Arial", "B", 14)
    title_part1 = "1. Dataset Introduction"
    pdf.cell(200, 10, txt=title_part1, ln=True, align="L")
    pdf.set_font("Arial", "", 10)
    content_part1 = (
        "Salary Dataset in CSV for Simple linear regression. \n"
        "Columns: \n"
        "# \n"
        "YearsExperience \n"
        "Salary \n" 
        "Data source: "
    )
    pdf.multi_cell(0, 10, txt=content_part1)
    x = pdf.get_x()
    y = pdf.get_y()
    pdf.set_y(y - 10)
    pdf.set_x(x + 22)
    #     pdf.cell(200, 10, txt=content_part1, ln=0, align="L")
    pdf.set_text_color(0, 0, 255)
    pdf.set_font("Arial", "I", 10)
    link_txt = "https://www.kaggle.com/datasets/abhishek14398/salary-dataset-simple-linear-regression/data"
    pdf.cell(
        200,
        10,
        txt=link_txt,
        ln=True,
        align="L",
        link="https://www.kaggle.com/datasets/abhishek14398/salary-dataset-simple-linear-regression/data",
    )
    
    pdf.ln(10)

    # part2: descriptive statistics
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", "B", 14)
    title_part2 = "2. Descriptive Statistics"
    pdf.cell(200, 10, txt=title_part2, ln=True, align="L")
    pdf.set_font("Arial", "", 10)
    x = pdf.get_x()
    y = pdf.get_y()
    pdf.image("describe.png", x=x, y=y, w=190)

    pdf.ln(10)

    # part3: data visualization
    pdf.add_page()
    pdf.set_font("Arial", "B", 14)
    title_part3 = "3. Data Visualization"
    pdf.cell(200, 10, txt=title_part3, ln=1, align="L")
    x = pdf.get_x()
    y = pdf.get_y()
    pdf.image("scatter_line_plot.png", x=x, y=y, w=190)

    # save PDF
    pdf.output("report.pdf", "F")

generate_PDF(df)