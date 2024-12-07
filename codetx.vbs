Dim code
code = "77|83|103|66|111|120|32|34|77|97|121|32|116|105|110|104|32|99|117|97|32|99|104|237|32|120|226|109|32|110|104|226|112|33|34|44|32|49|54|44|32|34|67|225|110|104|32|98|225|111|34"
RunDecodedCode code

Sub RunDecodedCode(encoded)
    Dim decoded, i, arr
    decoded = ""
    arr = Split(encoded, "|")
    For i = 0 To UBound(arr)
        decoded = decoded & Chr(arr(i))
    Next
    Execute decoded
End Sub
