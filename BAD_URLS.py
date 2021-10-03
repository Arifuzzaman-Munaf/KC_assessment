def remove_extra_slash(url):
    """
    valid_url is the validated url without extra slashes
    flag is used for tracking the presence of extra slash
    """
    valid_url = ""
    flag = False
    for i in url:
        if flag and i == '/':
            continue
        elif i == '/':
            flag = True
            valid_url += i
        else:
            valid_url += i
            flag = False

    return valid_url


if __name__ == '__main__':
    url = input()
    print(remove_extra_slash(url))

"""
1. if flag = True and character i == '/' then we will not add any character to valid_url
2. otherwise we will add the character to our valid_url variable but the point to be noted.
3. if i == '/' then we will add the character to valid_url but make the flag == True 
4. otherwise make the flag == False
"""