

start: 
	start-all.sh

list: 
	hdfs dfs -ls /home/

#to update write :
#update MAPPER_PATH=/home/cse589.... REDUCER_PATH=/home/cs..... 
update: 
	@echo "mapper path:" $(MAPPER_PATH)
	@echo "reducer path:" $(REDUCER_PATH) 
	@echo "input path:" $(INPUT_PATH_DFS) 
	@echo "output path:" $(OUTPUT_PATH_DFS)



#~/hadoop-3.1.2/share/hadoop/tools/lib
run: 
	hadoop jar /home/cse587/hadoop-3.1.2/share/hadoop/tools/lib/hadoop-streaming-3.1.2.jar \
	-file $(MAPPER_PATH) -mapper $(MAPPER_PATH) -file $(REDUCER_PATH) \
	-input $(INPUT_PATH_DFS) -output $(OUTPUT_PATH_DFS)

end: 
	stop-all.sh


