import matplotlib.pyplot as plt



class analysis:
    def __init__(self):
        self.count = 0
        self.xvals = []
        self.yvals = []
        

    def VisualizePopulation(self, population):
        self.xvals.append(self.count)
        self.yvals.append(population)
        self.count += 1

        plt.plot(self.xvals, self.yvals)
        plt.draw()
        plt.pause(0.5)
        plt.tight_layout()