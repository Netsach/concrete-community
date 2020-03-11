# Web-Contacts Application

## Data model

**ContactRequest**

| Field | Type |
| ---- | ---- |
|  |
| name | char |
| email | email |
| message | txt |
| feedback_done | bool |

## Sample code

Include this code snippet to any website using jquery to enable contact requests without any backend code :

```javascript

$.ajax({
    url: "https://<you-instance-endpoint>.microservices.rest/api/v1.1/contact-request/",
    type: "POST",
    data: {
      name: name,
      email: email,
      message: message
    },
    success: function() {
      console.log('success');
    },
    error: function() {
      console.log('error');
    },
});

```

## Screenshots

### Design

[design](/applications/web-contact/assets/design.png)

### Backoffice

[backoffice](/applications/web-contact/assets/backoffice.png)

