title_of_article = input()
content_of_article = input()

print("<h1>\n\t"+f"{title_of_article}"+"\n</h1>")
print("<article>\n\t"+f"{content_of_article}"+"\n</article>")
comment_on_article = input()

while not comment_on_article == "end of comments":
    print("<div>\n\t" + f"{comment_on_article}" + "\n</div>")
    comment_on_article = input()

