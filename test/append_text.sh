
filelist=`ls -1 ` 

for filename in $filelist ; do  

  sed  '3 a<link rel="stylesheet" href="./static_files/style.css" type="text/css" media="screen, projection">'  -i  $filename
  sed  '4 a<link rel="stylesheet" href="./static_files/layout.css" type="text/css" media="screen, projection">' -i  $filename
done
