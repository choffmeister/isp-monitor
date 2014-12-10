set terminal svg size 1280,800
set output "target/log.svg"
set datafile separator ";"
set xdata time
set timefmt x "%Y-%m-%d %H:%M:%S"
set format x "%Y-%m-%d\n%H:%M:%S"
set ylabel "latency"
set yrange [0:100]
set format y "%0.1f ms"
set ytics 10
set y2label "packet loss"
set y2range [0:100]
set format y2 "%0.f %%"
set y2tics 10

plot \
  "target/log.aggregated.csv" using 1:4 title "Average latency" with lines axes x1y1, \
  "target/log.aggregated.csv" using 1:(100-$3/$2*100) title "Packet loss" with lines axes x1y2
