# authentication system

## Get an anonymous user

### Request
- Url: api/user/anon
- Method: Get

### Response
```json
{
  "user_id": "${user_id}",
  "is_anonymous": true,
  "user_name":"anon",
  "user_ttl": -1
}
```
**user_ttl**
The time the anonymous account(and its data and files) can keep alive

The account gets removed:
- 0: It gets never expired (Normal account's data gets never expired)
- -1: When the session in the server expires
- ${number}: Number seconds after the last operation is made, no more less than 3600. 

## Register an normal user
### Request
- Url: api/register
- Method: Post

**Arguments**
user_name=${user_name}
email=${email}
password=${password}
### Response
**Success**
HTTP Code 200
```json
{
  "user_id": "${user_id}",
  "is_anonymous": "${boolean}",
  "user_name":"${user_name}",
  "user_ttl": "${number}"
}
```
**Failure**
HTTP Code 401
```json
{
  "failure_code": "${number}",
  "failure_reason": "${string}"
}
```

## Login
### Request
- Url: api/login
- Method: Post

**Arguments**

user_id=${userid}&password=${password}

### Response
**Success**
HTTP Code 200
```json
{
  "user_id": "${user_id}",
  "is_anonymous": "${boolean}",
  "user_name":"${user_name}",
  "user_ttl": "${number}"
}
```
**Failure**
HTTP Code 401
```json
{
  "failure_code": "${number}",
  "failure_reason": "${string}"
}
```

# instant_content

## Get the instant_contents

### Request
- Url: /instant_contents/${paginate_number} 
- Method: Get

**argument**
paginate_size=5

### Response
```json
{
  "total_page_number":"${number_number}",
  "current_page_number": "${number_current_page_number}",
  "contents_draft": {
      "instant_content_id": "${str_id}",
      "content_type": "${number}",
      "content": "${base64}",
      "compression_method":"${number}"
  },
  "contents":[{
      "instant_content_id": "${str_id}",
      "content_type": "${number}",
      "content": "${base64}",
      "compression_method":"${number}",
      "text_version_content": "${str_content}"
    }]
}
```

## Get the instant_content's text version content
This will trigger the convert and fill the data into the text_version_content field
### Request
- Url: /instant_content/${id}/text_version_content
- Method: Get

### Response
```json
{
  "text_version_content":"${str_content}"
}
```
## Get the latest instant_content

### Request
Get the latest instant_content
- Url: /instant_content/latest
Get the latest instant_content by the type
- Url: /instant_content/latest/type/${type}

### Response
```json
{
      "instant_content_id": "${str_id}",
      "content_type": "${number}",
      "content": "${base64}",
      "compression_method":"${number}",
      "text_version_content": "${str_content}"
}


```

## Write the instant content draft
Update the draft data
### Request
- Url: /instant_content/draft
- Method: Post

**argument**

content_type=${number}
content=${base64}
compression=${number}

### Response
```json
{
  "status": "success"
}
```
## Write the instant content 
Post a new instant content and delete the draft
### Request
- Url: /instant_content
- Method: Post

**argument**

content_type=${number}
content=${base64}
compression=${number}

### Response
```json
{
  "status": "success"
}
```

