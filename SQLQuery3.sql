--confirm the confirmation worked clearly
select count(*) as Total_Rows from RetailCombined
select count(*) as Failed_Dates from RetailCombined where InvoiceDate is null
select count(*) as Failed_Prices from RetailCombined where Price is null