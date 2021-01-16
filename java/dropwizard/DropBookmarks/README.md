# DropBookmarks

How to start the DropBookmarks application
---

1. Run `mvn clean install` to build your application
1. Start application with `java -jar target/DropBookmarks-1.0-SNAPSHOT.jar server config.yml`
1. To check that your application is running enter url `http://localhost:8080`

Health Check
---

To see your applications health enter url `http://localhost:8081/healthcheck`

# My Commands and Tricks section

1. How to create the package?

<code>mvn archetype:generate -DgroupId=com.udemy -DartifactId=DropBookmarks -Dpackage=com.udemy.dropbookmarks -Dname=DropBookmarks -DarchetypeGroupId=io.dropwizard.archetypes -DarchetypeArtifactId=java-simple -DarchetypeVersion=2.0.9 -DinteractiveMode=false</code>

2. How to compile?

<code>mvn clean package</code>

3. How to run the server?
java -jar target/DropBookmarks-1.0-SNAPSHOT.jar server confg.yml



# Common issues