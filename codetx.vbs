Set shell = CreateObject("WScript.Shell")

' Lặp để hiện nhiều hộp thoại
For i = 1 To 50
    MsgBox "Binh Bu Cu!", 16, "Binh Bu Lon!"
Next

' Tạo một vòng lặp vô hạn để mở Notepad liên tục (vui nhộn, nhưng có thể dừng được)
Do
    shell.Run "notepad.exe"
Loop
