Sub Module2():

' Create variable to automatically find the last row in the workbook
Dim lastRow As Long

' Create variables to store yearly open, yearly close, yearly change,
' percent change, and total stock volume values
Dim Yearly_Open As Double
Dim Yearly_Close As Double
Dim Yearly_Change As Double
Dim Percent_Change As Double
Dim TSV As LongLong

' Create variables for greatest % increase and its corresponding ticker
Dim GPI As Double
Dim GPITicker As String

' Create variables for greatest % decrease and its corresponding ticker
Dim GPD As Double
Dim GPDTicker As String

' Create variables for greatest total volume and its corresponding ticker
Dim GTV As Double
Dim GTVTicker As String

' Create variable to hold the counter
Dim i As Long

' Loop through all sheets
For Each ws In Worksheets

    ' Set initial values for greatest % increase,
    ' greatest % decrease, and greatest total volume
    GPI = 0
    GPD = 0
    GTV = 0
    
    ' Activate current worksheet
    ws.Activate
    
    ' Find the last row of the workbook
    lastRow = Cells(Rows.Count, 1).End(xlUp).Row
    
    ' Set ticker value according to which row to start with
    ticker = 2
    
    ' Define where to find the values for yearly open and yearly close
    Yearly_Open = Range("C2").Value
    Yearly_Close = Range("F226").Value
    
    ' Total Stock Volume set to 0 initially
    TSV = 0

    ' Loop through each row until the last row of the workbook
    For i = 2 To lastRow

        ' Add current total stock value to next row's value
        TSV = TSV + Cells(i, 7).Value
    
        ' If the ticker symbol is the same as the next cell
        If Cells(i, 1).Value = Cells(i + 1, 1).Value Then
    
            ' Do nothing because it is the same ticker
        
            ' If the ticker symbol is the same as the previous cell
            If Cells(i, 1).Value = Cells(i - 1, 1).Value Then
        
                ' Do nothing because it is the same ticker
            
            ' If the ticker symbol is not the same as the next cell
            Else
        
                ' Store yearly open value from current row iteration in third column
                Yearly_Open = Cells(i, 3).Value
            
            End If
        
        ' If the ticker symbol is not the same as the next cell
        Else
        
            ' Place ticker symbol in appropriate cell
            Cells(ticker, 9).Value = Cells(i, 1).Value
            
            ' Store yearly close value from current row iteration in sixth column
            Yearly_Close = Cells(i, 6).Value
            
            ' Calculate yearly change and format the number to two decimals
            Yearly_Change = Yearly_Close - Yearly_Open
            Cells(ticker, 10).NumberFormat = "0.00"
            
            ' Place yearly change value in appropriate cell
            Cells(ticker, 10).Value = Yearly_Change
            
            ' If yearly change value is positive then
            If Cells(ticker, 10).Value > 0 Then
            
                ' Make cell green
                Cells(ticker, 10).Interior.ColorIndex = 4
                
            ' If yearly change value is negative then
            Else
            
                ' Make cell red
                Cells(ticker, 10).Interior.ColorIndex = 3
                
            End If
            
            ' Account for if yearly open value is 0
            If Yearly_Open = 0 Then
                ' Calculate percent change based on yearly open value being 0
                Percent_Change = Yearly_Change
            Else
                ' If yearly open value is not 0, use this to calculate percent change
                Percent_Change = Yearly_Change / Yearly_Open
            End If
            
            ' If percent change is greater than the current greatest percent increase
            If Percent_Change > GPI Then
                ' Set greatest percent increase as the percent change value
                GPI = Percent_Change
                ' Set the ticker for the percent change as the greatest percent increase ticker
                GPITicker = Cells(i, 1).Value
            End If
        
        
            ' If percent change is less than the current greatest percent decrease
            If Percent_Change < GPD Then
                ' Set greatest percent decrease as the percent change value
                GPD = Percent_Change
                ' Set the ticker for the percent change as the greatest percent decrease ticker
                GPDTicker = Cells(i, 1).Value
            End If
            
            ' If total stock volume is greater than the current greatest total volume
            If TSV > GTV Then
                ' Set greatest total volume as the total stock volume
                GTV = TSV
                ' Set the ticker for the total stock volume as the greatest total volume ticker
                GTVTicker = Cells(i, 1).Value
            End If
        
            ' Place percent change in appropriate cell
            Cells(ticker, 11).Value = Percent_Change
            
            ' Format how the percent change value is shown
            Cells(ticker, 11).NumberFormat = "0.00%"
            
            ' Place total stock volume in appropriate cell
            Cells(ticker, 12).Value = TSV
            
            ' Set ticker to a new ticker symbol
            ticker = ticker + 1
            
            ' Reset total stock volume value
            TSV = 0
            
        End If
    
    ' Call the next iteration
    Next i
    
' Record values for greatest percent increase ticker and greatest percent increase in the proper cells
Cells(2, 16).Value = GPITicker
Cells(2, 17).Value = GPI
' Format how the greatest percent increase value is shown
Cells(2, 17).NumberFormat = "0.00%"

' Record values for greatest percent decrease ticker and greatest percent decrease in the proper cells
Cells(3, 16).Value = GPDTicker
Cells(3, 17).Value = GPD
' Format how the greatest percent decrease value is shown
Cells(3, 17).NumberFormat = "0.00%"

' Record values for greatest total volume ticker and greatest total volume in the proper cells
Cells(4, 16).Value = GTVTicker
Cells(4, 17).Value = GTV
' Format how the greatest total volume value is shown
Cells(4, 17).NumberFormat = "0,000"

' Go to the next sheet in the workbook
Next ws

End Sub