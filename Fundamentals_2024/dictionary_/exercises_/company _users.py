companies = {}
while True:
    company_data = input()

    if ' -> ' not in company_data:
        break

    company, id_ = company_data.split(' -> ')

    if company not in companies:
        companies[company] = []
    if id_ not in companies[company]:
        companies[company] += [id_]


for company in companies.keys():
    print(company)
    for id_ in companies[company]:
        print(f"-- {id_}")

