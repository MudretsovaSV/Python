import easygui
flavor=easygui.enterbox("What is your favorte ice cream flavor?",
                default='Vanilla')
easygui.msgbox("You picked "+flavor)
