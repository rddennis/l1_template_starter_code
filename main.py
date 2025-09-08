import jinja2

from datetime import datetime

today = datetime.now().strftime("%H:%M")

starter_template = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Welcome Page</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: linear-gradient(to right, #6dd5ed, #2193b0);
      color: #fff;
      text-align: center;
      padding-top: 15%;
      margin: 0;
      height: 100vh;
    }
    h1 {
      font-size: 3em;
      margin-bottom: 0.5em;
    }
    p {
      font-size: 1.5em;
      margin-top: 0;
    }
  </style>
</head>
<body>
  <h1>Welcome, User!</h1>
  <p>Good Morning!</p>
  <p>This page was developed at 09:45 AM.</p>
</body>
</html>

"""
