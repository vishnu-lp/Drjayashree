# import re
# regexp = re.compile('"[a-z]"/"[a-z]"')
# for line in open('example.txt').readlines():
#     if regexp.search(line):
#         o = open('.txt', 'w')
#         o.write(line)
#     else:
#         print("no")
# import fileinput
#
# with fileinput.FileInput('example.txt', inplace=True, backup='.bak') as file:
#     o = open('xyz.txt', 'w')
#     for line in file:
#         if 'image/' in line:
#             line.replace('image/', 'static/image/')
#         elif 'css/' in line:
#             line.replace('css/', 'static/css/')

with open('aboutus.html', 'r') as file:
    file_data = file.read()
    file_data = file_data.replace('href="static/images/', 'href="static/swap/images/')
    file_data = file_data.replace('link href="static/css/', 'link href="static/swap/css/')
    file_data = file_data.replace('link href="static/font-awesome/', 'link href="static/swap/font-awesome/')
    file_data = file_data.replace('src="static/images/', 'src="static/swap/images/')
    file_data = file_data.replace('src="static/js/', 'src="static/swap/js/')
    file_data = file_data.replace('href="static/bootstrap/', 'href="static/swap/bootstrap/')
    file_data = file_data.replace('content="static/images/', 'content="static/swap/images/')

with open('aboutus.html', 'w') as file:
    file.write(file_data)
