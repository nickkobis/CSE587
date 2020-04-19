
start: 
	start-all.sh

list: 
	hdfs dfs -ls /home/
	hdfs dfs -ls /home/output/

#the I and O are the input and output of the hdfs
#make sure home and /home/output exists in the hdfs
#to run:
#make run M=./mapper.py R=./reducer.py I=/home/gutenberg/ O=takeX
run: 
	hdfs dfs -mkdir -p /home
	hdfs dfs -mkdir -p /home/output
	hadoop jar /home/cse587/hadoop-3.1.2/share/hadoop/tools/lib/hadoop-streaming-3.1.2.jar \
	-file $(M) -mapper "python3 $(M)" -file $(R) -reducer "python3 $(R)" -input $(I) -output /home/output/$(O)

#to run: (f is for file)
#make run1 F=1
run1:
	make run M=./part1/mapperp1.py R=./part1/reducerp1.py I=/home/gutenberg/ O=take_part1_$(F)
	make takeout I=take_part1_$(F) O=out_part1_$(F)
	cat ./output/out_part1_$(F)

run2:
	make run M=./part2/mapperp2_1.py R=./part2/reducerp2_1.py I=/home/gutenberg/ O=take_part21_$(F)
	make run M=./part2/mapperp2_2.py R=./part2/reducerp2_2.py I=/home/output/take_part21_$(F)/part* O=take_part22_$(F)
	make takeout I=take_part22_$(F) O=out_part2_$(F)
	cat ./output/out_part2_$(F)

run3:
	make run M=./part3/mapperp3.py R=./part3/reducerp3.py I=/home/gutenberg/ O=take_part3_$(F)
	make takeout I=take_part3_$(F) O=out_part3_$(F)
	cat ./output/out_part3_$(F)

run4:
	make run M=./part4/mapperp4.py R=./part4/reducerp4.py I=/home/csv/ O=take_part4_$(F)
	make takeout I=take_part4_$(F) O=out_part4_$(F)
	cat ./output/out_part4_$(F)

end: 
	stop-all.sh

clean:
	rm ./output/*

clean_hadoop:
	hdfs dfs -rm /home/output/*/*
	hdfs dfs -rmdir --ignore-fail-on-non-empty /home/output/*
	make clean
	clear

#moves file from input to project file
#make sure /home/ouput is set up in the hdfs
#to run:
#make takeout I=take7 O=my_new_output_file
takeout:
	mkdir -p ./temp
	mkdir -p ./output
	hdfs dfs -copyToLocal -f /home/output/$(I)/part* ./temp/
	cp ./temp/part* ./output/$(O)
	rm ./temp/*

