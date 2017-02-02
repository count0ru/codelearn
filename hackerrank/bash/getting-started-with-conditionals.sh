read LINE
if [ $LINE == "y" ] || [ $LINE == "Y" ] 
        then echo "YES"
elif  [ $LINE == "n" ] || [ $LINE == "N" ] 
        then  echo "NO"
fi
