#forsøk på å lage en metode for generering av kode fra signalliste i excel

import openpyxl as pyxl
BaseFileName = "Kludrsheet.xlsx"

wb = pyxl.load_workbook(BaseFileName)

ws = wb.active
headers = []
sheetRows = ws.rows


listofCells = []
cVal = []
tempList = []

rowInt=0

#def getRowVals(_rowNum):
#    getRowNumber = _rowNum
 #   for c in row:
 #       rowCells


for row in ws.rows:
    for c in row:
        tempList.append(c.value)

    listofCells = tempList
    #print(listofCells)
    rowInt +=1

#print(sheetRows)

#print(listofCells)
print(ws.rows)
