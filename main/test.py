#!/usr/bin/env python3
"""
Extended LeanIX data analysis test
Demonstrates advanced testing skills
"""

import pandas as pd
import numpy as np
from datetime import datetime

def test_data_loading():
    """Test data loading functionality"""
    print("🔍 Testing data loading...")
    
    try:
        df = pd.read_excel("sources/sample_leanix_data.xlsx")
        print(f"✅ Data loaded successfully!")
        print(f"   📊 Records: {len(df):,}")
        print(f"   📋 Columns: {len(df.columns)}")
        return df
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None

def test_basic_analysis(df):
    """Test basic data analysis"""
    print("\n🔍 Testing basic analysis...")
    
    # Test basic information
    print(f"📈 Total records: {len(df):,}")
    print(f"📋 Total columns: {len(df.columns)}")
    print(f"⚠️  Missing values: {df.isnull().sum().sum():,}")
    print(f"🔄 Duplicate records: {df.duplicated().sum():,}")
    
    # Test data types
    print(f"\n📊 Data types:")
    for dtype, count in df.dtypes.value_counts().items():
        print(f"   • {dtype}: {count} columns")
    
    print("✅ Basic analysis completed!")

def test_business_metrics(df):
    """Test business metrics calculation"""
    print("\n🔍 Testing business metrics...")
    
    # Test cost analysis
    if 'Maintenance_Cost' in df.columns and 'Development_Cost' in df.columns:
        total_maintenance = df['Maintenance_Cost'].sum()
        total_development = df['Development_Cost'].sum()
        total_cost = total_maintenance + total_development
        
        print(f"💰 Cost analysis:")
        print(f"   • Total maintenance costs: ${total_maintenance:,.2f}")
        print(f"   • Total development costs: ${total_development:,.2f}")
        print(f"   • Total costs: ${total_cost:,.2f}")
        
        # Test top expensive applications
        df['Total_Cost'] = df['Maintenance_Cost'] + df['Development_Cost']
        top_expensive = df.nlargest(3, 'Total_Cost')[['Application_Name', 'Total_Cost']]
        print(f"\n🏆 Top 3 most expensive applications:")
        for idx, row in top_expensive.iterrows():
            print(f"   • {row['Application_Name']}: ${row['Total_Cost']:,.2f}")
    
    # Test criticality analysis
    if 'Business_Criticality' in df.columns:
        criticality_dist = df['Business_Criticality'].value_counts()
        print(f"\n📊 Application criticality distribution:")
        for level, count in criticality_dist.items():
            percentage = (count / len(df)) * 100
            print(f"   • {level}: {count} ({percentage:.1f}%)")
    
    print("✅ Business metrics test completed!")

def test_security_analysis(df):
    """Test security analysis"""
    print("\n🔍 Testing security analysis...")
    
    # Test security scores
    if 'Security_Score' in df.columns:
        low_security = (df['Security_Score'] < 80).sum()
        avg_security = df['Security_Score'].mean()
        
        print(f"🛡️ Security analysis:")
        print(f"   • Average security score: {avg_security:.1f}/100")
        print(f"   • Applications with low security (<80): {low_security}")
        print(f"   • Percentage of low security applications: {(low_security/len(df))*100:.1f}%")
    
    # Test compliance status
    if 'Compliance_Status' in df.columns:
        compliance_dist = df['Compliance_Status'].value_counts()
        non_compliant = compliance_dist.get('Non-Compliant', 0)
        
        print(f"\n📋 Compliance analysis:")
        print(f"   • Non-compliant applications: {non_compliant}")
        print(f"   • Non-compliant percentage: {(non_compliant/len(df))*100:.1f}%")
    
    # Test vulnerability analysis
    if 'Vulnerability_Count' in df.columns:
        high_vulnerability = (df['Vulnerability_Count'] > 5).sum()
        avg_vulnerabilities = df['Vulnerability_Count'].mean()
        
        print(f"\n🔍 Vulnerability analysis:")
        print(f"   • Average vulnerabilities: {avg_vulnerabilities:.1f}")
        print(f"   • Applications with high vulnerability count (>5): {high_vulnerability}")
    
    print("✅ Security analysis test completed!")

def test_performance_analysis(df):
    """Test performance analysis"""
    print("\n🔍 Testing performance analysis...")
    
    # Test performance scores
    if 'Performance_Score' in df.columns:
        low_performance = (df['Performance_Score'] < 70).sum()
        avg_performance = df['Performance_Score'].mean()
        
        print(f"⚡ Performance analysis:")
        print(f"   • Average performance score: {avg_performance:.1f}/100")
        print(f"   • Applications with low performance (<70): {low_performance}")
        print(f"   • Percentage of low performance applications: {(low_performance/len(df))*100:.1f}%")
    
    # Test availability
    if 'Availability_Percentage' in df.columns:
        low_availability = (df['Availability_Percentage'] < 99).sum()
        avg_availability = df['Availability_Percentage'].mean()
        
        print(f"\n📈 Availability analysis:")
        print(f"   • Average availability: {avg_availability:.2f}%")
        print(f"   • Applications with low availability (<99%): {low_availability}")
    
    print("✅ Performance analysis test completed!")

def test_data_quality(df):
    """Test data quality assessment"""
    print("\n🔍 Testing data quality...")
    
    # Calculate completeness
    total_cells = len(df) * len(df.columns)
    missing_cells = df.isnull().sum().sum()
    completeness = ((total_cells - missing_cells) / total_cells) * 100
    
    print(f"📊 Data quality metrics:")
    print(f"   • Data completeness: {completeness:.1f}%")
    print(f"   • Total cells: {total_cells:,}")
    print(f"   • Missing cells: {missing_cells:,}")
    
    # Test for outliers in numeric columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    print(f"\n🔍 Outlier analysis:")
    for col in numeric_cols:
        if col in ['Performance_Score', 'Security_Score', 'Availability_Percentage']:
            # Check for values outside valid range
            if col == 'Performance_Score':
                invalid_count = ((df[col] < 0) | (df[col] > 100)).sum()
            elif col == 'Security_Score':
                invalid_count = ((df[col] < 0) | (df[col] > 100)).sum()
            elif col == 'Availability_Percentage':
                invalid_count = ((df[col] < 0) | (df[col] > 100)).sum()
            else:
                continue
            
            if invalid_count > 0:
                print(f"   ⚠️  {col}: {invalid_count} invalid values")
            else:
                print(f"   ✅ {col}: All values within valid range")
    
    print("✅ Data quality test completed!")

def main():
    """Main test function"""
    print("🚀 Running Advanced LeanIX Data Analysis Tests")
    print("="*60)
    
    # Test data loading
    df = test_data_loading()
    
    if df is None:
        print("❌ Cannot proceed with tests - data loading failed")
        return
    
    # Test basic analysis
    test_basic_analysis(df)
    
    # Test business metrics
    test_business_metrics(df)
    
    # Test security analysis
    test_security_analysis(df)
    
    # Test performance analysis
    test_performance_analysis(df)
    
    # Test data quality
    test_data_quality(df)
    
    print("\n" + "="*60)
    print("✅ All tests completed!")
    print("="*60)
    print("📝 Next steps:")
    print("  • Run the main analyzer: python leanix_analyzer.py")
    print("  • Start the web app: streamlit run streamlit_app.py")
    print("  • Check generated files and reports")

if __name__ == "__main__":
    main() 