import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')


count = data['Primary Fur Color'].value_counts()

print(count)

squirrels_count = pandas.DataFrame(count)
squirrels_count.to_csv('squirrel_count.csv')
print('\n\n')

print(squirrels_count)
