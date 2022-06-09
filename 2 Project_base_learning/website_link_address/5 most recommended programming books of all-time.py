'''
https://github.com/daolf/Most-recommended-programming-books#methodology
'''
def clean_link(link):
    link = link.encode().decode('ascii', errors='ignore')
    link = link.replace("'", '')
    link = link.lower()
    link = ' '.join([w for w in link.split(' ') if w not in ['the', 'a']])
    link = link.split('by')[0]
    link = link.split(':')[0]
    link = link.split('(')[0]
    link = ' '.join(link.split())
    link = link.replace('-', '_')
    link = ''.join([c for c in link if c.isalpha() or c == '_' or c == ' '])
    link = link.strip()
    link = link.replace(' ', '_')
    link = ''.join([c for c in link if c.isalpha() or c == '_'])
    return link

link = 'https://github.com/daolf/Most-recommended-programming-books#methodology'
link = "http://blog.sina.com.cn/s/blog_5def3a7f0102z3oi.html"
print(clean_link(link))