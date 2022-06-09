def remove_url_anchor(url):
    url = list(url)
    output = []
    if url.count('#'):
        for i in range(len(url)):
            if url[i]=='#':
                break
            output.append(url[i])
        output = ''.join(output)
        return output
    else:
        url = ''.join(url)
        return url
print(remove_url_anchor("www.codewars.com#about"))