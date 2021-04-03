# 
while sleep 86400;
do
python3 baseball_scraper.py
git add .
git commit -m "daily stats update"
git push;
done