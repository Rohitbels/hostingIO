import xlrd,xlwt






#open any sheet to copy the initial 5 columns
book = xlrd.open_workbook('1.xls',formatting_info=True)

#result workbook
workbook = xlwt.Workbook()


#add sheet in resulted workbook
worksheet = workbook.add_sheet('Sheet1')
sheet=book.sheet_by_index(0)


#Number of columns to be copied initially		
copyInitCols=range(0,2)

#get the all rows of the initial book to be copied in final book
#copies only the 
rows=sheet.get_rows()
rowNumber = 0
colNumber = 0
for row in rows:
	colNumber=0	
	for column in copyInitCols:		
			worksheet.write(rowNumber, colNumber,row[column].value)
			colNumber+=1
	rowNumber+=1		




#adding .xls to file name
def concate(x):
		return(`x`+".xls")

#
filName=map(concate,range(1,4))


copyRange=range(2,7)



icol=colNumber
for file in filName:
	book = xlrd.open_workbook(file,formatting_info=True)
	
	sheet=book.sheet_by_index(0)
	g=sheet.get_rows()
	
	row=0
	for x in g:
		col=icol
		for i in copyRange:
			if(row==0):
				worksheet.write(row, col,     file+x[i].value)		
			else:
				worksheet.write(row, col,     x[i].value)		
			

			col+=1
			
		row+=1
	icol=icol+(col-icol)		





workbook.save('Expenses01.xls')
