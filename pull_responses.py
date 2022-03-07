import datetime
import requests
import json
import os
TYPEFORM_TOKEN = os.environ["TYPEFORM_TOKEN"]
FORM_ID = os.environ["FORM_ID"]

# {
#     "landing_id": "iee1xbkm5pik0ts7iee1hvcpdjk78kbh",
#     "token": "iee1xbkm5pik0ts7iee1hvcpdjk78kbh",
#     "response_id": "iee1xbkm5pik0ts7iee1hvcpdjk78kbh",
#     "landed_at": "2022-03-07T19:12:40Z",
#     "submitted_at": "2022-03-07T19:13:59Z",
#     "metadata": {
#         "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0",
#         "platform": "other",
#         "referer": "https://xiyan128.typeform.com/to/uRSli9Ir",
#         "network_id": "2cf2e805cb",
#         "browser": "default"
#     },
#     "hidden": {},
#     "calculated": {
#         "score": 0
#     },
#     "answers": [
#         {
#             "field": {
#                 "id": "EB2ZkayDU3mg",
#                 "ref": "9aae972a-3251-4a18-a74d-4d6b9c110d2d",
#                 "type": "short_text"
#             },
#             "type": "text",
#             "text": "A test"
#         },
#         {
#             "field": {
#                 "id": "4LjsZa5Uq23X",
#                 "ref": "3844c2e2-6a61-48f8-a993-5d10340508bc",
#                 "type": "short_text"
#             },
#             "type": "text",
#             "text": "Xiyan Shao"
#         },
#         {
#             "field": {
#                 "id": "35KvZ72b7LTS",
#                 "ref": "d1440abe-a46e-4a02-b8e3-93733aa1ab0a",
#                 "type": "dropdown"
#             },
#             "type": "text",
#             "text": "Consent Form"
#         },
#         {
#             "field": {
#                 "id": "nuoUDTK5CUcF",
#                 "ref": "0edd7fff-c7b8-48da-8d70-3f09f722594c",
#                 "type": "long_text"
#             },
#             "type": "text",
#             "text": "Tag1, tag2, tag3"
#         },
#         {
#             "field": {
#                 "id": "pte6YJazrkBb",
#                 "ref": "ed0beb38-1c59-4cea-b73c-58c8f879cc8b",
#                 "type": "long_text"
#             },
#             "type": "text",
#             "text": "This is just a test"
#         },
#         {
#             "field": {
#                 "id": "0rK1ljT0458x",
#                 "ref": "c1b06ec8-2daa-490d-8f46-d3d71b52e9c7",
#                 "type": "long_text"
#             },
#             "type": "text",
#             "text": "No team"
#         },
#         {
#             "field": {
#                 "id": "uFJF4cRAJnBz",
#                 "ref": "104c34e8-9866-40a3-a57e-e92946533f03",
#                 "type": "short_text"
#             },
#             "type": "text",
#             "text": "UCSD"
#         },
#         {
#             "field": {
#                 "id": "DjSGmIdC6GaF",
#                 "ref": "3f676924-609e-4ed4-ad0d-56b7db63f82b",
#                 "type": "short_text"
#             },
#             "type": "text",
#             "text": "not a study"
#         },
#         {
#             "field": {
#                 "id": "hIfd2vnbVIKC",
#                 "ref": "353eb39a-a700-4a07-ab34-199dad16d2f2",
#                 "type": "file_upload"
#             },
#             "type": "file_url",
#             "file_url": "https://api.typeform.com/forms/uRSli9Ir/responses/iee1xbkm5pik0ts7iee1hvcpdjk78kbh/fields/hIfd2vnbVIKC/files/0e8b57084959-1644276468183_1_2015_06_01_AEHIV_038_RP_V1.1_29MAY2015_clean.docx"
#         }
#     ]
# }

def get_feild_value(res, field_id):
    for answer in res["answers"]:
        if answer["field"]["id"] == field_id:
            return answer["text"]
    return None

def get_feild_file_url(res, field_id):
    for answer in res["answers"]:
        if answer["field"]["id"] == field_id:
            return answer["file_url"]
    return None

def text_to_list(text):
    return list(map(str.strip, text.split(",")))

def process_response(res):
    res_dict = {}
    res_dict["alias"] = get_feild_value(res, "EB2ZkayDU3mg")
    res_dict["uploader"] = get_feild_value(res, "4LjsZa5Uq23X")
    res_dict["upload_date"] = res["submitted_at"]
    res_dict["category"] = get_feild_value(res, "35KvZ72b7LTS")
    res_dict["tags"] = text_to_list(get_feild_value(res, "nuoUDTK5CUcF"))
    res_dict["description"] = get_feild_value(res, "pte6YJazrkBb")
    res_dict["team"] = text_to_list(get_feild_value(res, "0rK1ljT0458x"))
    res_dict["instituion"] = get_feild_value(res, "uFJF4cRAJnBz")
    res_dict["study"] = get_feild_value(res, "DjSGmIdC6GaF")
    return res_dict

if __name__ == "__main__":
    # fetch from https://api.typeform.com/forms
    url = f"https://api.typeform.com/forms/{FORM_ID}/responses"
    header = {"Authorization": f"Bearer {TYPEFORM_TOKEN}"}
    # one hour ago in ISO 8601 format
    params = {"since": (datetime.datetime.utcnow() - datetime.timedelta(hours=1)).replace(microsecond=0).isoformat()}
    response = requests.get(url, headers=header, params=params)
    print(response.url)
    if response.status_code == 200:
        print("Successfully fetched responses")
        responses = response.json()
        if len(responses["items"]) == 0:
            print("::set-output name=diff::false")
            exit(0)
        print("::set-output name=diff::true")
        for response in responses["items"]:
            res_dict = process_response(response)
            # download file
            file_url = get_feild_file_url(response, "hIfd2vnbVIKC")
            if file_url is not None:
                file_name = file_url.split("/")[-1]
                file_response = requests.get(file_url, headers=header)
                # get directory name as category name
                category = res_dict["category"]
                # create directory if not exists
                if not os.path.exists(category):
                    os.mkdir(category)
                # write file
                with open(f"{category}/{file_name}", "wb") as f:
                    f.write(file_response.content)
                print(f"Saved file {file_name} in {category}")
                
                # write json
                with open(f"{category}/{file_name}.json", "w") as f:
                    json.dump(res_dict, f)
                print(f"Saved json metadata file {file_name}.json in {category}")
    else:
        print("Failed to fetch responses")
        print("Response code: {}".format(response.status_code))
        print("Response text: {}".format(response.text))
    