
import requests
import bs4

s = requests.Session()

#s.get()

req = s.post('https://frbservices.org/EPaymentsDirectory/submitAgreement', data= {'agreementValue':'Agree'})

#print (req.text)

#s.get(https://www.frbservices.org/EPaymentsDirectory/search.html?AgreementSessionObject=Agree)

#https://www.frbservices.org/EPaymentsDirectory/detailACH.html?referredBy=detailFromAchResults&aba=011000015&displaySearchLinks=true

req = s.get('https://www.frbservices.org/EPaymentsDirectory/detailACH.html?referredBy=detailFromAchResults&aba=011000015&displaySearchLinks=true')

soup = bs4.BeautifulSoup(req.content, 'lxml')



details = [ 'detail_name', 'detail_location', 'detail_rn', 'detail_tn', 'detail_revised', 'detail_office_code', \
'detail_record_type', 'detail_new_rn', 'detail_status_code', 'detail_FRB']

data = {}

for detail in details:
    detail_content = soup.find(name='li', attrs={'id':detail})
    contents_split = str(detail_content).split('>')
#    print (detail_content)
    datastring = contents_split[3][:-4][1:]
    data[detail]=datastring
    print (datastring)


print (data)
#print (req.text)


#s.get(req)

#wget --post-data="agreementValue=Agree" https://frbservices.org/EPaymentsDirectory/submitAgreement --save-cookies cookie.txt --keep-session-cookies --delete-after


# https://github.com/albertico/frbs-fedwire-fedach/blob/master/FedACHdir_FORMAT.md
'detail_name', 'detail_location', 'detail_rn', 'detail_tn', 'detail_revised', 'detail_office_code', \
'detail_record_type', 'detail_new_rn', 'detail_status_code', 'detail_FRB'
# < ul class ="list-unstyled" >
#< li id = "detail_name" > < strong > Bank Name: < / strong > FEDERAL RESERVE BANK < / li >
#< li id = "detail_location" > < strong > Location: < / strong > ATLANTA, GA < / li >
#< li id = "detail_rn" > < strong > Routing Number: < / strong > 0110 - 0001 - 5 < / li >
#< li id = "detail_tn" > < strong > Telephone Number: < / strong > 877 - 372 - 2457 < / li >
#< li id = "detail_revised" > < strong > Revised: < / strong > December 24, 2015 < / li >
#< li id = "detail_office_code" > < strong > Office Code: < / strong > O < / li >
#< li id = "detail_record_type" > < strong > Record Type Code: < / strong > 0 < / li >
#< li id = "detail_new_rn" > < strong > New Routing Number: < / strong > Not Applicable < / li >
#< li id = "detail_status_code" > < strong > Institution Status Code: < / strong > 1 < / li >
#< li id = "detail_FRB" > < strong > Servicing FRB Number: < / strong > 011000015 < / li >
#< / ul >
