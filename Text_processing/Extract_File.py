file_path = input().split("\\")

file_extract = file_path[-1].split('.')
extension = file_extract[1]
file = file_extract[0]


print(f'File name: {file}')
print(f'File extension: {extension}')