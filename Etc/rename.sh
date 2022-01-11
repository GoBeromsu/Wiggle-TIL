path=`pwd -P`

files=$(find $path/* -name "*.md")

for file in $files;do
    name=${file##*/}
    name=${name%.md}
    echo -e "# $name\n" | cat - $file > $file.
    rm $file
    mv $file. $file
done