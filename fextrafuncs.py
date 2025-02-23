"""
Fextrafuncs V0.1
Extra function from F language.
Producted by 86 Program Group.
See copyrights on fextrafuncs.Copyright().
2023/1/11 V0.1:None informations in this update.
"""
# Functions
from tkinter import messagebox as call
def Fcallback(mode,Type,inform):
    if mode == 'Shell':
        try:
            raise Type (inform)
        except NameError:
            raise NameError ('name {} is not defined'.format(Type))
        else:
            pass
    elif mode == 'FShell':
        call.showerror(Type,inform)
def Copyright(Mode):
    if Mode == 'Shell':
        print('Copyright (c) 2018-2023 86 Program Group.\nAll Rights Reserved.')
    elif Mode == 'FShell':
        call.showinfo('Copyright','Copyright (c) 2018-2023 86 Program Group.\nAll Rights Reserved.')
# Test codes(test functions above,do not run it!)
"""
Fcallback('Shell',RuntimeError,'Test callback')

Fcallback('Shell',UndefinedError,'Test invalid callback')

Fcallback('FShell','CodeGrammarError','Test F callback')

Copyright('Shell')

Copyright('FShell')
"""
