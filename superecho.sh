for (( i=0; i<${#@}; i++ )); do
    echo ${@}[$i]
done

for i in $@; do
    echo $i
done
