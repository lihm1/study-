###
~~~
#!/bin/bash

if [ $1 == "-h" ];then
	echo "Usage: generate pbs file from template and SRR accession number."
	echo "Format: pbs_gen_v2.sh <pbs template> <file containing accession number>."
	echo "<head> in template file will be replaced by SRR accession number."
	echo "if <file containing accession number> is missed, all files like GSE\*.AC in current folder will be used."
	exit
fi

PBSFILE=$1
if test $2
then
	GEOLIST=$2
else
	GEOLIST=GSE*.AC
fi

for i in $(cat ${GEOLIST})
do
sed -r "s/<head>/${i}/g" $PBSFILE >${i}_$PBSFILE
done
~~~
