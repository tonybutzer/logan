#! /bin/bash
for i in 2013 ; do {
	echo $i;
	python rap_cog_creator.py -y $i &
}; done
