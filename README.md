# Twitter_data_collection
## About
This Project is about fetching the top trending tweets from the twitter for different countries using Tweepy Api along with the tweet volume and the tweet time stamp and using apache kafka to ingest the data in real time  and performing analysis and transformations on the data using Apache spark and storing the streaming data to MongoDb Atlas.
## Toolbox 🧰
<img src="https://cdn.worldvectorlogo.com/logos/python-5.svg" width="50" height="50" alt="Python"/> &emsp; <img src="https://cdn.worldvectorlogo.com/logos/apache-spark-5.svg" width="70" alt="Apache Spark" height="70"/>
&emsp; <img src="https://raw.githubusercontent.com/devicons/devicon/1119b9f84c0290e0f0b38982099a2bd027a48bf1/icons/apachekafka/apachekafka-original-wordmark.svg" width ="90" height="75" alt="Apache Kafka"/>
&emsp;<img src ="https://raw.githubusercontent.com/devicons/devicon/1119b9f84c0290e0f0b38982099a2bd027a48bf1/icons/mongodb/mongodb-original-wordmark.svg" width="70" height="70" alt="Mongo Db"/>

## Installation Steps
1.First we need to install Python(3.7) and java(jdk 8) On the machine for this projet to work appropiately.<br>
2.After the successfull installation of above we need to download and <a href="https://kafka.apache.org/">Install Kafka</a> version 2.6.0 with scala version 2.12.<br>
3.Now we Need to Download Apache Spark <a href ="https://spark.apache.org/downloads.html">Apache Spark </a>version 3.3.0 with hadoop version 3.3. Download the <a href="https://github.com/cdarlint/winutils">winUtils file</a> for hadoop version 3.<br>
4.Now we need to setup the path in enviornment variables for spark and haddop.<br>
5.Login to your mongo db atlas cluster and get the connection string to coonect to the database.<br>

## Deployment Process
### starting up zookeeper server on local host 9092
.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
### starting up kafka broker
.\bin\windows\kafka-server-start.bat .\config\server.properties
### Creating kafka topic 
.\bin\windows\kafka-topics.bat --create --topic <topic_name> --replication-factor 1 --partitions 1<br><br>
Now you kafka Broker is up , you need to deploy the above code in any on the IDE of your choice and you will start seeing the data in your mongodb cluster 

## Note
1.Since the kafka and mongo db connector are not part of the default spark package you need to define the connectors as the configuration while creating the spark session as mentioned in the code.<br>

2.While working with any IDE you need to import the spark and hadoop enviornment variable in the project structure under settings.
