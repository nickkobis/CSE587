
start: 
	start-all.sh

list: 
	hdfs dfs -ls /home/

#the I and O are the input and output of the hdfs
#to run:
#make run M=./mapper.py R=./reducer.py I=/home/gutenburg/ O=/home/output/takeX
run: 
	hadoop jar /home/cse587/hadoop-3.1.2/share/hadoop/tools/lib/hadoop-streaming-3.1.2.jar \
	-file $(M) -mapper "python3 $(M)" -file $(R) -reducer "python3 $(R)" -input $(I) -output $(O)

end: 
	stop-all.sh

setuphdfs:
	hdfs dfs -mkdir /home/ouput

#moves file from input to project file
#to run:
#make takeout I=part7 O=my_new_output_file
takeout:
	mkdir ./temp
	hsdf dfs -copyToLocal /home/output/$(I) ./temp/
	cp ./temp/part* $(O)
	rm ./temp/*
	rmdir ./temp
