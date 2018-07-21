def insert():
	import sys
        import boto3
        dynamodb = boto3.resource('dynamodb')
        table=dynamodb.Table(sys.argv[1])
        #print(sys.argv[1])

        table.put_item(Item={'username':'Ashwini','last_name':'Swain'})
        table.put_item(Item={'username':'Austin','last_name':'3:16'})
        table.put_item(Item={'username':'Darshit','last_name':'Surtiya'})
insert()

