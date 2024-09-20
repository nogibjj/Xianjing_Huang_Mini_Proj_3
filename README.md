# Xianjing_Huang_Mini_Proj_3
[![Lint](https://github.com/nogibjj/Xianjing_Huang_Mini_Proj_3/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/Xianjing_Huang_Mini_Proj_3/actions/workflows/lint.yml)
[![Install](https://github.com/nogibjj/Xianjing_Huang_Mini_Proj_3/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/Xianjing_Huang_Mini_Proj_3/actions/workflows/install.yml)
[![Format](https://github.com/nogibjj/Xianjing_Huang_Mini_Proj_3/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/Xianjing_Huang_Mini_Proj_3/actions/workflows/format.yml)
[![Test](https://github.com/nogibjj/Xianjing_Huang_Mini_Proj_3/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/Xianjing_Huang_Mini_Proj_3/actions/workflows/test.yml)

### Directory Tree Structure
```
Xianjing_Huang_Mini_Proj_3/
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
├── describe.png
├── main.py
├── Makefile
├── README.md
├── report.pdf
├── requirements.txt
├── Salary_dataset.csv
├── scatter_line_plot.png
└── test_main.py
```

### Requirements
* Python script using Polars for descriptive statistics
* Read a dataset (CSV or Excel)
* Generate summary statistics (mean, median, standard deviation)
* Create at least one data visualization

### Polars vs Pandas
* Polars generally outperforms Pandas in terms of speed, especially for large datasets. This is because Polars is designed for parallelized execution and is optimized for in-memory performance.
* Pandas may still be more familiar or convenient for certain smaller tasks or when using legacy systems that require it.


### Preparation
1. Open codespaces
2. Wait for container to be built and pinned requirements from `requirements.txt` to be installed
3. If running locally, `git clone` the repository and use `make install`
![0](/imgs/000.png)

### Check format and test errors
1. Format code `make format`
![1](/imgs/001.png)
2. Lint code `make lint`
![2](/imgs/002.png)
3. Test code `make test`
![3](/imgs/003.png)

### Descriptive Statistics
![4](/imgs/004.png)

### Visualization
![6](/scatter_line_plot.png)

### Report
Generated summary report (PDF) via CI/CD for extra credit.
![5](/imgs/005.png)
You can find it here [Report](/report.pdf)


