now="$(date +%F-%H-%M-%S)";
git pull;
git add -A;
git commit -m "update ${now}";
git push
