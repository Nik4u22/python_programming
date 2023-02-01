# Install necessary packages
# pip install beautifulsoup4
# pip install lxml
# pip install requests

from bs4 import BeautifulSoup
import requests

# Read data from static html file
with open('home.html', 'r') as html_file:
    content = html_file.read()
    
    # Create instance of BeautifulSoup
    soup = BeautifulSoup(content, 'lxml')
    print(soup.prettify())
    # Search for specific tag - store all h5 tags
    tags = soup.find('h5')
    print(tags)
    course_cards = soup.findall('div', class_='card')
    for course in course_cards:
        print(course)
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        print(f'{course_name} costs {course_price}')


# Scrap data from live online website
def find_jobs():
    html_text = requests.get('https://www.shine.com/job-search/fresher-jobs-in-nagpur?q=fresher&loc=Nagpur').text
    soup = BeautifulSoup(html_text, 'html.parser')
    job = soup.find('li', class_ = 'class_name')
    company_name = job.find('h3', class_ = 'class_name').text.replace('', '')
    skills = job.find('span', class_ = 'class_name').text

    #Write data in file
    with open(f'posts/{index}.txt', 'w') as f:
        f.write(f'Company Name: {company_name.strip()} \n')
        f.write(f'Required Skills: {skills.strip()} \n')
    print(f'File saved: {index}')