def get_details():
        import sys
        import boto3

        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(sys.argv[1])
        username=sys.argv[2] #input('Enter User Name: ')
        lastname=sys.argv[3] #input('Enter Last Name: ')
        def getting(username,lastname):
                try:
                    	response = table.get_item(Key={ 'username': username, '$
                        item = response['Item']
                        print('User Found',item)
                except:
                       	print('User Not Found!! Sorry to Say!!')
        getting(username,lastname)
get_details()

