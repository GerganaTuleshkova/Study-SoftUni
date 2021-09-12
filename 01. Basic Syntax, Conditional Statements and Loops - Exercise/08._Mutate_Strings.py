string1 = input()
string2 = input()

media_string = string2[0] + string1[1:(len(string1))]
if media_string != string1:
    print(media_string)

for index in range(1, len(string1)):
    #new_media_string = media_string[0:index] + string2[index] + media_string[(index+1):(len(string1))]
    new_media_string = media_string[:index] + string2[index] + media_string[(index + 1):]
    if new_media_string == media_string:
        continue
    else:
        media_string = new_media_string
    #media_string = media_string[index]
    print(media_string)
    if media_string == string2:
        break
