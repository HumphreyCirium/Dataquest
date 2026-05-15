
## First Python Script



data_file='python/data/sample/AppleStore.csv'
data_file_2='python/data/sample/googleplaystore.csv'

opened_file = open(data_file)
from csv import reader

with open(data_file, newline="", encoding="utf-8") as f:
    ios_data = list(reader(f))


with open(data_file_2, newline="", encoding="utf-8") as f:
    android_data = list(reader(f))


def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line after each row

    if rows_and_columns:
        print('Number of rows:', len(dataset) - 1)
        print('Number of columns:', len(dataset[0]))

explore_data(ios_data, 0, 5, True)
explore_data(android_data, 0, 5, True)

print(len(android_data[9148]))

duplicate_apps=[]
unique_apps=[]

for app in android_data[1:]:
    name=app[0]
    ratings=app[3]
    if name in unique_apps:
        duplicate_apps.append(app)
    else:
        unique_apps.append(name)


pruned_apps=[]
pruned_apps_names=[]

for app in duplicate_apps:
    name=app[0]
    ratings=app[3]
    if name in pruned_apps_names:
        index=pruned_apps_names.index(name)
        if pruned_apps[index][3]<ratings:
            pruned_apps[index]=app
    else:
        pruned_apps.append(app)
        pruned_apps_names.append(name)



print('Number of pruned apps:', len(pruned_apps))
print('\n')
print('Examples of pruned apps:', pruned_apps[:15])
print('\n')
print('Number of unique apps:', len(unique_apps))

reviews_max={}

for app in android_data[1:]:
    name=app[0]
    reviews=app[3]
    if name in reviews_max and reviews_max[name]<reviews:
        reviews_max[name]=reviews
    elif name not in reviews_max:
        reviews_max[name]=reviews

print('Expected number of unique apps:', len(reviews_max))


print(len(reviews_max))

def check_lang(string):
    nonascii=0
    for character in string:
        if ord(character)>127:
            nonascii+=1
        if nonascii>3:
            return False        
    return True

print(check_lang('Instagram'))
print(check_lang('爱奇艺PPS -《欢乐颂2》电视剧热播'))
print(check_lang('Docs To Go™ Free Office Suite'))
print(check_lang('Instachat 😜'))   

english_apps=[]

for app in android_data[1:]:
    name=app[0]
    if check_lang(name) ==True:
       english_apps.append(app)

print('Number of English apps:', len(english_apps))

"""
| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |
"""