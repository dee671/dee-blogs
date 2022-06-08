print ('static site builder')

#index
#reads top.html
top_html = open('./templates/top.html').read()

#reads middle.html
middle_html = open('./contents/index.html').read()

#reads bottom.html
bottom_html = open('./templates/bottom.html').read()

#assembles new middle.html
print ('combining html')
combined_html = top_html + middle_html + bottom_html
print (combined_html)

#writes brand new .html file in the same dir
open ('index.html', 'w+').write(combined_html)

#projects
top_html = open('./templates/top.html').read()

middle_html = open('./contents/projects.html').read()

bottom_html = open('./templates/bottom.html').read()

print ('combining html')
combined_html = top_html + middle_html + bottom_html
print (combined_html)

open ('projects.html', 'w+').write(combined_html)

#ventures
top_html = open('./templates/top.html').read()

middle_html = open('./contents/ventures.html').read()

bottom_html = open('./templates/bottom.html').read()

print ('combining html')
combined_html = top_html + middle_html + bottom_html
print (combined_html)

open ('ventures.html', 'w+').write(combined_html)

#contacts
top_html = open('./templates/top.html').read()

middle_html = open('./contents/contacts.html').read()

bottom_html = open('./templates/bottom.html').read()

print ('combining html')
combined_html = top_html + middle_html + bottom_html
print (combined_html)

open ('contacts.html', 'w+').write(combined_html)