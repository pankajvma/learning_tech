<!DOCTYPE html>
<html>

<head>

	<link rel="stylesheet" type="text/css" 
		  href="/resources/css/my-test.css">

    <script src="${pageContext.request.contextPath}/resources/js/simple-test.js"></script>

</head>

<body>
${pageContext.request.contextPath}
<h2>Spring MVC Demo - Home Page</h2>
<a href="hello/showForm">Plain Hello World</a>

<br><br>

<img src="${pageContext.request.contextPath}/imgs/spring-logo.png" />

<br><br>

<input type="button" onclick="doSomeWork()" value="Click Me"/>

</body>

</html>