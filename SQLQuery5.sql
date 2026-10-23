--De-Duplicate and produce the final cleaned data
with Deduped as(
	select *,
	row_number() over(
		partition by Invoice, StockCode, Description, Quantity, InvoiceDate, Price, Customer_ID, Country
		order by (select null)) as RowNum
	from RetailCombined)
select Invoice, StockCode, Description, Quantity, InvoiceDate, Price, Customer_ID, Country, SourceSheet
into RetailCleaned
from Deduped
where RowNum = 1