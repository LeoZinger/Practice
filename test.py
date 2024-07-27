# Calculate the Best SAT Score 
sat_list = [{"company": "google", "name":"tom", "sat": 98}, {"company": "google", "name": "greg", "sat": 95},
            {"company": "meta", "name": "ian", "sat": 98}, {"company": "meta", "name": "darren", "sat": 82},
            {"company": "amazon", "name": "tom", "sat": 97}, {"company": "amazon", "name": "nathan", "sat": 91},
            {"company": "microsoft", "name": "sam", "sat": 92}, {"company": "microsoft", "name": "peter", "sat": 98},
            ]


print(sat_list)
sat_res = {}
sat_count = {}

# sat_res["google"] = (str(sat_list[0]["sat"]), 1)
# print(sat_res)

for sat_map in sat_list:
    count = sat_count.get(sat_map["company"], 0) + 1
    print("Count = ", count)
    sat_count[sat_map["company"]] = count
    sat_res[sat_map["company"]] = (sat_res.get(sat_map["company"], (0, 0))[0] + sat_map["sat"], count)
    print(sat_res)

    sat_res_list = sorted(sat_res.items(), key=lambda x: x[1][0], reverse=True)
    print(sat_res_list)
    print("best SAT score: ", sat_res_list[0])



