path=`pwd -P`

files=$(find $path/* -name "*.md")

for file in $files;do
    name=${file##*/}
    name=${name%.md}
    echo "# $name " > $file
done