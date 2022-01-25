# Core Library Resource

### Moderator Guide

When you receive a response from the Google Upload Forms, do the following

1. Upload the file to the directory associated with the resource’s category. For example, if this file is of category “Consent Form”, please upload the new resource under `/Consent Form`. Enter any comments as the commit message.
2. Create a companion metadata file. Filling the fields by referring to the schema described in the section below. After you have done that, upload the metadata file to the same directory as the resource.
3. Check the library GUI and see if the new resource is properly displayed. If the metadata is not shown, check if the name `<file_name>.json` matches the new resource `<file_name>` (e.g. `test.pdf` → `test.pdf.json`)
4. You are all set!

> Q: What if I'm not a moderator, but I want to contribute to this repo?
> 
> A: Create a new branch for this commit and start a pull request

> Q: Can I upload a resource using the local git client?
> 
> A: Of course. Use the normal `git add .`, `git commit`, and `git push` commands.


### Resource metadata schema

For each resource file, create a companion metadata file `<file_name>.json`.

```js
{
    // the version of metadata; this version is beta 0.0.1
    "metaVersion": "0.0.2",
    "category": "Consent Form", // not used yet
    "tags": [
        "GPS",
        "Wearable",
    ] // tags for searching
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
