## Word Meter MiSe (Micro Services)


Business Scenario
```
User will send a word in the front end
Flask FE will get the word and send it to Spring Backend
Spring BE will check with PostgresDB and get the meter
If the DB doesn't have the meter stored, Spring BE will call the Flask ML for the meter to be discovered
Once the Spring BE gets the meter for the new value, it will store the meter in the DB.
```

Folder Structure
```
word-meter-mise
    

```