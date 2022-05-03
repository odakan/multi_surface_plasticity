import matplotlib
matplotlib.use("Agg")
from matplotlib.figure import Figure
from subprocess import Popen, PIPE
from numpy import loadtxt
import matplotlib.pyplot as plt


class MaterialTest():
    def __init__(self, parameters = None):
        #initialize material variables
        self.fields = { #default values
            'bulk modulus':         16750,
            'scale hardening':      1,
            'max strain':           1E-2,
            'increment strain':     1E-4,
            'Nloop':                0,
        }
        if parameters != None: #if parameters exists
            if len(parameters) < 5: #if parameters is not less than 5 vars
                #use user input values
                self.fields['bulk modulus'] = parameters(1)
                self.fields['scale hardening'] = parameters(2)
                self.fields['max strain'] = parameters(3)
                self.fields['increment strain'] = parameters(4)
                self.fields['Nloop'] = parameters(5)
        #prepare for .exe input
        self.argv = []
        for name, variable in self.fields.items():
            self.argv.append(variable)
        #call calculate    
        self.calculate()

    def calculate(self):
        # Call the executable to run Gauss point
        print("Start calculation! ")
        arg = ' '.join([str(x) for x in self.argv])
        command = 'multi_ys_VM.exe ' + arg 
        test = Popen(command, stdout=PIPE)
        #output = test.communicate()[0] #for debugging read the output

        print("Start Plotting! ")
        strain_stress = loadtxt('strain_stress.txt')
        strain = strain_stress[:,0]
        stress = strain_stress[:,1]

        print("First time plot!")
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        self.line, = self.ax.plot(strain,stress)
        plt.draw()
        self.figSave(self.argv)

    def figSave(self, values):
        figtitle = ""
        for idx,field in enumerate(self.fields):
            figtitle = figtitle + field +" = " + "{:.2E}".format(float(values[idx])) +'\n'  
        figtitle = figtitle + '\n\n'
        self.ax.set_title(figtitle)
        self.fig.savefig("strain_stress.png", bbox_inches='tight')


app = MaterialTest()
del app 