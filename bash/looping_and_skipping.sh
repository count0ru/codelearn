X=1;
while [ $X -le 100 ]
do
        [ $((X%2)) != 0 ] && echo $X
        X=$((X+1));
done

