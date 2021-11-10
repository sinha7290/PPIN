Download the latest STRING dataset of Human protein protein interactions as edge list with third column as combined STRING score. Save the score wise sorted edge list as hppin_sort.txt
Save the combined scores of the edges in a separate file called combined_score.txt
run bash cutoff.sh to find the cutoff = X
get the line number (N) of the cutoff interaction using: grep -n (X-1) combined_score.txt|head -1
get the cutoff edge_list with combined score using:  sed -n -e '1,(N-1)p' hppin_sort.txt > hppin_cutoff.txt
get the modified edge list using: awk '{print $1,'\t',$2}' hppin_cutoff.txt > hppin.txt
get the sub-graph PPIN (edge_list.txt) and minimum spanning tree graph (MST.txt) based on the target protein list using: ppin.py 
