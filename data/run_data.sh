# example with 8 workers:
for i in $(seq 0 7); do
  python generate_dataset.py --total=1000000000 --out=logins --workers=8 --worker_id=$i &
done
wait
cat logins_part*.txt > logins_all_1B.txt
