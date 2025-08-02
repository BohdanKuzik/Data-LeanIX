# Advanced LeanIX Data Analyzer

A comprehensive tool for enterprise architecture analysis, designed for Junior Data Analyst positions. This project demonstrates advanced data analysis skills, business intelligence, and technical capabilities.

## 🎯 Project Overview

This project analyzes LeanIX enterprise architecture data to provide insights into:
- **Business Analysis**: Cost analysis, application criticality, risk assessment
- **Security & Compliance**: Security scores, compliance status, vulnerability analysis
- **Performance Metrics**: Performance scores, availability, optimization opportunities
- **Data Quality**: Completeness, consistency, accuracy assessment

## 🚀 Main Features

- **Advanced Data Analysis**: Comprehensive analysis of enterprise architecture data
- **Business Intelligence**: Cost analysis, risk assessment, and KPI tracking
- **Security & Compliance Analysis**: Security scoring and compliance monitoring
- **Performance Optimization**: Performance metrics and availability analysis
- **Advanced Visualizations**: Interactive charts and correlation analysis
- **Comprehensive Reporting**: Detailed reports with actionable recommendations
- **Web Application**: Interactive Streamlit dashboard for data exploration

## 📁 Project Structure

```
Data-LeanIX/
├── main/
│   ├── leanix_analyzer.py          # Main analysis engine
│   ├── streamlit_app.py            # Interactive web application
│   ├── test.py                     # Test suite
│   └── sources/
│       ├── sample_leanix_data.xlsx     # Sample data for analysis
│       └── LeanIX_Project_Data_Real.xlsx # Original data file
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

## 🛠️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Data-LeanIX
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the analysis**:
   ```bash
   cd main
   python leanix_analyzer.py
   ```

4. **Start the web application**:
   ```bash
   streamlit run streamlit_app.py
   ```

## 📊 What the Program Analyzes

### Business Analysis
- **Application Criticality**: Distribution of critical, high, medium, and low criticality applications
- **Cost Analysis**: Maintenance costs, development costs, and total cost breakdown
- **Risk Assessment**: High-risk and critical applications identification
- **Top Expensive Applications**: Identification of the most costly applications

### Security & Compliance Analysis
- **Security Scores**: Average security scores and low-security application identification
- **Compliance Status**: Compliant vs non-compliant application distribution
- **Vulnerability Analysis**: Applications with high vulnerability counts
- **Security Trends**: Security score distribution and threshold analysis

### Performance Analysis
- **Performance Scores**: Average performance metrics and low-performance application identification
- **Availability Analysis**: Application availability percentages and downtime analysis
- **Performance Optimization**: Identification of applications needing performance improvements

### Advanced Visualizations
- **Cost Distribution**: Histograms of maintenance and development costs
- **Correlation Matrix**: Relationships between numeric indicators
- **Department Analysis**: Performance metrics by organizational department
- **Performance Comparison**: Scatter plots comparing different metrics


## 📈 Sample Output

### Console Analysis
```
🚀 RUNNING ADVANCED LEANIX DATA ANALYSIS
============================================================
📊 BASIC DATA INFORMATION
==================================================
📈 Total records: 100
📋 Total columns: 22
⚠️  Missing values: 45
🔄 Duplicate records: 0

📊 DATA QUALITY SCORE
==================================================
📈 Data completeness: 97.9%
🔄 Data consistency: 95.0%
🎯 Data accuracy: 98.0%
📊 Overall quality score: 97.0%
🎯 Quality level: Excellent

💼 BUSINESS ANALYSIS
==================================================
📊 Application criticality distribution:
   • Medium: 35 (35.0%)
   • High: 28 (28.0%)
   • Low: 22 (22.0%)
   • Critical: 15 (15.0%)

💰 Cost analysis:
   • Total maintenance costs: $1,234,567.89
   • Total development costs: $2,345,678.90
   • Total costs: $3,580,246.79
```

### Generated Files
- `cost_distribution.png` - Cost analysis visualizations
- `correlation_matrix.png` - Correlation analysis heatmap
- `department_analysis.png` - Department performance metrics
- `comprehensive_analysis_report.txt` - Detailed analysis report

## 🌐 Web Application Features

The Streamlit application provides:
- **Data Overview**: Basic metrics and data information
- **Business Analysis**: Cost analysis and criticality distribution
- **Security Analysis**: Security scores and compliance status
- **Performance Analysis**: Performance metrics and availability
- **Advanced Visualization**: Interactive charts and comparisons
- **Comprehensive Reports**: Downloadable analysis reports

## 🎯 Why This Fits Junior Roles

### Demonstrates Growth
- **Progressive Complexity**: Shows ability to handle complex data analysis
- **Technical Skills**: Demonstrates Python, data analysis, and visualization skills
- **Business Understanding**: Shows ability to translate data into business insights

### Comprehensive Approach
- **End-to-End Solution**: Complete analysis pipeline from data loading to reporting
- **Multiple Technologies**: Uses various libraries and frameworks
- **Professional Output**: Generates professional-quality reports and visualizations

### Interview-Ready
- **Clear Documentation**: Well-documented code and comprehensive README
- **Test Coverage**: Includes test suite for validation
- **Real-World Application**: Addresses actual business problems

## 🔧 How to Adapt for Your Needs

### Customize Analysis
```python
# Add new business metrics
def custom_business_analysis(self):
    # Your custom analysis logic
    pass

# Modify visualization types
def create_custom_charts(self):
    # Your custom visualizations
    pass
```

### Extend Data Sources
```python
# Support additional file formats
def load_data(self):
    if self.file_path.endswith('.csv'):
        self.df = pd.read_csv(self.file_path)
    elif self.file_path.endswith('.xlsx'):
        self.df = pd.read_excel(self.file_path)
```

### Add New Metrics
```python
# Calculate custom KPIs
def calculate_custom_kpis(self):
    # Your custom KPI calculations
    pass
```

## 📋 Requirements

- Python 3.8+
- pandas==2.3.1
- openpyxl==3.1.5
- matplotlib==3.10.5
- streamlit==1.47.1
- numpy==2.3.2
- seaborn==0.13.2

## 🚀 Quick Start

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run analysis**:
   ```bash
   cd main
   python leanix_analyzer.py
   ```

3. **Start web app**:
   ```bash
   streamlit run streamlit_app.py
   ```

4. **Run tests**:
   ```bash
   python test.py
   ```

## 📞 Support

For questions or issues, please refer to the code comments and documentation within each file. The project is designed to be self-explanatory and well-documented for interview presentations.

---

**Created for Data Analyst Interview Preparation**  
*Demonstrating advanced data analysis, business intelligence, and technical skills* 