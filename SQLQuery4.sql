--Check 1: Missing Customer ID
select count(*) as Missing_CustomerID
from RetailCombined where Customer_ID is null

--Check 2: Negative or Zero Qty.
select count(*) as Negative_Qty
from RetailCombined where Quantity <= 0

--Check 3: Missing Description
select count(*) as Missing_Description
from RetailCombined where Description is null

--Check 4: Exact duplicate rows
select Invoice, StockCode, Description, Quantity, InvoiceDate, Price, Customer_ID,Country,
		count(*) as ExactDupeCount
from RetailCombined
group by Invoice, StockCode, Description, Quantity, InvoiceDate, Price, Customer_ID, Country
having count(*) > 1