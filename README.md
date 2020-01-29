## POSTBOX
```
Post Box is a simple restful mail delivery web application consisting of a flask.
```
### docker run
```
$ git clone git@github.com:byunseob/postbox.git

Change env (SMTP, ACCOUNT, PASSWORD)
 
$ docker-compose up -d

```


### Method
 - POST
### Body
 - to = [ (string, array) | required ] to_mail_address
 - cc = [ (string, array) | required ] cc_mail_address
 - alias = [string] mail sender alias (default: 42Maru Team)
 - subject = [ string | required ]
 - content = [ string(html) | required ] mail body
 - content_type = [string | ('html', 'plain')] mal_type (default: html)
 - file = [file] attach file
### Success Response
```
Code: 200
{
    "data": "success"
}
```            
##Sample Call

```
url = "http://YOUR-POSTBOX-HOST/mail"
files = {'file': open('file.txt', 'rb')}
values = {
    "to": ["byunseob@42maru.com", "wet814@42maru.com"],
    "cc": ["byunseob@42maru.com", "wet814@42maru.com"],
    "subject": "제목",
    "content": "hi",
    "alias": "byunseob",
    "content_type": "html"
}

requests.post(url, files=files, data=values)
```
            
            
