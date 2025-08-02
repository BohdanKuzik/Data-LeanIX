import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import seaborn as sns

class LeanIXAnalyzer:
    """
    Advanced LeanIX Data Analyzer for Junior Data Analyst
    Demonstrates advanced data analysis skills
    """
    
    def __init__(self, file_path):
        """Initialize the analyzer"""
        self.file_path = file_path
        self.df = None
        self.load_data()
    
    def load_data(self):
        """Load data from Excel file"""
        try:
            self.df = pd.read_excel(self.file_path)
            print(f"✅ Data loaded successfully!")
            print(f"   📊 Records: {len(self.df):,}")
            print(f"   📋 Columns: {len(self.df.columns)}")
            print(f"   📝 Column names: {list(self.df.columns)}")
        except Exception as e:
            print(f"❌ Error loading data: {e}")
    
    def basic_data_info(self):
        """Basic information about the data"""
        print("\n" + "="*50)
        print("📊 BASIC DATA INFORMATION")
        print("="*50)
        
        # Basic information
        print(f"📈 Total records: {len(self.df):,}")
        print(f"📋 Total columns: {len(self.df.columns)}")
        print(f"⚠️  Missing values: {self.df.isnull().sum().sum():,}")
        print(f"🔄 Duplicate records: {self.df.duplicated().sum():,}")
        
        # Data types
        print(f"\n📊 Data types:")
        for dtype, count in self.df.dtypes.value_counts().items():
            print(f"   • {dtype}: {count} columns")
    
    def missing_data_analysis(self):
        """Analysis of missing data"""
        print("\n" + "="*50)
        print("🔍 MISSING DATA ANALYSIS")
        print("="*50)
        
        missing_data = self.df.isnull().sum()
        
        if missing_data.sum() == 0:
            print("✅ No missing data found!")
        else:
            print("📋 Missing data by columns:")
            for col, missing_count in missing_data.items():
                if missing_count > 0:
                    missing_percent = (missing_count / len(self.df)) * 100
                    print(f"   • {col}: {missing_count} ({missing_percent:.1f}%)")
    
    def data_quality_score(self):
        """Calculate advanced data quality score"""
        print("\n" + "="*50)
        print("📊 DATA QUALITY SCORE")
        print("="*50)
        
        # Calculate data completeness
        total_cells = len(self.df) * len(self.df.columns)
        missing_cells = self.df.isnull().sum().sum()
        completeness = ((total_cells - missing_cells) / total_cells) * 100
        
        # Calculate data consistency
        consistency_score = self.calculate_consistency_score()
        
        # Calculate data accuracy
        accuracy_score = self.calculate_accuracy_score()
        
        # Overall quality score
        overall_quality = (completeness + consistency_score + accuracy_score) / 3
        
        print(f"📈 Data completeness: {completeness:.1f}%")
        print(f"🔄 Data consistency: {consistency_score:.1f}%")
        print(f"🎯 Data accuracy: {accuracy_score:.1f}%")
        print(f"📊 Overall quality score: {overall_quality:.1f}%")
        print(f"📊 Total cells: {total_cells:,}")
        print(f"⚠️  Missing cells: {missing_cells:,}")
        
        # Quality assessment
        if overall_quality >= 90:
            quality_level = "Excellent"
        elif overall_quality >= 80:
            quality_level = "Good"
        elif overall_quality >= 70:
            quality_level = "Satisfactory"
        else:
            quality_level = "Needs Improvement"
        
        print(f"🎯 Quality level: {quality_level}")
    
    def calculate_consistency_score(self):
        """Calculate data consistency score"""
        score = 100
        
        # Check consistency of numeric values
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            if col in ['Maintenance_Cost', 'Development_Cost', 'User_Count', 'Data_Volume_GB']:
                # Check for negative values
                negative_count = (self.df[col] < 0).sum()
                if negative_count > 0:
                    score -= (negative_count / len(self.df)) * 10
        
        # Check date consistency
        if 'Last_Updated' in self.df.columns:
            try:
                self.df['Last_Updated'] = pd.to_datetime(self.df['Last_Updated'])
                future_dates = (self.df['Last_Updated'] > datetime.now()).sum()
                if future_dates > 0:
                    score -= (future_dates / len(self.df)) * 10
            except:
                score -= 5
        
        return max(score, 0)
    
    def calculate_accuracy_score(self):
        """Calculate data accuracy score"""
        score = 100
        
        # Check for outliers in numeric columns
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            if col in ['Performance_Score', 'Security_Score', 'Availability_Percentage']:
                # Check for values outside valid range
                if col == 'Performance_Score':
                    invalid_count = ((self.df[col] < 0) | (self.df[col] > 100)).sum()
                elif col == 'Security_Score':
                    invalid_count = ((self.df[col] < 0) | (self.df[col] > 100)).sum()
                elif col == 'Availability_Percentage':
                    invalid_count = ((self.df[col] < 0) | (self.df[col] > 100)).sum()
                else:
                    continue
                
                if invalid_count > 0:
                    score -= (invalid_count / len(self.df)) * 10
        
        return max(score, 0)
    
    def business_analysis(self):
        """Business data analysis"""
        print("\n" + "="*50)
        print("💼 BUSINESS ANALYSIS")
        print("="*50)
        
        # Application criticality analysis
        if 'Business_Criticality' in self.df.columns:
            criticality_dist = self.df['Business_Criticality'].value_counts()
            print("📊 Application criticality distribution:")
            for level, count in criticality_dist.items():
                percentage = (count / len(self.df)) * 100
                print(f"   • {level}: {count} ({percentage:.1f}%)")
        
        # Cost analysis
        if 'Maintenance_Cost' in self.df.columns and 'Development_Cost' in self.df.columns:
            total_maintenance = self.df['Maintenance_Cost'].sum()
            total_development = self.df['Development_Cost'].sum()
            total_cost = total_maintenance + total_development
            
            print(f"\n💰 Cost analysis:")
            print(f"   • Total maintenance costs: ${total_maintenance:,.2f}")
            print(f"   • Total development costs: ${total_development:,.2f}")
            print(f"   • Total costs: ${total_cost:,.2f}")
            
            # Top 5 most expensive applications
            self.df['Total_Cost'] = self.df['Maintenance_Cost'] + self.df['Development_Cost']
            top_expensive = self.df.nlargest(5, 'Total_Cost')[['Application_Name', 'Total_Cost']]
            print(f"\n🏆 Top 5 most expensive applications:")
            for idx, row in top_expensive.iterrows():
                print(f"   • {row['Application_Name']}: ${row['Total_Cost']:,.2f}")
        
        # Risk analysis
        if 'Risk_Level' in self.df.columns:
            risk_dist = self.df['Risk_Level'].value_counts()
            high_critical_risk = risk_dist.get('High', 0) + risk_dist.get('Critical', 0)
            print(f"\n⚠️  Risk analysis:")
            print(f"   • Applications with high/critical risk: {high_critical_risk}")
            print(f"   • Percentage of high-risk applications: {(high_critical_risk/len(self.df))*100:.1f}%")
    
    def security_compliance_analysis(self):
        """Security and compliance analysis"""
        print("\n" + "="*50)
        print("🔒 SECURITY AND COMPLIANCE ANALYSIS")
        print("="*50)
        
        # Compliance analysis
        if 'Compliance_Status' in self.df.columns:
            compliance_dist = self.df['Compliance_Status'].value_counts()
            non_compliant = compliance_dist.get('Non-Compliant', 0)
            print(f"📋 Compliance status:")
            for status, count in compliance_dist.items():
                percentage = (count / len(self.df)) * 100
                print(f"   • {status}: {count} ({percentage:.1f}%)")
            print(f"   ⚠️  Non-compliant applications: {non_compliant}")
        
        # Security analysis
        if 'Security_Score' in self.df.columns:
            low_security = (self.df['Security_Score'] < 80).sum()
            avg_security = self.df['Security_Score'].mean()
            print(f"\n🛡️  Security analysis:")
            print(f"   • Average security score: {avg_security:.1f}/100")
            print(f"   • Applications with low security (<80): {low_security}")
            print(f"   • Percentage of low security applications: {(low_security/len(self.df))*100:.1f}%")
        
        # Vulnerability analysis
        if 'Vulnerability_Count' in self.df.columns:
            high_vulnerability = (self.df['Vulnerability_Count'] > 5).sum()
            avg_vulnerabilities = self.df['Vulnerability_Count'].mean()
            print(f"\n🔍 Vulnerability analysis:")
            print(f"   • Average number of vulnerabilities: {avg_vulnerabilities:.1f}")
            print(f"   • Applications with high vulnerability count (>5): {high_vulnerability}")
    
    def performance_analysis(self):
        """Performance analysis"""
        print("\n" + "="*50)
        print("⚡ PERFORMANCE ANALYSIS")
        print("="*50)
        
        if 'Performance_Score' in self.df.columns:
            low_performance = (self.df['Performance_Score'] < 70).sum()
            avg_performance = self.df['Performance_Score'].mean()
            print(f"📊 Performance analysis:")
            print(f"   • Average performance score: {avg_performance:.1f}/100")
            print(f"   • Applications with low performance (<70): {low_performance}")
            print(f"   • Percentage of low performance applications: {(low_performance/len(self.df))*100:.1f}%")
        
        if 'Availability_Percentage' in self.df.columns:
            low_availability = (self.df['Availability_Percentage'] < 99).sum()
            avg_availability = self.df['Availability_Percentage'].mean()
            print(f"\n📈 Availability analysis:")
            print(f"   • Average availability: {avg_availability:.2f}%")
            print(f"   • Applications with low availability (<99%): {low_availability}")
    
    def create_advanced_charts(self):
        """Create advanced charts"""
        print("\n" + "="*50)
        print("📈 CREATING ADVANCED CHARTS")
        print("="*50)
        
        # Set chart style
        plt.style.use('seaborn-v0_8')
        
        # 1. Cost distribution
        if 'Maintenance_Cost' in self.df.columns and 'Development_Cost' in self.df.columns:
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
            
            ax1.hist(self.df['Maintenance_Cost'], bins=20, alpha=0.7, color='skyblue', edgecolor='black')
            ax1.set_title('Maintenance Cost Distribution')
            ax1.set_xlabel('Maintenance Cost ($)')
            ax1.set_ylabel('Number of Applications')
            
            ax2.hist(self.df['Development_Cost'], bins=20, alpha=0.7, color='lightgreen', edgecolor='black')
            ax2.set_title('Development Cost Distribution')
            ax2.set_xlabel('Development Cost ($)')
            ax2.set_ylabel('Number of Applications')
            
            plt.tight_layout()
            plt.savefig('cost_distribution.png', dpi=300, bbox_inches='tight')
            print("📊 Cost distribution chart saved as 'cost_distribution.png'")
        
        # 2. Correlation matrix of numeric indicators
        numeric_cols = ['Maintenance_Cost', 'Development_Cost', 'User_Count', 'Data_Volume_GB', 
                       'Performance_Score', 'Security_Score', 'Availability_Percentage', 
                       'Integration_Count', 'Vulnerability_Count', 'Incident_Count_Last_Year']
        numeric_df = self.df[numeric_cols].dropna()
        
        if len(numeric_df) > 0:
            plt.figure(figsize=(12, 10))
            correlation_matrix = numeric_df.corr()
            sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, 
                       square=True, linewidths=0.5)
            plt.title('Correlation Matrix of Numeric Indicators')
            plt.tight_layout()
            plt.savefig('correlation_matrix.png', dpi=300, bbox_inches='tight')
            print("📊 Correlation matrix saved as 'correlation_matrix.png'")
        
        # 3. Department analysis
        if 'Owner_Department' in self.df.columns:
            plt.figure(figsize=(12, 8))
            
            # Number of applications by department
            dept_counts = self.df['Owner_Department'].value_counts()
            plt.subplot(2, 2, 1)
            dept_counts.plot(kind='bar', color='lightcoral')
            plt.title('Number of Applications by Department')
            plt.xticks(rotation=45)
            
            # Average costs by department
            if 'Total_Cost' in self.df.columns:
                dept_costs = self.df.groupby('Owner_Department')['Total_Cost'].mean().sort_values(ascending=False)
                plt.subplot(2, 2, 2)
                dept_costs.plot(kind='bar', color='lightblue')
                plt.title('Average Costs by Department')
                plt.xticks(rotation=45)
            
            # Average security score by department
            if 'Security_Score' in self.df.columns:
                dept_security = self.df.groupby('Owner_Department')['Security_Score'].mean().sort_values(ascending=False)
                plt.subplot(2, 2, 3)
                dept_security.plot(kind='bar', color='lightgreen')
                plt.title('Average Security Score by Department')
                plt.xticks(rotation=45)
            
            # Average performance score by department
            if 'Performance_Score' in self.df.columns:
                dept_performance = self.df.groupby('Owner_Department')['Performance_Score'].mean().sort_values(ascending=False)
                plt.subplot(2, 2, 4)
                dept_performance.plot(kind='bar', color='gold')
                plt.title('Average Performance Score by Department')
                plt.xticks(rotation=45)
            
            plt.tight_layout()
            plt.savefig('department_analysis.png', dpi=300, bbox_inches='tight')
            print("📊 Department analysis saved as 'department_analysis.png'")
    
    def generate_comprehensive_report(self):
        """Generate comprehensive report"""
        print("\n" + "="*50)
        print("📄 GENERATING COMPREHENSIVE REPORT")
        print("="*50)
        
        # Calculate metrics
        total_records = len(self.df)
        total_columns = len(self.df.columns)
        missing_values = self.df.isnull().sum().sum()
        completeness = ((total_records * total_columns - missing_values) / (total_records * total_columns)) * 100
        
        # Business metrics
        total_maintenance_cost = self.df['Maintenance_Cost'].sum() if 'Maintenance_Cost' in self.df.columns else 0
        total_development_cost = self.df['Development_Cost'].sum() if 'Development_Cost' in self.df.columns else 0
        avg_security_score = self.df['Security_Score'].mean() if 'Security_Score' in self.df.columns else 0
        avg_performance_score = self.df['Performance_Score'].mean() if 'Performance_Score' in self.df.columns else 0
        
        # Create report
        report = f"""
COMPREHENSIVE LEANIX DATA ANALYSIS REPORT
{'='*60}

Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

MAIN METRICS:
• Total records: {total_records:,}
• Total columns: {total_columns}
• Missing values: {missing_values:,}
• Data completeness: {completeness:.1f}%

BUSINESS METRICS:
• Total maintenance costs: ${total_maintenance_cost:,.2f}
• Total development costs: ${total_development_cost:,.2f}
• Total costs: ${total_maintenance_cost + total_development_cost:,.2f}
• Average security score: {avg_security_score:.1f}/100
• Average performance score: {avg_performance_score:.1f}/100

COLUMN ANALYSIS:
"""
        
        # Add column information
        for col in self.df.columns:
            missing_count = self.df[col].isnull().sum()
            missing_percent = (missing_count / total_records) * 100
            report += f"• {col}: {missing_count} missing ({missing_percent:.1f}%)\n"
        
        # Add criticality analysis
        if 'Business_Criticality' in self.df.columns:
            criticality_dist = self.df['Business_Criticality'].value_counts()
            report += f"\nAPPLICATION CRITICALITY DISTRIBUTION:\n"
            for level, count in criticality_dist.items():
                percentage = (count / total_records) * 100
                report += f"• {level}: {count} ({percentage:.1f}%)\n"
        
        # Add risk analysis
        if 'Risk_Level' in self.df.columns:
            risk_dist = self.df['Risk_Level'].value_counts()
            high_critical_risk = risk_dist.get('High', 0) + risk_dist.get('Critical', 0)
            report += f"\nRISK ANALYSIS:\n"
            report += f"• Applications with high/critical risk: {high_critical_risk}\n"
            report += f"• Percentage of high-risk applications: {(high_critical_risk/total_records)*100:.1f}%\n"
        
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
        
        # Save report
        with open('comprehensive_analysis_report.txt', 'w', encoding='utf-8') as f:
            f.write(report)
        
        print("📄 Comprehensive report saved as 'comprehensive_analysis_report.txt'")
        print("\n📋 REPORT CONTENT:")
        print(report)
    
    def run_analysis(self):
        """Run complete analysis"""
        print("🚀 RUNNING ADVANCED LEANIX DATA ANALYSIS")
        print("="*60)
        
        self.basic_data_info()
        self.missing_data_analysis()
        self.data_quality_score()
        self.business_analysis()
        self.security_compliance_analysis()
        self.performance_analysis()
        self.create_advanced_charts()
        self.generate_comprehensive_report()
        
        print("\n" + "="*60)
        print("✅ ANALYSIS COMPLETED!")
        print("="*60)
        print("📁 Created files:")
        print("  • cost_distribution.png")
        print("  • correlation_matrix.png")
        print("  • department_analysis.png")
        print("  • comprehensive_analysis_report.txt")
        print("\n🎯 This analysis demonstrates:")
        print("  • Advanced data analysis skills")
        print("  • Business analysis and KPIs")
        print("  • Security and compliance analysis")
        print("  • Creation of comprehensive visualizations")
        print("  • Generation of detailed reports")

if __name__ == "__main__":
    # Create analyzer
    analyzer = LeanIXAnalyzer("sources/sample_leanix_data.xlsx")
    
    # Run analysis
    analyzer.run_analysis() 