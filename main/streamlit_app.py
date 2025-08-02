import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from datetime import datetime

st.set_page_config(
    page_title="Advanced LeanIX Analyzer",
    page_icon="📊",
    layout="wide"
)

st.title("Advanced LeanIX Data Analyzer")
st.markdown("### Comprehensive tool for enterprise architecture analysis")

@st.cache_data
def load_data():
    try:
        df = pd.read_excel("sources/sample_leanix_data.xlsx")
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

def main():
    df = load_data()
    
    if df is None:
        st.error("Failed to load data. Please check the file path.")
        return
    
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox(
        "Select page:",
        ["Data Overview", "Business Analysis", "Security", "Performance", "Visualization", "Report"]
    )
    
    if page == "Data Overview":
        show_data_overview(df)
    elif page == "Business Analysis":
        show_business_analysis(df)
    elif page == "Security":
        show_security_analysis(df)
    elif page == "Performance":
        show_performance_analysis(df)
    elif page == "Visualization":
        show_visualization(df)
    elif page == "Report":
        show_report(df)

def show_data_overview(df):
    st.header("Data Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Records", f"{len(df):,}")
    
    with col2:
        st.metric("Columns", f"{len(df.columns)}")
    
    with col3:
        missing_count = df.isnull().sum().sum()
        st.metric("Missing Values", f"{missing_count:,}")
    
    with col4:
        completeness = ((len(df) * len(df.columns) - missing_count) / (len(df) * len(df.columns))) * 100
        st.metric("Data Completeness", f"{completeness:.1f}%")
    
    st.subheader("Data Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Data Types:**")
        dtype_info = df.dtypes.value_counts()
        for dtype, count in dtype_info.items():
            st.write(f"• {dtype}: {count} columns")
    
    with col2:
        st.write("**Column Names:**")
        for col in df.columns:
            st.write(f"• {col}")
    
    st.subheader("First 5 rows of data")
    st.dataframe(df.head(), use_container_width=True)
    
    st.subheader("Missing Data Analysis")
    missing_data = df.isnull().sum()
    
    if missing_data.sum() == 0:
        st.success("No missing data found!")
    else:
        missing_df = pd.DataFrame({
            'Column': missing_data.index,
            'Missing': missing_data.values,
            'Percentage': (missing_data.values / len(df)) * 100
        })
        missing_df = missing_df[missing_df['Missing'] > 0].sort_values('Missing', ascending=False)
        st.dataframe(missing_df, use_container_width=True)

def show_business_analysis(df):
    st.header("Business Analysis")
    
    if 'Business_Criticality' in df.columns:
        st.subheader("Application Criticality Distribution")
        criticality_dist = df['Business_Criticality'].value_counts()
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig, ax = plt.subplots(figsize=(4, 3))
            criticality_dist.plot(kind='bar', ax=ax, color='lightblue')
            plt.title('Criticality Distribution')
            plt.xticks(rotation=45)
            st.pyplot(fig)
        
        with col2:
            for level, count in criticality_dist.items():
                percentage = (count / len(df)) * 100
                st.metric(f"{level}", f"{count} ({percentage:.1f}%)")
    
    if 'Maintenance_Cost' in df.columns and 'Development_Cost' in df.columns:
        st.subheader("Cost Analysis")
        
        total_maintenance = df['Maintenance_Cost'].sum()
        total_development = df['Development_Cost'].sum()
        total_cost = total_maintenance + total_development
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Maintenance Costs", f"${total_maintenance:,.0f}")
        
        with col2:
            st.metric("Development Costs", f"${total_development:,.0f}")
        
        with col3:
            st.metric("Total Costs", f"${total_cost:,.0f}")
        
        df['Total_Cost'] = df['Maintenance_Cost'] + df['Development_Cost']
        top_expensive = df.nlargest(5, 'Total_Cost')[['Application_Name', 'Total_Cost']]
        
        st.subheader("Top 5 Most Expensive Applications")
        st.dataframe(top_expensive, use_container_width=True)
    
    if 'Risk_Level' in df.columns:
        st.subheader("Risk Analysis")
        risk_dist = df['Risk_Level'].value_counts()
        high_critical_risk = risk_dist.get('High', 0) + risk_dist.get('Critical', 0)
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig, ax = plt.subplots(figsize=(4, 3))
            risk_dist.plot(kind='bar', ax=ax, color=['green', 'yellow', 'orange', 'red'])
            plt.title('Risk Level Distribution')
            plt.xticks(rotation=45)
            st.pyplot(fig)
        
        with col2:
            st.metric("High/Critical Risk", f"{high_critical_risk}")
            st.metric("High-Risk Percentage", f"{(high_critical_risk/len(df))*100:.1f}%")

def show_security_analysis(df):
    st.header("Security and Compliance Analysis")
    
    if 'Compliance_Status' in df.columns:
        st.subheader("Compliance Status")
        compliance_dist = df['Compliance_Status'].value_counts()
        non_compliant = compliance_dist.get('Non-Compliant', 0)
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig, ax = plt.subplots(figsize=(4, 3))
            compliance_dist.plot(kind='bar', ax=ax, color='lightgreen')
            plt.title('Compliance Status')
            plt.xticks(rotation=45)
            st.pyplot(fig)
        
        with col2:
            st.metric("Non-Compliant", f"{non_compliant}")
            st.metric("Non-Compliant Percentage", f"{(non_compliant/len(df))*100:.1f}%")
    
    if 'Security_Score' in df.columns:
        st.subheader("Security Analysis")
        
        low_security = (df['Security_Score'] < 80).sum()
        avg_security = df['Security_Score'].mean()
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Average Security Score", f"{avg_security:.1f}/100")
        
        with col2:
            st.metric("Low Security (<80)", f"{low_security}")
        
        with col3:
            st.metric("Low Security Percentage", f"{(low_security/len(df))*100:.1f}%")
        
        fig, ax = plt.subplots(figsize=(6, 3))
        ax.hist(df['Security_Score'], bins=12, alpha=0.7, color='lightblue', edgecolor='black')
        ax.axvline(avg_security, color='red', linestyle='--', label=f'Average: {avg_security:.1f}')
        plt.title('Security Score Distribution')
        plt.xlabel('Security Score')
        plt.ylabel('Number of Applications')
        plt.legend()
        st.pyplot(fig)
    
    if 'Vulnerability_Count' in df.columns:
        st.subheader("Vulnerability Analysis")
        
        high_vulnerability = (df['Vulnerability_Count'] > 5).sum()
        avg_vulnerabilities = df['Vulnerability_Count'].mean()
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Average Vulnerabilities", f"{avg_vulnerabilities:.1f}")
        
        with col2:
            st.metric("High Vulnerability Count (>5)", f"{high_vulnerability}")
        
        with col3:
            st.metric("High Vulnerability Percentage", f"{(high_vulnerability/len(df))*100:.1f}%")

def show_performance_analysis(df):
    st.header("Performance Analysis")
    
    if 'Performance_Score' in df.columns:
        st.subheader("Performance Analysis")
        
        low_performance = (df['Performance_Score'] < 70).sum()
        avg_performance = df['Performance_Score'].mean()
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Average Performance Score", f"{avg_performance:.1f}/100")
        
        with col2:
            st.metric("Low Performance (<70)", f"{low_performance}")
        
        with col3:
            st.metric("Low Performance Percentage", f"{(low_performance/len(df))*100:.1f}%")
        
        fig, ax = plt.subplots(figsize=(6, 3))
        ax.hist(df['Performance_Score'], bins=12, alpha=0.7, color='lightgreen', edgecolor='black')
        ax.axvline(avg_performance, color='red', linestyle='--', label=f'Average: {avg_performance:.1f}')
        plt.title('Performance Score Distribution')
        plt.xlabel('Performance Score')
        plt.ylabel('Number of Applications')
        plt.legend()
        st.pyplot(fig)
    
    if 'Availability_Percentage' in df.columns:
        st.subheader("Availability Analysis")
        
        low_availability = (df['Availability_Percentage'] < 99).sum()
        avg_availability = df['Availability_Percentage'].mean()
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Average Availability", f"{avg_availability:.2f}%")
        
        with col2:
            st.metric("Low Availability (<99%)", f"{low_availability}")
        
        with col3:
            st.metric("Low Availability Percentage", f"{(low_availability/len(df))*100:.1f}%")

def show_visualization(df):
    st.header("Visualization")
    
    viz_type = st.selectbox(
        "Select visualization type:",
        ["Cost Distribution", "Correlation Matrix", "Department Analysis"]
    )
    
    if viz_type == "Cost Distribution":
        if 'Maintenance_Cost' in df.columns and 'Development_Cost' in df.columns:
            fig, ax = plt.subplots(figsize=(6, 4))
            ax.hist(df['Maintenance_Cost'], bins=8, alpha=0.7, color='lightblue', edgecolor='black')
            plt.title('Maintenance Cost Distribution')
            plt.xlabel('Cost ($)')
            plt.ylabel('Number of Applications')
            st.pyplot(fig)
    
    elif viz_type == "Correlation Matrix":
        numeric_cols = ['Maintenance_Cost', 'Development_Cost', 'Performance_Score', 'Security_Score']
        available_cols = [col for col in numeric_cols if col in df.columns]
        
        if len(available_cols) >= 2:
            numeric_df = df[available_cols].dropna()
            if len(numeric_df) > 0:
                fig, ax = plt.subplots(figsize=(4, 3))
                correlation_matrix = numeric_df.corr()
                sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, 
                           square=True, linewidths=0.5, ax=ax, fmt='.2f')
                plt.title('Correlation Matrix')
                st.pyplot(fig)
    
    elif viz_type == "Department Analysis":
        if 'Owner_Department' in df.columns:
            fig, ax = plt.subplots(figsize=(6, 4))
            dept_counts = df['Owner_Department'].value_counts()
            dept_counts.plot(kind='bar', color='lightcoral', ax=ax)
            plt.title('Applications by Department')
            plt.xlabel('Department')
            plt.ylabel('Number of Applications')
            plt.xticks(rotation=45)
            st.pyplot(fig)

def show_report(df):
    st.header("Comprehensive Analysis Report")
    
    total_records = len(df)
    total_columns = len(df.columns)
    missing_values = df.isnull().sum().sum()
    completeness = ((total_records * total_columns - missing_values) / (total_records * total_columns)) * 100
    
    total_maintenance_cost = df['Maintenance_Cost'].sum() if 'Maintenance_Cost' in df.columns else 0
    total_development_cost = df['Development_Cost'].sum() if 'Development_Cost' in df.columns else 0
    avg_security_score = df['Security_Score'].mean() if 'Security_Score' in df.columns else 0
    avg_performance_score = df['Performance_Score'].mean() if 'Performance_Score' in df.columns else 0
    
    report = f"""
# Comprehensive LeanIX Data Analysis Report

**Analysis Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Main Metrics
- **Total records:** {total_records:,}
- **Total columns:** {total_columns}
- **Missing values:** {missing_values:,}
- **Data completeness:** {completeness:.1f}%

## Business Metrics
- **Total maintenance costs:** ${total_maintenance_cost:,.2f}
- **Total development costs:** ${total_development_cost:,.2f}
- **Total costs:** ${total_maintenance_cost + total_development_cost:,.2f}
- **Average security score:** {avg_security_score:.1f}/100
- **Average performance score:** {avg_performance_score:.1f}/100

## Column Analysis
"""
    
    for col in df.columns:
        missing_count = df[col].isnull().sum()
        missing_percent = (missing_count / total_records) * 100
        report += f"- **{col}:** {missing_count} missing ({missing_percent:.1f}%)\n"
    
    if 'Business_Criticality' in df.columns:
        criticality_dist = df['Business_Criticality'].value_counts()
        report += f"\n## Application Criticality Distribution\n"
        for level, count in criticality_dist.items():
            percentage = (count / total_records) * 100
            report += f"- **{level}:** {count} ({percentage:.1f}%)\n"
    
    if 'Risk_Level' in df.columns:
        risk_dist = df['Risk_Level'].value_counts()
        high_critical_risk = risk_dist.get('High', 0) + risk_dist.get('Critical', 0)
        report += f"\n## Risk Analysis\n"
        report += f"- **Applications with high/critical risk:** {high_critical_risk}\n"
        report += f"- **Percentage of high-risk applications:** {(high_critical_risk/total_records)*100:.1f}%\n"
    
    report += f"""

## Recommendations
1. Check columns with high percentage of missing data
2. Establish rules for filling mandatory fields
3. Regularly monitor data quality
4. Create data cleaning process
5. Improve security of applications with low scores
6. Optimize performance of problematic applications
7. Develop risk reduction plan for high-risk applications

---
*Created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""
    
    st.markdown(report)
    
    st.download_button(
        label="Download Report",
        data=report,
        file_name=f"comprehensive_leanix_report_{datetime.now().strftime('%Y%m%d')}.md",
        mime="text/markdown"
    )

if __name__ == "__main__":
    main() 