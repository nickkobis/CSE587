
start: 
	start-all.sh

list: 
	hdfs dfs -ls /home/
	hdfs dfs -ls /home/output/

#the I and O are the input and output of the hdfs
#make sure home and /home/output exists in the hdfs
#to run:
#make run M=./mapper.py R=./reducer.py I=/home/gutenburg/ O=takeX
run: 
	hdfs dfs -mkdir -p /home
	hdfs dfs -mkdir -p /home/output
	hadoop jar /home/cse587/hadoop-3.1.2/share/hadoop/tools/lib/hadoop-streaming-3.1.2.jar \
	-file $(M) -mapper "python3 $(M)" -file $(R) -reducer "python3 $(R)" -input $(I) -output /home/output/$(O) 

run2: 
	hdfs dfs -mkdir -p /home
	hdfs dfs -mkdir -p /home/output
	hadoop jar /home/cse587/hadoop-3.1.2/share/hadoop/tools/lib/hadoop-streaming-3.1.2.jar -D mapred.reduce.tasks=1 \
	-file $(M) -mapper "python3 $(M)" -file $(R) -reducer "python3 $(R)" -input $(I) -output /home/output/$(O) 

end: 
	stop-all.sh

clean:
	rm ./output/*
	rm ./temp/*

clean_hadoop:
	hdfs dfs -rm /home/output/*/*
	hdfs dfs -rmdir --ignore-fail-on-non-empty /home/output/*

#moves file from input to project file
#make sure /home/ouput is set up in the hdfs
#to run:
#make takeout I=take7 O=my_new_output_file
takeout:
	mkdir -p ./temp
	mkdir -p ./output
	@hdfs dfs -copyToLocal -f /home/output/$(I)/part* ./temp/
	cp ./temp/part* ./output/$(O)
	rm ./temp/*
