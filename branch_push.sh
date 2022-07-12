now="$(date +%F-%H-%M-%S)";
git checkout -b "mr-${now}";
git add -A;
git commit -m 'new merge request';
git push -u origin "mr-${now}";
git checkout main;
git branch "$now" -d