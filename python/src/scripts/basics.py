
## First Python Script


# data files for this project are stored in the python/data/sample directory.
data_file='python/data/sample/AppleStore.csv'
data_file_2='python/data/sample/googleplaystore.csv'


from csv import reader

# open the file and store the contents in a list of lists
# file will be closed automatically after the nested block of code
with open(data_file, newline="", encoding="utf-8") as f:
    ios_data = list(reader(f))

# open the file and store the contents in a list of lists
# file will be closed automatically after the nested block of code
with open(data_file_2, newline="", encoding="utf-8") as f:
    android_data = list(reader(f))

# basic function to explore the data
def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line after each row

    if rows_and_columns:
        print('Number of rows:', len(dataset) - 1)
        print('Number of columns:', len(dataset[0]))

# explore the first 5 rows of the AppleStore dataset
explore_data(ios_data, 0, 5, True)
explore_data(android_data, 0, 5, True)

# print the length of one of the rows in the dataset 
# this row is a known outlier in the dataset, and it has fewer columns than the other rows
print(len(android_data[10473]))

# remove the outlier
del android_data[10473]

# check for duplicates in the dataset (by name of the app)
duplicate_apps=[]
unique_apps=[]

# populate the duplicate_apps and unique_apps lists
for app in android_data[1:]:
    name=app[0]
    ratings=app[3]
    if name in unique_apps:
        duplicate_apps.append(app)
    else:
        unique_apps.append(name)

# now we will remove the duplicates, keeping only the entry with the highest number of reviews
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

# make a dictionary to store unique apps by name
# with the app with the highest number of reviews for each name
android_unique_apps={}

for app in android_data[1:]:
    name=app[0]
    reviews=app[3]
    if name in android_unique_apps:
        app_in_dict=android_unique_apps[name]
        if app_in_dict[3]<reviews:
            android_unique_apps[name]=app
    else:
        android_unique_apps[name]=app

android_unique_apps_list=list(android_unique_apps.values())
print('Expected number of unique Android apps:', len(android_unique_apps))

explore_data(android_unique_apps_list, 0, 5, True)

ios_unique_apps={}

for app in ios_data[1:]:
    name=app[1]
    reviews=app[3]
    if name in ios_unique_apps:
        app_in_dict=ios_unique_apps[name]
        if app_in_dict[3]<reviews:
            ios_unique_apps[name]=app
    else:
        ios_unique_apps[name]=app

ios_unique_apps_list=list(ios_unique_apps.values())
print('Expected number of unique iOS apps:', len(ios_unique_apps))

# find apps with more than 3 non-ASCII characters in their name
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

# create a list of apps with English names, using the function we just created
android_english_apps=[]

for app in android_unique_apps_list:
    name=app[0]
    if check_lang(name) ==True:
       android_english_apps.append(app)

print('Number of Android English apps:', len(android_english_apps))

explore_data(android_english_apps, 0, 5, True)

ios_english_apps=[]

for app in ios_unique_apps_list:
    name=app[1]
    if check_lang(name) ==True:
       ios_english_apps.append(app)

print('Number of iOS English apps:', len(ios_english_apps))

## example of a markdown table to display data in a structured way
"""
| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |
"""

## now filter out the free apps from the English apps datasets
android_final=[]    

for app in android_english_apps:
    price=app[7]
    if price=='0':
        android_final.append(app)
print('Number of free Android apps:', len(android_final))

ios_final=[]

for app in ios_english_apps:
    price=float(app[4])
    if price==0.0:
        ios_final.append(app)   

print('Number of free iOS apps:', len(ios_final))

print('Examples of free Android apps:', android_final[:5])
print('\n') 
print('Examples of free iOS apps:', ios_final[:5])

print('\n') 
print(android_data[0])
print('\n') 
print(ios_data[0])

# we will now analyze the frequency table of genres for the free English apps in the Google Play store
def freq_table(dataset, index):
    table={}
    total=0
    for app in dataset:
        total+=1
        value=app[index]
        if value in table:
            table[value]+=1
        else:
            table[value]=1

    table_percentages={}
    for key in table:
        percentage=(table[key]/total)*100
        table_percentages[key]=percentage

    return table

def display_table(dataset, index):
    table = freq_table(dataset, index)
    table_display = []
    for key in table:
        key_val_as_tuple = (table[key], key)
        table_display.append(key_val_as_tuple)

    table_sorted = sorted(table_display, reverse = True)
    for entry in table_sorted:
        print(entry[1], ':', entry[0])

display_table(android_final, 9)

print('\n')
display_table(ios_final, 11)

categories_android = freq_table(android_final, 9)

for category in categories_android:
    total = 0
    len_category = 0
    for app in android_final:
        category_app = app[9]
        if category_app == category:
            n_installs = app[5]
            n_installs = n_installs.replace('+', '')
            n_installs = n_installs.replace(',', '')
            n_installs = float(n_installs)
            total += n_installs
            len_category += 1

    avg_n_installs = total / len_category
    print(category, ':', avg_n_installs)

    