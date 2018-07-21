#!/bin/bash

echo 'Existing Tables: '
aws dynamodb list-tables
echo 'Enter table-name to be created: '
read varname
python dynamodb_create.py $varname
echo 'After table creation, list of tables: '
aws dynamodb list-tables
echo 'Inserting into' $varname
python dynamodb_insert.py $varname
echo 'Values inserted!!'
echo 'Enter username to search: '
read username
echo 'Enter lastname to search: '
read lastname
python dynamodb_get.py $varname $username $lastname
echo 'Task of the table done!! Deleting the table $varname'
aws dynamodb delete-table --table-name $varname

