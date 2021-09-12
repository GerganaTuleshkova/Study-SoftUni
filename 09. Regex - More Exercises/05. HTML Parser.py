import re

text = input()

pattern_raw = r"\<title\>(?P<title>.*)\<\/title\>.*\<body\>(?P<body>.*)\<\/body\>"

pattern_final = r"(?P<tag>\<[^\<\>]+\>)*(?P<take_text>[^\<\>])(?P<new_line>\\n)*(?P<end_tag>\<\/[^\<\>]+\>)*"
pattern_new_line = r"\\n"

extracted_text_iter = re.finditer(pattern_raw, text)
for info in extracted_text_iter:
    title_raw = info.group("title")
    body_raw = info.group("body")
    title_final_iter = re.finditer(pattern_final, title_raw)
    title_to_print = ""
    for iter_t in title_final_iter:
        title_to_print += iter_t.group("take_text")
    title_to_print_2 = re.sub(pattern_new_line, "", title_to_print)
    body_to_print = ""
    body_final_iter = re.finditer(pattern_final, body_raw)
    for iter_b in body_final_iter:
        body_to_print += iter_b.group("take_text")
    body_to_print_2 = re.sub(pattern_new_line, "", body_to_print)
    print(f"Title: {title_to_print_2}")
    print(f"Content: {body_to_print_2}")