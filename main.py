from bs4 import BeautifulSoup
import requests
import time

print('Enter Your Familier Skill')
fam_skill = input(':')
print('Filtering out {}....'.format(fam_skill))

def find_job():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Data+Analyst&txtLocation=').text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li', class_ ="clearfix job-bx wht-shd-bx")
    for index,job in enumerate(jobs):
        published_date = job.find('span', class_ ="sim-posted").span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_ ="joblist-comp-name").text.replace(' ','')
            skill = job.find('span',class_ = "srp-skills").text.replace(' ','')
            experience_location = job.find('ul', class_="top-jd-dtl clearfix").text.replace('card_travel','Experience: \n').replace('location_on','Location:')
            job_description = job.header.h2.a['href']
            if fam_skill in skill:
                with open(f'result/{index}.txt','w') as f:
                    f.write(f'Company Name: {company_name.strip()} \n')
                    f.write(f'\nSkills: {skill.strip()} \n')
                    f.write(f'\nMore Info: {job_description.strip()} \n')
                    f.write(f'{experience_location}')
                print(f'File Saved {index}...')
                
if __name__ == '__main__':
    while True:
        find_job()
        time_wait = 10
        print('Waiting for {} mins..'.format(time_wait))
        time.sleep(time_wait * 60)