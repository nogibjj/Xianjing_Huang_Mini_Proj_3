# Xianjing_Huang_Mini_Proj_2
[![Lint](https://github.com/Remi12138/Xianjing_Huang_Mini_Proj_2/actions/workflows/lint.yml/badge.svg)](https://github.com/Remi12138/Xianjing_Huang_Mini_Proj_2/actions/workflows/lint.yml)
[![Format](https://github.com/Remi12138/Xianjing_Huang_Mini_Proj_2/actions/workflows/format.yml/badge.svg)](https://github.com/Remi12138/Xianjing_Huang_Mini_Proj_2/actions/workflows/format.yml)
[![Install](https://github.com/Remi12138/Xianjing_Huang_Mini_Proj_2/actions/workflows/install.yml/badge.svg)](https://github.com/Remi12138/Xianjing_Huang_Mini_Proj_2/actions/workflows/install.yml)
[![Test](https://github.com/Remi12138/Xianjing_Huang_Mini_Proj_2/actions/workflows/test.yml/badge.svg)](https://github.com/Remi12138/Xianjing_Huang_Mini_Proj_2/actions/workflows/test.yml)

### Directory Tree Structure
```
Xianjing_Huang_Mini_Proj_2/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/
│   └── workflows/
│       ├── format.yml
│       ├── install.yml
│       ├── lint.yml
│       └── test.yml
├── imgs/
├── .gitignore
├── data_intro.png
├── main.py
├── Makefile
├── medals_histogram_plot.png
├── medals_pie_chart_plot.png
├── olympics2024.csv
├── README.md
├── repport.pdf
├── requirements.txt
└── test_main.py
```

### Requirements
* Python script using Polars for descriptive statistics
* Read a dataset (CSV or Excel)
* Generate summary statistics (mean, median, standard deviation)
* Create at least one data visualization

### Preparation
1. Open codespaces
2. Wait for container to be built and pinned requirements from `requirements.txt` to be installed
3. If running locally, `git clone` the repository and use `make install`
![1](/imgs/001.png)

### Check format and test errors
1. Format code `make format`
![3](/imgs/003.png)
2. Lint code `make lint`
![4](/imgs/004.png)
3. Test code `make test`
![2](/imgs/002.png)

### Descriptive Statistics
![0](/imgs/000.png)

### Visualization
1. Histogram
![5](/medals_histogram_plot.png)
2. Pie Chart
![6](/medals_pie_chart_plot.png)

### Report
Generated summary report (PDF) via CI/CD for extra credit.
![7](/imgs/005.png)
You can find it here [Report](/report.pdf)


