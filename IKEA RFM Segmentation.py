import pandas as pd

df = pd.read_csv('RetailCleaned.csv', header = None)
df.columns = ['Invoice', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 'Price', 'Customer_ID', 'Country', 'SourceSheet']
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
print(df.shape)
df.info()

# Filter and calculate Recency, Frequency, and Monetary values (RFM Metrics).
def calculate_rfm(df):
    rfm_data = df[(df['Customer_ID'].notna()) & (df['Quantity'] > 0)].copy()
    snapshot_date = pd.to_datetime('2011-12-10')  # Date of analysis.

    rfm = rfm_data.groupby('Customer_ID').agg(
        Recency=('InvoiceDate', lambda x: (snapshot_date - x.max()).days),
        Frequency=('Invoice', 'nunique'),
        Monetary=('Quantity', lambda x: (x * rfm_data.loc[x.index, 'Price']).sum())
    ).reset_index()
    return rfm

#Score customers and assign business segments
def score_and_segment(rfm):
    rfm['R_Score'] = pd.qcut(rfm['Recency'].rank(method='first'), 5, labels = [5, 4, 3, 2, 1]).astype(int)
    rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels = [1, 2, 3, 4, 5]).astype(int)
    rfm['M_Score'] = pd.qcut(rfm['Monetary'].rank(method='first'), 5, labels = [1, 2, 3, 4, 5]).astype(int)
    return rfm

def segment_customer(row):
    if row['R_Score'] >= 4 and row['F_Score'] >= 4:
        return 'Champions'
    elif row['R_Score'] >= 3 and row['F_Score'] >= 3:
        return 'Loyal Customers'
    elif row['R_Score'] <= 2 and row['F_Score'] >= 3:
        return 'At Risk'
    elif row['R_Score'] >= 4 and row['F_Score'] <= 2:
        return 'New Customers'
    elif row['R_Score'] <= 2 and row['F_Score'] <= 2:
        return 'Needs Attention'
    else:
        return 'Lost Customers'

#Merge RFM results back onto Transaction and Export
def merge_and_export(df, output_file, rfm):
    rfm['Segment'] = rfm.apply(segment_customer, axis=1)
    rfm['IsChurned'] = rfm['Recency'] > 90  # Assuming churned if recency is greater than 90 days.

    df= df[(df['Customer_ID'].notna()) & (df['Quantity'] > 0)].copy()
    df['InvoiceMonth'] = df['InvoiceDate'].dt.to_period('M').dt.to_timestamp()
    df['Revenue'] = df['Quantity'] * df['Price']

    df_final = df.merge(
        rfm[['Customer_ID', 'Recency', 'Frequency', 'Monetary', 'R_Score', 'F_Score', 'M_Score', 'Segment', 'IsChurned']],
        on='Customer_ID', how='left')
    output_file = 'EcommerceDashboardData.xlsx'

    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        df_final.to_excel(
        writer,
        sheet_name='Ecommerce Data',
        index=False)
    print(f"Excel file created successfully: {output_file}")

# Run the functions
rfm = calculate_rfm(df)
rfm = score_and_segment(rfm)
df_final = merge_and_export(df, 'EcommerceDashboardData.xlsx', rfm)
