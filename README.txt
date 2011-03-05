

Examples:

Invoices:
./csvToLedger --open="~/desktop/test.csv" -a "Equity:Revenue, Liabilities:Taxes Payable, Assets:Accounts Receivables" -f "-total,-tax" -d "date" -n "note" -s "~/desktop/save.txt"

Payments:
./csvToLedger --open="~/desktop/test.csv" -a "Assets:Checking, Equity:Revenue" -f "amount" -d "timestamp" -n "projectname" -s "~/desktop/save.txt"

Expenses:
./csvToLedger --open="~/desktop/test.csv" -a "Equity:Expenses, Assets:Checking" -f "cost" -d "timestamp" -n "note" -s "~/desktop/save.txt"


Example File:

2008/08/23 * Bill for printing materials and hours
	Equity:Revenue		(119.01 * (-1))
	Liabilities:Taxes Payable		(1.014000 * (-1))
	Assets:Accounts Receivables
2009/10/09 * Bill for services and servicing server
	Equity:Revenue		(842.00 * (-1))
	Liabilities:Taxes Payable		(2.000000 * (-1))
	Assets:Accounts Receivables
2011/03/03 * Newsletter Graphics
	Assets:Checking		105.000000
	Equity:Revenue
2009/09/27 * Flash Player License
	Equity:Expenses		100.000000
	Assets:Checking
2009/09/27 * SVN Service
	Equity:Expenses		14.990000
	Assets:Checking