# Core Library Resources

### Resource metadata schema

For each resource file, create a companion metadata file `<file_name>.json`.

```js
{
    // the version of metadata; this version is beta 0.0.1
    "metaVersion": "0.0.1",
    // alternative name for the file
    "alias": "A short description",
    // uploader name of the file
    "uploader": "Alice",
    // date in YYYY/MM/DD format
    "uploadDate": "2021/12/08",
    // a short description for the resource
    "description": "A very short description",
    // team member names
    "team": [
        "Bob Boba",
        "Cathy Cai"
    ],
    // institution name
    "institution": "UCSD",
    // study associated with the resource
    "study": "On how to create a distributed resource library.",
    // related studies
    "relatedStudies": [
        "Distributed resource library is good for reason A!",
        "Distributed resource library is good for reason B!",
        "Distributed resource library is bad for reason C...",
    ],
    // discussion links for the resource
    "discussions": [
        "https://meta.discourse.org/t/how-to-install-a-plugin-on-discourse-hosted-discourse/42783/6",
        "https://meta.discourse.org/t/discussion-of-resource",
        "other links..."
    ]
}
```
The folder where the resource is in is the category/tag of the file. For example, `consent_form/test.pdf` is under the category "consent_form".
