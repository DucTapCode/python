print("""
                                            ,----,                                                              
                                          ,/   .`|                                                              
    ,---,                               ,`   .'  :                      ,----..                                 
  .'  .' `\                           ;    ;     /          ,-.----.   /   /   \                ,---,           
,---.'     \          ,--,          .'___,/    ,'           \    /  \ |   :     :  ,---.      ,---.'|           
|   |  .`\  |       ,'_ /|          |    :     |            |   :    |.   |  ;. / '   ,'\     |   | :           
:   : |  '  |  .--. |  | :    ,---. ;    |.';  ;  ,--.--.   |   | .\ :.   ; /--` /   /   |    |   | |   ,---.   
|   ' '  ;  :,'_ /| :  . |   /     \`----'  |  | /       \  .   : |: |;   | ;   .   ; ,. :  ,--.__| |  /     \  
'   | ;  .  ||  ' | |  . .  /    / '    '   :  ;.--.  .-. | |   |  \ :|   : |   '   | |: : /   ,'   | /    /  | 
|   | :  |  '|  | ' |  | | .    ' /     |   |  ' \__\/: . . |   : .  |.   | '___'   | .; :.   '  /  |.    ' / | 
'   : | /  ; :  | : ;  ; | '   ; :__    '   :  | ," .--.; | :     |`-''   ; : .'|   :    |'   ; |:  |'   ;   /| 
|   | '` ,/  '  :  `--'   \'   | '.'|   ;   |.' /  /  ,.  | :   : :   '   | '/  :\   \  / |   | '/  ''   |  / | 
;   :  .'    :  ,      .-./|   :    :   '---'  ;  :   .'   \|   | :   |   :    /  `----'  |   :    :||   :    | 
|   ,.'       `--`----'     \   \  /           |  ,     .-./`---'.|    \   \ .'            \   \  /   \   \  /  
'---'                        `----'             `--`---'      `---`     `---`               `----'     `----'   
                                                                                                                
""")
chieucao = input("Nhập chiều cao của bạn (cm) :")
cannang = input("Nhap can nang cua ban (kg) :")
bmi = int(cannang)/(float(chieucao)/100)**2
print(int(bmi))