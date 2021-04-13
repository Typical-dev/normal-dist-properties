import random
import plotly.express as px
import plotly.figure_factory as ff
import scipy 
import statistics
count = []
result = []
for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    result.append(dice1 + dice2)
    count.append(i)
#fig = ff.create_distplot([result], ["result"])
#fig.show()
mean = statistics.mean(result)
median = statistics.median(result)
mode = statistics.mode(result)
sd = statistics.stdev(result)
print(f"mean: {mean}, median: {median}, mode: {mode}, Standard-deviation: {sd}")
first_sd_start, first_sd_end = mean - sd, mean + sd
second_sd_start, second_sd_end = mean - (2*sd), mean + (2*sd)
third_sd_start, third_sd_end = mean - (3*sd), mean + (3*sd)
oneSDarray = [r for r in result if r > first_sd_start and r < first_sd_end]
twoSDarray = [r for r in result if r > second_sd_start and r < second_sd_end]
threeSDarray = [r for r in result if r > third_sd_start and r < third_sd_end]
print(f"{len(oneSDarray)*100/len(result)} of data within one SD")
print(f"{len(twoSDarray)*100/len(result)} of data within two SD")
print(f"{len(threeSDarray)*100/len(result)} of data within three SD")