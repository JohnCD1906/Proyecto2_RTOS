# Graficador de senal sinusoidal aleatoria x[n] 
# Alan Carrasco y John Cesario

set style data lines
set autoscale

#------------- f(t) ----------------
set title "x[n]" font "18"
set xrange [0:250]
set xlabel   "M [Sample]" font ",18"
set ylabel   "x[n]" font ",18"
plot "x_n.dat"