"""
F-FuncPie V0.1.1
Extra function from F language.
Produced by 86 Program Group.
See copyrights on ffuncpie.Copyright().
2023/1/11 V0.1:None informations in this update.
2025/2/23 V0.1.1:Small Fixes.
"""
# Functions
from tkinter import messagebox as call
def Fcallback(mode,Type,info):
    if mode == 'Shell':
        try:
            raise Type (info)
        except NameError:
            raise NameError ('name {} is not defined'.format(Type))
        else:
            pass
    elif mode == 'FShell':
        call.showerror(Type,info)
def Copyright(Mode):
    if Mode == 'Shell':
        print('Copyright (c) 2018-2025 86 Program Group.\nAll Rights Reserved.')
    elif Mode == 'FShell':
        call.showinfo('Copyright','Copyright (c) 2018-2025 86 Program Group.\nAll Rights Reserved.')
# Test codes(test functions,do not run it!)
"""
Fcallback('Shell',RuntimeError,'Test callback')

Fcallback('Shell',UndefinedError,'Test invalid callback')

Fcallback('FShell','CodeGrammarError','Test F callback')

Copyright('Shell')

Copyright('FShell')
"""
