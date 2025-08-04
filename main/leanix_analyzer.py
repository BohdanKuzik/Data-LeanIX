import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

class LeanIXAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
        self.load_data()
    
    def load_data(self):
        try:
            self.df = pd.read_excel(self.file_path)
            print(f"Data loaded successfully!")
        except Exception as e:
            print(f"Error loading data: {e}")
    
    def basic_data_info(self):
        print("BASIC DATA INFORMATION")

        print(f"Total records: {len(self.df):,}")
        print(f"Total columns: {len(self.df.columns)}")
        print(f"Missing values: {self.df.isnull().sum().sum():,}")
        print(f"Duplicate records: {self.df.duplicated().sum():,}")
    
    def business_analysis(self):
        print("\n" + "="*50)
        print("BUSINESS ANALYSIS")

        if 'Business_Criticality' in self.df.columns:
            criticality_dist = self.df['Business_Criticality'].value_counts()
            print("Application criticality distribution:")
            for level, count in criticality_dist.items():
                percentage = (count / len(self.df)) * 100
                print(f"  {level}: {count} ({percentage:.1f}%)")
        
        if 'Maintenance_Cost' in self.df.columns and 'Development_Cost' in self.df.columns:
            total_maintenance = self.df['Maintenance_Cost'].sum()
            total_development = self.df['Development_Cost'].sum()
            total_cost = total_maintenance + total_development
            
            print(f"\nCost analysis:")
            print(f"  Total maintenance costs: ${total_maintenance:,.2f}")
            print(f"  Total development costs: ${total_development:,.2f}")
            print(f"  Total costs: ${total_cost:,.2f}")
            
            self.df['Total_Cost'] = self.df['Maintenance_Cost'] + self.df['Development_Cost']
            top_expensive = self.df.nlargest(5, 'Total_Cost')[['Application_Name', 'Total_Cost']]
            print(f"\nTop 5 most expensive applications:")
            for idx, row in top_expensive.iterrows():
                print(f"  {row['Application_Name']}: ${row['Total_Cost']:,.2f}")
        
        if 'Risk_Level' in self.df.columns:
            risk_dist = self.df['Risk_Level'].value_counts()
            high_critical_risk = risk_dist.get('High', 0) + risk_dist.get('Critical', 0)
            print(f"\nRisk analysis:")
            print(f"  Applications with high/critical risk: {high_critical_risk}")
            print(f"  Percentage of high-risk applications: {(high_critical_risk/len(self.df))*100:.1f}%")

    def create_advanced_charts(self):
        print("\n" + "="*50)
        print("CREATING CHARTS")

        if 'Maintenance_Cost' in self.df.columns and 'Development_Cost' in self.df.columns:
            fig = go.Figure()
            fig.add_trace(go.Histogram(
                x=self.df['Maintenance_Cost'],
                nbinsx=8,
                name='Maintenance Cost',
                marker_color='lightblue',
                opacity=0.7
            ))
            fig.update_layout(
                title='Maintenance Cost Distribution',
                xaxis_title='Cost ($)',
                yaxis_title='Number of Applications',
                template='plotly_white',
                width=600,
                height=400
            )
            fig.write_html('cost_distribution.html')
            try:
                fig.write_image('cost_distribution.png', width=600, height=400)
                print("Cost distribution chart saved as 'cost_distribution.html' and 'cost_distribution.png'")
            except Exception as e:
                print(f"Warning: Could not save PNG file: {e}")
                print("Cost distribution chart saved as 'cost_distribution.html' only")
        
        numeric_cols = ['Maintenance_Cost', 'Development_Cost', 'Performance_Score', 'Security_Score']
        available_cols = [col for col in numeric_cols if col in self.df.columns]
        
        if len(available_cols) >= 2:
            numeric_df = self.df[available_cols].dropna()
            if len(numeric_df) > 0:
                correlation_matrix = numeric_df.corr()
                
                fig = go.Figure(data=go.Heatmap(
                    z=correlation_matrix.values,
                    x=correlation_matrix.columns,
                    y=correlation_matrix.columns,
                    colorscale='RdBu',
                    zmid=0,
                    text=correlation_matrix.round(2).values,
                    texttemplate="%{text}",
                    textfont={"size": 10},
                    hoverongaps=False
                ))
                
                fig.update_layout(
                    title='Correlation Matrix',
                    template='plotly_white',
                    width=500,
                    height=400
                )
                fig.write_html('correlation_matrix.html')
                try:
                    fig.write_image('correlation_matrix.png', width=500, height=400)
                    print("Correlation matrix saved as 'correlation_matrix.html' and 'correlation_matrix.png'")
                except Exception as e:
                    print(f"Warning: Could not save PNG file: {e}")
                    print("Correlation matrix saved as 'correlation_matrix.html' only")
        
        if 'Owner_Department' in self.df.columns:
            dept_counts = self.df['Owner_Department'].value_counts()
            
            fig = go.Figure(data=go.Bar(
                x=dept_counts.index,
                y=dept_counts.values,
                marker_color='lightcoral',
                text=dept_counts.values,
                textposition='auto'
            ))
            
            fig.update_layout(
                title='Applications by Department',
                xaxis_title='Department',
                yaxis_title='Number of Applications',
                template='plotly_white',
                width=600,
                height=400,
                xaxis_tickangle=-45
            )
            fig.write_html('department_analysis.html')
            try:
                fig.write_image('department_analysis.png', width=600, height=400)
                print("Department analysis saved as 'department_analysis.html' and 'department_analysis.png'")
            except Exception as e:
                print(f"Warning: Could not save PNG file: {e}")
                print("Department analysis saved as 'department_analysis.html' only")
    
    def generate_comprehensive_report(self):
        print("\n" + "="*50)
        print("GENERATING COMPREHENSIVE REPORT")

        total_records = len(self.df)
        total_columns = len(self.df.columns)
        missing_values = self.df.isnull().sum().sum()
        completeness = ((total_records * total_columns - missing_values) / (total_records * total_columns)) * 100
        
        total_maintenance_cost = self.df['Maintenance_Cost'].sum() if 'Maintenance_Cost' in self.df.columns else 0
        total_development_cost = self.df['Development_Cost'].sum() if 'Development_Cost' in self.df.columns else 0
        avg_security_score = self.df['Security_Score'].mean() if 'Security_Score' in self.df.columns else 0
        avg_performance_score = self.df['Performance_Score'].mean() if 'Performance_Score' in self.df.columns else 0
        
        report = f"""
            COMPREHENSIVE LEANIX DATA ANALYSIS REPORT
            
            Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            
            MAIN METRICS:
            Total records: {total_records:,}
            Total columns: {total_columns}
            Missing values: {missing_values:,}
            Data completeness: {completeness:.1f}%
            
            BUSINESS METRICS:
            Total maintenance costs: ${total_maintenance_cost:,.2f}
            Total development costs: ${total_development_cost:,.2f}
            Total costs: ${total_maintenance_cost + total_development_cost:,.2f}
            Average security score: {avg_security_score:.1f}/100
            Average performance score: {avg_performance_score:.1f}/100
            
            COLUMN ANALYSIS:
        """
        
        for col in self.df.columns:
            missing_count = self.df[col].isnull().sum()
            missing_percent = (missing_count / total_records) * 100
            report += f"{col}: {missing_count} missing ({missing_percent:.1f}%)\n"
        
        if 'Business_Criticality' in self.df.columns:
            criticality_dist = self.df['Business_Criticality'].value_counts()
            report += f"\nAPPLICATION CRITICALITY DISTRIBUTION:\n"
            for level, count in criticality_dist.items():
                percentage = (count / total_records) * 100
                report += f"{level}: {count} ({percentage:.1f}%)\n"
        
        if 'Risk_Level' in self.df.columns:
            risk_dist = self.df['Risk_Level'].value_counts()
            high_critical_risk = risk_dist.get('High', 0) + risk_dist.get('Critical', 0)
            report += f"\nRISK ANALYSIS:\n"
            report += f"Applications with high/critical risk: {high_critical_risk}\n"
            report += f"Percentage of high-risk applications: {(high_critical_risk/total_records)*100:.1f}%\n"
        
        report += f"""
            RECOMMENDATIONS:
            1. Check columns with high percentage of missing data
            2. Establish rules for filling mandatory fields
            3. Regularly monitor data quality
            4. Create data cleaning process
            5. Improve security of applications with low scores
            6. Optimize performance of problematic applications
            7. Develop risk reduction plan for high-risk applications
            
            Created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        
        with open('comprehensive_analysis_report.txt', 'w', encoding='utf-8') as f:
            f.write(report)
        
        print("Comprehensive report saved as 'comprehensive_analysis_report.txt'")

    def run_analysis(self):
        print("RUNNING ADVANCED LEANIX DATA ANALYSIS")

        self.basic_data_info()
        self.business_analysis()
        self.create_advanced_charts()
        self.generate_comprehensive_report()
        
        print("\n" + "="*60)
        print("ANALYSIS COMPLETED!")
        print("Created files:")
        print("  cost_distribution.html & cost_distribution.png")
        print("  correlation_matrix.html & correlation_matrix.png")
        print("  department_analysis.html & department_analysis.png")
        print("  comprehensive_analysis_report.txt")
        print("\nThis analysis demonstrates:")
        print("  Data analysis skills")
        print("  Business analysis and KPIs")
        print("  Security and compliance analysis")
        print("  Creation of visualizations")
        print("  Generation of detailed reports")

if __name__ == "__main__":
    analyzer = LeanIXAnalyzer("main/sources/sample_leanix_data.xlsx")
    analyzer.run_analysis()
