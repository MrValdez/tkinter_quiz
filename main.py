try:
    # python 2.x
    import Tkinter as tkinter
    import tkMessageBox as messagebox
except ImportError:
    # python 3.x
    import tkinter       
    import tkinter.messagebox as messagebox

class Application(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        
        self.Label1 = tkinter.Label(self)
        self.Label1["text"] = "Are you a boy or a girl?"
        
        image1 = tkinter.PhotoImage(data=
        """R0lGODlhUgBZAHAAACH5BAEAAPwALAAAAABSAFkAhwAAAAAAMwAAZgAAmQAAzAAA/wArAAArMwAr
ZgArmQArzAAr/wBVAABVMwBVZgBVmQBVzABV/wCAAACAMwCAZgCAmQCAzACA/wCqAACqMwCqZgCq
mQCqzACq/wDVAADVMwDVZgDVmQDVzADV/wD/AAD/MwD/ZgD/mQD/zAD//zMAADMAMzMAZjMAmTMA
zDMA/zMrADMrMzMrZjMrmTMrzDMr/zNVADNVMzNVZjNVmTNVzDNV/zOAADOAMzOAZjOAmTOAzDOA
/zOqADOqMzOqZjOqmTOqzDOq/zPVADPVMzPVZjPVmTPVzDPV/zP/ADP/MzP/ZjP/mTP/zDP//2YA
AGYAM2YAZmYAmWYAzGYA/2YrAGYrM2YrZmYrmWYrzGYr/2ZVAGZVM2ZVZmZVmWZVzGZV/2aAAGaA
M2aAZmaAmWaAzGaA/2aqAGaqM2aqZmaqmWaqzGaq/2bVAGbVM2bVZmbVmWbVzGbV/2b/AGb/M2b/
Zmb/mWb/zGb//5kAAJkAM5kAZpkAmZkAzJkA/5krAJkrM5krZpkrmZkrzJkr/5lVAJlVM5lVZplV
mZlVzJlV/5mAAJmAM5mAZpmAmZmAzJmA/5mqAJmqM5mqZpmqmZmqzJmq/5nVAJnVM5nVZpnVmZnV
zJnV/5n/AJn/M5n/Zpn/mZn/zJn//8wAAMwAM8wAZswAmcwAzMwA/8wrAMwrM8wrZswrmcwrzMwr
/8xVAMxVM8xVZsxVmcxVzMxV/8yAAMyAM8yAZsyAmcyAzMyA/8yqAMyqM8yqZsyqmcyqzMyq/8zV
AMzVM8zVZszVmczVzMzV/8z/AMz/M8z/Zsz/mcz/zMz///8AAP8AM/8AZv8Amf8AzP8A//8rAP8r
M/8rZv8rmf8rzP8r//9VAP9VM/9VZv9Vmf9VzP9V//+AAP+AM/+AZv+Amf+AzP+A//+qAP+qM/+q
Zv+qmf+qzP+q///VAP/VM//VZv/Vmf/VzP/V////AP//M///Zv//mf//zP///wAAAAAAAAAAAAAA
AAj/APcJHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePIEOKHHkQgEmSKAmaXAkg5UiW
MF2ChElTZkeaOG1qxMlTp0WeQFv6lBg06FCIRYX2PLowqdB9QJkmdKoyqtSCSUtavSqwKEKvXLsu
/Wo0LNSaCmvGNHv2adq1a9k+RNvWrdymcevavauVJVa/fN8CHpg38N/BhBEbrqpY72KDdBmffJy4
sdiVlCtj7juZcuTDnR8XBr2X72fSnkejFq1acmm2pyFbNhu7L+vZmWXjzr2aN97dvvW+Dq45NHHS
w+VuFZ6aau2wTsuajr5cOfXq0KW7fj50rGDuNnMiihUvlfz41jLNE0WfEjxD9yLhv2f/Evh54+nt
z9X/Ub5D+jPxt99m4Qn4n4EbARiRgh4xOCB+KDl4IIH5UZiRhBxh+B2EESK44VH+bZgcSSGSZaFO
6i2oYYMlFjeiSyn+tmJ/3k1VY3nauThjfNflCFuPO8IIJIeBXXfcZS0eqeSSTDbp5JNQRolSQAA7""")
        image2 = tkinter.PhotoImage(data=
"""R0lGODlhUgBZAHAAACH5BAEAAPwALAAAAABSAFkAhwAAAAAAMwAAZgAAmQAAzAAA/wArAAArMwAr
ZgArmQArzAAr/wBVAABVMwBVZgBVmQBVzABV/wCAAACAMwCAZgCAmQCAzACA/wCqAACqMwCqZgCq
mQCqzACq/wDVAADVMwDVZgDVmQDVzADV/wD/AAD/MwD/ZgD/mQD/zAD//zMAADMAMzMAZjMAmTMA
zDMA/zMrADMrMzMrZjMrmTMrzDMr/zNVADNVMzNVZjNVmTNVzDNV/zOAADOAMzOAZjOAmTOAzDOA
/zOqADOqMzOqZjOqmTOqzDOq/zPVADPVMzPVZjPVmTPVzDPV/zP/ADP/MzP/ZjP/mTP/zDP//2YA
AGYAM2YAZmYAmWYAzGYA/2YrAGYrM2YrZmYrmWYrzGYr/2ZVAGZVM2ZVZmZVmWZVzGZV/2aAAGaA
M2aAZmaAmWaAzGaA/2aqAGaqM2aqZmaqmWaqzGaq/2bVAGbVM2bVZmbVmWbVzGbV/2b/AGb/M2b/
Zmb/mWb/zGb//5kAAJkAM5kAZpkAmZkAzJkA/5krAJkrM5krZpkrmZkrzJkr/5lVAJlVM5lVZplV
mZlVzJlV/5mAAJmAM5mAZpmAmZmAzJmA/5mqAJmqM5mqZpmqmZmqzJmq/5nVAJnVM5nVZpnVmZnV
zJnV/5n/AJn/M5n/Zpn/mZn/zJn//8wAAMwAM8wAZswAmcwAzMwA/8wrAMwrM8wrZswrmcwrzMwr
/8xVAMxVM8xVZsxVmcxVzMxV/8yAAMyAM8yAZsyAmcyAzMyA/8yqAMyqM8yqZsyqmcyqzMyq/8zV
AMzVM8zVZszVmczVzMzV/8z/AMz/M8z/Zsz/mcz/zMz///8AAP8AM/8AZv8Amf8AzP8A//8rAP8r
M/8rZv8rmf8rzP8r//9VAP9VM/9VZv9Vmf9VzP9V//+AAP+AM/+AZv+Amf+AzP+A//+qAP+qM/+q
Zv+qmf+qzP+q///VAP/VM//VZv/Vmf/VzP/V////AP//M///Zv//mf//zP///wAAAAAAAAAAAAAA
AAj/APcJHEiwoMGDCBMqXMiwocOHECNKnEixosWLGDNq3Mixo8ePIEOKHElyI4CTKFGWDJmypcuV
Jl3KbAnT4sybL2tGxMkzpc6HOA8G/blwZkOjRBHK3JkzKcGlEqE63Sc1atOkVydm1blVK02sPjV+
/dmVYtmRY8WG5bpWrUq2bTOeBZk25luYdd2ehLvXY160cfUC4DvYb2DAdzn+Fbn4YmO6j70eRtzX
buWaka0mxpsZaOePn49OLjnX82jSoZWmBl1aYVWwqwW+djq7aGvMtQ0inar7plDfvFX35Bnc9XDg
xY0f35xcec/mkm9DF355utnT1kUzzw4xNveB3r9TW8Uunnrh8t3Joy8YPvjy59PfD48vnzj0+vbv
48/NvX1/9euBB2CA421H4G8GHsjegAH6l52D1kFIX4IKCkhhhQVWh+GCF2LY4YYghijiiCSWaOKJ
KKao4orNBQQAOw==
""")
        
        self.Button1 = tkinter.Button(self)
        self.Button1["command"] = self.Button1_Click
        self.Button1["image"] = image1
        self.Button1.photo = image1

        self.Button2 = tkinter.Button(self)
        self.Button2["command"] = self.Button2_Click
        self.Button2["image"] = image2
        self.Button2.photo = image2
                
        self.Label1.pack()        
        self.Button1.pack(side="left")
        self.Button2.pack(side="right")
        self.pack()
        
    def Button1_Click(self):
        messagebox.showinfo("Professor says", "You are handsome")
        
    def Button2_Click(self):
        messagebox.showinfo("Professor says", "You are beautiful")
        
root = tkinter.Tk()
app = Application(root)
app.mainloop()