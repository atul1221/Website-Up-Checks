# Website-Up-Checks
Mini project to check if website is up and running fine.

It is using response python library to get reponse from the website then it will log the output to the log file using logging library.

**HTTP response status codes**
Informational responses (100 – 199)<br>
Successful responses (200 – 299)<br>
Redirection messages (300 – 399)<br>
Client error responses (400 – 499)<br>
Server error responses (500 – 599)<br>


**Standard HTTP status codes in the range of 200 to 299**

200 OK: The request has succeeded.<br>
201 Created: The request has been fulfilled, resulting in the creation of a new resource.<br>
202 Accepted: The request has been accepted for processing, but the processing has not been completed.<br>
203 Non-Authoritative Information: The server is a transforming proxy and received a 200 OK response from the origin, but it's returning a modified version of the response.<br>
204 No Content: The server successfully processed the request, but there is no content to return.<br>
205 Reset Content: Tells the client to reset the document which sent this request.<br>
206 Partial Content: The server is delivering only part of the resource due to a range header sent by the client.<br>
207 Multi-Status: Provides status for multiple independent operations.<br>
208 Already Reported: Used inside a DAV: propstat response element to avoid repeatedly enumerating the internal members of multiple bindings to the same collection.<br>
226 IM Used: The server has fulfilled a request for the resource, and the response is a representation of the result of one or more instance-manipulations applied to the current instance.<br>

Author ~ Atul Sahay
