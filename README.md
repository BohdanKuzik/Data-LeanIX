# Data Analyzer

A comprehensive tool for enterprise architecture analysis.

## Project Overview

This project analyzes LeanIX enterprise architecture data to provide insights into:
- **Business Analysis**: Cost analysis, application criticality, risk assessment
- **Security & Compliance**: Security scores, compliance status, vulnerability analysis
- **Performance Metrics**: Performance scores, availability, optimization opportunities
- **Data Quality**: Completeness, consistency, accuracy assessment

## Main Features

- **Advanced Data Analysis**: Comprehensive analysis of enterprise architecture data
- **Business Intelligence**: Cost analysis, risk assessment, and KPI tracking
- **Security & Compliance Analysis**: Security scoring and compliance monitoring
- **Performance Optimization**: Performance metrics and availability analysis
- **Advanced Visualizations**: Interactive Plotly charts and correlation analysis
- **Comprehensive Reporting**: Detailed reports with actionable recommendations
- **Web Application**: Interactive Streamlit dashboard for data exploration


## Installation & Setup

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

## What the Program Analyzes

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


### Generated Files
- `cost_distribution.html` & `cost_distribution.png` - Interactive cost analysis visualizations
- `correlation_matrix.html` & `correlation_matrix.png` - Interactive correlation analysis heatmap
- `department_analysis.html` & `department_analysis.png` - Interactive department performance metrics
- `comprehensive_analysis_report.txt` - Detailed analysis report


## Requirements

- Python 3.8+
- pandas==2.3.1
- openpyxl==3.1.5
- matplotlib==3.10.5
- streamlit==1.47.1
- numpy==2.3.2
- plotly==5.17.0
